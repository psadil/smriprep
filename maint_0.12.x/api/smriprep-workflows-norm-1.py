from smriprep.workflows.norm import init_anat_norm_wf
wf = init_anat_norm_wf(
    sloppy=False,
    omp_nthreads=1,
    templates=['MNI152NLin2009cAsym', 'MNI152NLin6Asym'],
)