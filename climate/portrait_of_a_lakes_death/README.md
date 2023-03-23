[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/h4ck1ng-science/portrait_of_a_lakes_death/HEAD)

# Portait of a lake's death. 

A geospatial analysis project. 

Colas Droin (EPFL), Diana Zambelloni (EPFL), and Carlos Vivar Rios (h4ck1ng.science)

## Abstract

In recent years, climate change has brought increasingly substantial effects on the land, including drought, which affects many countries worldwide in different ways, leading to catastrophic consequences for our ecosystem, including economic and social environmental disasters. Bodies of water represent one of the essential resources for life on the planet, which is why their disappearance should be of great concern to us. There have been many disappearing lakes recently, such as Chad Lake in Nigeria, Poopo Lake in Bolivia, Urma Lake in Iran, Jelenino in Poland, and many others. These include the complicated case of Acuelo Lagoon, an essential resource for the metropolitan city of Santiago de Chile, which unfortunately dried up entirely in May 2018.

In this project, we used remote sensing products delivered by the Sentinel-2 missions to assess the state of the lake from 2017 to 2022. After downloading all the data available in that period, we cropped the area of interest of the lake. Then we selected the images with enough quality to allow the segmentation and measurement of the total lake area in each image. This segmentation revealed a sharp drop in the entire lake's extension, leading to the absolute death of the lake around 2020. Finally, we performed an additional analysis of the lake's algae content to serve as a bioindicator of the water's quality. 

Public repositories of remote sensing products such as the ones provided by the Sentinel missions offer an excellent opportunity to monitor the impact of climate change on our environment. For Aculeo's lake could be too late, but real-time monitoring analysis of wetlands using satellite imagery can be used to predict critical situations that require urgent action by society. This technology can potentially become the tool that makes the difference between losing or saving our planet as we know it.

## How to run this article

This article is designed to be run in **Wekeo Jupyter Hub**. You can copy this repository and run the notebook titled `Portrait_of_a_lakes_death.ipynb`. There you will need to install some dependencies with `pip` before running the rest of the article. 

It is possible to run this notebook in **Binder**, however the RAM available is not enough to process all the images required for the analysis. 

## License

Copyright (c) 2022 Carlos Vivar Rios, Colas Droin, and Diana Zambelloni.

Permission is hereby granted, free of charge, to any person obtaininga copy of this software and associated documentation files (the"Software"), to deal in the Software without restriction, includingwithout limitation the rights to use, copy, modify, merge, publish,distribute, sublicense, and/or sell copies of the Software, and topermit persons to whom the Software is furnished to do so, subject tothe following conditions:

The above copyright notice and this permission notice shall beincluded in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OFMERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE ANDNONINFRINGEMENT.IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BELIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTIONOF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.