# xpopy
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HeQinWill/xpopy/blob/master/xpopy_demo.ipynb)

## INTRO
This is an unofficial implementation for the paper below. 
The acceleration is mainly owing to the **ufuncs** in [PyGEOS](https://github.com/pygeos/pygeos) and [NumPy](https://github.com/numpy/numpy), 
which tries to avoid iteration to provide a better performance 
(~**10** times the speed over [the official one](https://github.com/Kang-Sun-CfA/Oversampling_matlab/blob/master/popy.py) 
under a two-core test).  
In addition, the geometry operation seems to be more intuitive and easier to understand in the code snippets.  

> Sun, K., Zhu, L., Cady-Pereira, K., Chan Miller, C., Chance, K., Clarisse, L., Coheur, P.-F., González Abad, G., Huang, G., Liu, X., Van Damme, M., Yang, K., and Zondlo, M.: A physics-based approach to oversample multi-satellite, multispecies observations to a common grid, Atmos. Meas. Tech., 11, 6679–6701, https://doi.org/10.5194/amt-11-6679-2018, 2018.


## TODO
- Handle the global grids (longitude bounds: 0~360/±180, overlaps in high-latitude areas)
- Add ellipsoid projection
- More dataset will be ingested by pre-defined YAML files if possible
