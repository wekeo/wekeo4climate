import xarray as xr
import pandas as pd
import csv
import netCDF4
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
from dateutil.parser import parse
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import rcParams
from cycler import cycler
import csv
import netCDF4
from scipy import stats



def ClipDataOnRegion(inputNcFileSpec, areaPerimeter, outputNcFileSpec):

    """ CLIP INPUT OVER INTERESTED AREA---> csv Perimeter Areas  have Column Names: LAT & LON
        areaPerimeter: pandas dataset delimiting the area being analysed. In the dataset, the 1st column is longitude,
        the 2nd column is latitude dataOutputNcFpath: path of the output nc file.
    """

    print("CMEMS SST Dimension:",inputNcFileSpec)
    print("Clipped Area Dimensions:",areaPerimeter)

    lat_max=areaPerimeter['LAT'].max()
    lat_min=areaPerimeter['LAT'].min()
    lon_max=areaPerimeter['LON'].max()
    lon_min=areaPerimeter['LON'].min()


    t = inputNcFileSpec.sel(lat=slice(lat_min,lat_max), lon=slice(lon_min,lon_max))

    print("Reseized Area:",t)

    print ('saving to ', outputNcFileSpec)
    t.to_netcdf(path=outputNcFileSpec)
    print ('finished saving')

    return t

def GenerateAnnualMeanMaps(t,annualMapsNcFile):

    """ Annual Mean map on previously clipped data within 33 years
    """
    def AM(month):

        return (month >= 1) & (month <= 12)

    lon_name   = t.lon[:]
    lat_name   = t.lat[:]

    am1 = t.sel(time=AM(t['time.month']))
    am2 = am1.groupby('time.year').mean('time')

    print ('ANNUAL MEAN for 33 years:', am2)

    print ('ANNUAL MEAN for 33 years:', am2)
    print("Annual Mean minimum T:", am2.thetao.min())
    print("Annual Mean maximum T:", am2.thetao.max())

    print ('saving to ', annualMapsNcFile)
    am2.to_netcdf(path=annualMapsNcFile)
    print ('finished saving')

def GenerateSeasonalWinter(t,NCoutputWINTER):

    """ Winter Period time selection for the creation of WINTER PERIOD NetCDF file, over previously clipped data
    """

    def WINTER(month):

        return (month >= 1) & (month <= 4)

    lon_name   = t.lon[:]
    lat_name   = t.lat[:]

    seasonal_data_winter = t.sel(time=WINTER(t['time.month']))
    seasonal_data_winter1 = seasonal_data_winter.groupby('time.year').mean()

    print("Reseized Area:",seasonal_data_winter1)
    print("WINTER SEASON MINIMUM TEMPERATURE AT SEA SURFACE:", seasonal_data_winter1.thetao.min())
    print("WINTER SEASON MAXIMUM TEMPERATURE AT SEA SURFACE:", seasonal_data_winter1.thetao.max())

    print ('saving to ', NCoutputWINTER)
    seasonal_data_winter1.to_netcdf(path=NCoutputWINTER)
    print ('finished saving')

    return seasonal_data_winter1

def GenerateSeasonalSummer(t,NCoutputSUMMER):

    """ Summer Period time selection for the creation of SUMMER PERIOD NetCDF file, over previously clipped data
    """

    def SUMMER(month):

        return (month >= 7) & (month <= 10)

    lon_name   = t.lon[:]
    lat_name   = t.lat[:]

    seasonal_data_summer = t.sel(time=SUMMER(t['time.month']))
    seasonal_data_summer1 = seasonal_data_summer.groupby('time.year').mean()

    print("Reseized Area:",seasonal_data_summer1)
    print("SUMMER SEASON MINIMUM TEMPERATURE AT SEA SURFACE:", seasonal_data_summer1.thetao.min())
    print("SUMMER SEASON MAXIMUM TEMPERATURE AT SEA SURFACE:", seasonal_data_summer1.thetao.max())

    print ('saving to ', NCoutputSUMMER)

    seasonal_data_summer1.to_netcdf(path=NCoutputSUMMER)
    return seasonal_data_summer1
    print ('finished saving')



def Generate1DFixDim(t,NcFile1Doutput):

    """ Mean sized LAT an LON  1 dimensional NetCDF file over previously clipped data, for the next csv file creation function
    """

    lon_name = 'lon'
    lat_name = 'lat'
    fy_1D= t.mean(dim=(lat_name, lon_name), skipna=True)
    fy_1D.to_dataframe()
    print ('saving to ', NcFile1Doutput)
    fy_1D.to_netcdf(path=NcFile1Doutput)
    print ('finished saving')
    print("File Dimension:",fy_1D)

    return fy_1D


def Generate1DFixDimCSV(fy_1D,NcFile1DoutputCSV):

    """ Mean sized LAT an LON  1 dimensional CSV file over previously clipped data
    """

    nc = netCDF4.Dataset(fy_1D, mode='r')

    nc.variables.keys()

    time_var = nc.variables['time']
    dtime = netCDF4.num2date(time_var[:],time_var.units)
    temp = nc.variables['thetao'][:]

    temp_ts = pd.Series(temp, index=dtime)

    temp_ts.to_csv(NcFile1DoutputCSV,index=True)

    file2 = pd.read_csv(NcFile1DoutputCSV)
    headerList = ['DATE', 'TEMPERATURE']
    file2.to_csv(NcFile1DoutputCSV, header=headerList, index=False)

    return temp_ts



def Generate1DTendency(t,NcFile1Doutput):

    """ read file 1D fix dimension NetCDF file for the overall SST tendency
    """

    lon_name = 'lon'
    lat_name = 'lat'

    fy_1D= t.mean(dim=(lat_name, lon_name), skipna=True)
    fy_dt = fy_1D.groupby('time.year').mean()
    df = fy_dt.to_dataframe().reset_index().set_index('year')

    x=df.index
    y=df.thetao

    slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
    k=intercept + slope*x
    fig, axes = plt.subplots(1, figsize=(18,8), dpi= 100)

    plt.plot(df.thetao, color='teal', marker='o', markerfacecolor='firebrick', markeredgecolor='g', markersize=8)
    plt.plot(x, k, 'k')
    plt.grid()
    plt.title('Sea Surface Temperature Annual Trend in the Adriatic Sea', size=20)
    plt.ylabel('Sea Surface Temperature [°C]',fontsize=18)
    plt.xlabel('TS by years',fontsize=15)
    plt.xticks(size = 15)
    plt.yticks(size = 15)
    plt.savefig('image_outputs/annualTrend.png')


def GenerateDailyTimeSeries(temp_ts):

    """ Daily TS SST Analysis
    """

    file2 = pd.read_csv(temp_ts,index_col='DATE', parse_dates=['DATE'])
    fig, axes = plt.subplots(1, figsize=(18,8), dpi= 100)

    plt.title('Sea Surface Temperature Time Series, Daily Trend in the Adriatic Sea', size=20)
    plt.grid()
    plt.plot(file2, color='teal')
    plt.ylabel('Sea Surface Temperature [°C]',fontsize=18)
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.savefig('image_outputs/tsTrend.png')


def GenerateDailyTimeSeriesSTD(temp_ts):

    """ Daily TS STD Analysis
    """

    file2 = pd.read_csv(temp_ts,index_col='DATE', parse_dates=True)
    fy_dt = file2.groupby(pd.Grouper(freq='M')).mean()


    daily_sdT = fy_dt.rolling(window = 12).std()
    fig, axes = plt.subplots(1, figsize=(18,8), dpi= 100)

    plt.title('Sea Surface Temperature Standard Deviation in the Adriatic Sea', size=20)
    plt.grid()
    plt.plot(daily_sdT, color='teal')
    plt.ylabel('Sea Surface Temperature [°C]',fontsize=18)
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.savefig('image_outputs/std_sst.png')
    return daily_sdT

def GenerateDailyTimeSeriesPLOT(temp_ts):

    """ Monthly Mean TS Violin Plot
    """

    file2 = pd.read_csv(temp_ts, parse_dates=['DATE'])
    file2['Time Series from 1987 to 2019'] = [d.year for d in file2.DATE]
    file2['Month'] = [d.strftime('%b') for d in file2.DATE]
    years = file2['Time Series from 1987 to 2019'].unique()
    plt.style.use('seaborn')

    fig, axes = plt.subplots(1, figsize=(18,8), dpi= 100)
    sns.violinplot(x='Month', y='TEMPERATURE', data=file2.loc[~file2.Month.isin([1987, 2019]), :], palette="tab10", bw=.2, cut=1, linewidth=1)

    axes.set_title('Monthly Mean Sea Surface Temperature in the Adriatic Sea from 1987 to 2019', fontsize=20);
    plt.xticks(size = 20)
    plt.yticks(size = 20)
    plt.xlabel('Months',fontsize=18)
    plt.ylabel('Sea Surface Temperature [°C]',fontsize=18)
    plt.savefig('image_outputs/MonthlyMean.png')




def computeSenSlopeMap(seasonalMapsNcFile, outputNcFile):

    inputDs = xr.open_dataset(seasonalMapsNcFile)



##vals: per input data Summer and Winter Season Files
##a method for robust linear regression. It computes the slope as the median of all slopes (all seasonal mean) between paired values.
    def _compSenSlope(vals):
        alpha = .95
        medslope, _, _, _ = stats.mstats.theilslopes(vals, alpha=alpha)
        return medslope
###Apply a vectorized function for unlabeled arrays on xarray objects.
###xarray.apply_ufunc
###The function will be mapped over the data variable(s) of the input arguments

    slp = xr.apply_ufunc(_compSenSlope, inputDs, input_core_dims=[["year"]], dask="allowed", vectorize=True)
    slp.to_netcdf(outputNcFile)
    print("Output:", slp)
    print("output  min:", slp.thetao.min())
    print("output max:", slp.thetao.max())
    return slp