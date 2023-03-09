# WEkEO_NotebookCompetition
## GORNER GLACIER STUDY

### Data used (example - you can change this to suit your data sets)

| Product Description | Product Navigator | WEkEO HDA ID | WEkEO metadata |
|:--------------------:|:-------------:|:-----------------:|:-----------------:|
| Copernicus High Resolution Snow and Ice Monitoring: Persistent Snow Area | <a href="https://land.copernicus.eu/pan-european/biophysical-parameters/high-resolution-snow-and-ice-monitoring/snow-products/persistent-snow-area" target="_blank">link</a> | EO:CRYO:DAT:HRSI:PSA | <a href="https://www.wekeo.eu/data?view=dataset&dataset=EO%3ACRYO%3ADAT%3AHRSI%3APSA" target="_blank">link</a> |

### Learning outcomes

At the end of this notebook you will know:
* How the Persistent Snow Area (PSA) product is derived from Sentinel-2 data and what are its characteristic.
* How to retrieve PSA data from the WEkEO DIAS service.
* How to extract useful data in the region of interest and visualize changes it.
* How to analyse PSA and create a qualitative & quantitative assessment of PSA change.

### Introduction

Glaciers around the world have lost well over 9000 gigatonnes (nine trillion tonnes) of ice since 1961, raising sea level by 27 mm **[1]**.

The Swiss Gorner glacier, one of the biggest ice masses in the Alps on the west side of the monte Rosa, is intensively monitored because of the very evident accelerated ice loss caused by climate change. During the summer of 2021, an international scientific expedition was organized to better study the Gorner glacier in preparation for the COP26 conference (Glasgow, 2021). The expedition was joined by ESA Astronaut Luca Parmitano along with Susanne Mecklenburg, Head of ESA’s Climate Office **[2]** which contributed to bring back the pubblic attention on this issue.

*Figure 1* shows an analysis extrapolated from historical data on the area covered by the glacier in 1850 and 1973, compared with the more recent situation in 2010 and the Copernicus satelllite image from 2020. Below, *Figure 2* shows a stunning visual comparison of the glaciar extension between an historical image from 1926 and a picture taken in 2021 **[3]**.

<figure>
<img align="left" src=https://www.esa.int/var/esa/storage/images/esa_multimedia/images/2021/08/historic_outline_of_the_gorner_glacier_and_surrounding_area/23434550-2-eng-GB/Historic_outline_of_the_Gorner_Glacier_and_surrounding_area.jpg width="100%">
<figcaption align = "center"><b>Fig. 1. Credit: Copernicus Sentinel data (2020) and Historical glacier data from Glacier Monitoring in Switzerland (GLAMOS).</b></figcaption>
</figure>
<figure>
<img align="left" src=https://onthetrailoftheglaciers.com/wp-content/uploads/2019/03/S002047711_13-001-1.jpg width="1000">
<figcaption align = "center"><b>Fig. 2. Historical comparison of the Gorner glacier, 1926 (left) to 2021 (right) Credit: https://onthetrailoftheglaciers.com/.
</b></figcaption>
</figure>

### Project description

This notebook will present an application to retrieve glacier outline and calculate glacier's areas using the **Persistent Snow Area (PSA)** annual product derived from Sentinel-2 data **[4]** and distributed by the WEkEO DIAS service **[5]**. Data are produced from an aggregation of all the Fractional Snow Cover (FSC) maps, where pixels are classified as persistent snow area when snow is observed in at least for 95% of the observations (under clear sky conditions).

Thanks to the PSA satellite product, it is possible to study the surfece loss of snow area of the Gorner glacier over the last year, giving updated information on the status of the glacier.


### References

**[1]** Zemp, M., Huss, M., Thibert, E. et al. Global glacier mass changes and their contributions to sea-level rise from 1961 to 2016. Nature 568, 382–386 (2019).

**[2]** https://www.esa.int/Applications/Observing_the_Earth/Space_for_our_climate/ESA_astronaut_joins_glacier_expedition_in_Alps

**[3]** https://onthetrailoftheglaciers.com/

**[4]** https://land.copernicus.eu/pan-european/biophysical-parameters/high-resolution-snow-and-ice-monitoring/snow-products/persistent-snow-area

**[5]** https://www.wekeo.eu/data

