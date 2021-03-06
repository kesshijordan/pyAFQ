
AFQ: Automated Fiber Quantification
====================================

**pyAFQ is pre-release software. For the time-being, we recomend that you use the** `Matlab version of AFQ <https://github.com/yeatmanlab/AFQ>`_.

Tractography based on diffusion weighted MRI (dMRI) is used to find  the major
white matter fascicles (tracts) in the living human brain. The health of these
tracts is an important factor underlying many cognitive and neurological
disorders.

`AFQ` is a sofware package focused on automated delineation of the major fiber
tracts in individual human brains, and quantification of the tissue properties
within the tracts.

Tissue properties may vary systematically along each tract: different
populations of axons enter and exit the tract, and disease can strike at local
positions within the tract. Because of this, quantifying and understanding
diffusion measures along each fiber tract (the tract profile) may reveal new
insights into white matter development, function, and disease that are not
obvious from mean measures of that tract (Yeatman2012_).

.. [Yeatman2012] Jason D Yeatman, Robert F Dougherty, Nathaniel J Myall, Brian A Wandell, Heidi M Feldman, "Tract profiles of white matter properties: automating fiber-tract quantification", PloS One, 7: e49790

    .. toctree::
       :maxdepth: 2

       installation_guide
       auto_examples/index
       reference/index


.. figure:: _static/eScience_Logo_HR.png
   :align: center
   :figclass: align-center
   :target: http://escience.washington.edu

   Acknowledgements: this work was supported by a grant from the
   `Gordon & Betty Moore Foundation <https://www.moore.org/>`_,  and from the
   `Alfred P. Sloan Foundation <http://www.sloan.org/>`_ to the
   `University of Washington eScience Institute <http://escience.washington.edu/>`_.
