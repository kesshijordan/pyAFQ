import os
import os.path as op
import json

import boto3
import botocore

import numpy as np

import nibabel as nib
import dipy.data as dpd
from dipy.data.fetcher import _make_fetcher

from AFQ.utils.streamlines import read_trk

__all__ = ["fetch_callosum_templates", "read_callosum_templates",
           "fetch_templates", "read_templates", "fetch_hcp",
           "fetch_stanford_hardi_tractography",
           "read_stanford_hardi_tractography",
           "organize_stanford_data"]

afq_home = op.join(op.expanduser('~'), 'AFQ_data')

baseurl = "https://ndownloader.figshare.com/files/"

callosum_fnames = ["Callosum_midsag.nii.gz",
                   "L_AntFrontal.nii.gz",
                   "L_Motor.nii.gz",
                   "L_Occipital.nii.gz",
                   "L_Orbital.nii.gz",
                   "L_PostParietal.nii.gz",
                   "L_SupFrontal.nii.gz",
                   "L_SupParietal.nii.gz",
                   "L_Temporal.nii.gz",
                   "R_AntFrontal.nii.gz",
                   "R_Motor.nii.gz",
                   "R_Occipital.nii.gz",
                   "R_Orbital.nii.gz",
                   "R_PostParietal.nii.gz",
                   "R_SupFrontal.nii.gz",
                   "R_SupParietal.nii.gz",
                   "R_Temporal.nii.gz"]

callosum_remote_fnames = ["5273794", "5273797", "5273800", "5273803",
                          "5273806", "5273809", "5273812", "5273815",
                          "5273821", "5273818", "5273824", "5273827",
                          "5273830", "5273833", "5273836", "5273839",
                          "5273842"]

callosum_md5_hashes = ["709fa90baadeacd64f1d62b5049a4125",
                       "987c6169de807c4e93dc2cbd7a25d506",
                       "0da114123d0b0097b96fe450a459550b",
                       "6d845bd10504f67f1dc17f9000076d7e",
                       "e16c7873ef4b08d26b77ef746dab8237",
                       "47193fd4df1ea17367817466de798b90",
                       "7e78bf9671e6945f4b2f5e7c30595a3c",
                       "8adbb947377ff7b484c88d8c0ffc2125",
                       "0fd981a4d0847e0642ff96e84fe44e47",
                       "87c4855efa406d8fb004cffb8259180e",
                       "c7969bcf5f2343fd9ce9c49b336cf14c",
                       "bb4372b88991932150205ffb22aa6cb7",
                       "d198d4e7db18ddc7236cf143ecb8342e",
                       "d0f6edef64b0c710c92e634496085dda",
                       "85eaee44665f244db5adae2e259833f6",
                       "25f24eb22879a05d12bda007c81ea55a",
                       "2664e0b8c2d9c59f13649a89bfcce399"]

fetch_callosum_templates = _make_fetcher("fetch_callosum_templates",
                                         op.join(afq_home,
                                                 'callosum_templates'),
                                         baseurl, callosum_remote_fnames,
                                         callosum_fnames,
                                         md5_list=callosum_md5_hashes,
                                         doc="Download AFQ callosum templates")


def read_callosum_templates():
    """Load AFQ callosum templates from file

    Returns
    -------
    dict with: keys: names of template ROIs and values: nibabel Nifti1Image
    objects from each of the ROI nifti files.
    """
    files, folder = fetch_callosum_templates()
    template_dict = {}
    for f in files:
        template_dict[f.split('.')[0]] = nib.load(op.join(folder, f))
    return template_dict


template_fnames = ["ATR_roi1_L.nii.gz",
                   "ATR_roi1_R.nii.gz",
                   "ATR_roi2_L.nii.gz",
                   "ATR_roi2_R.nii.gz",
                   "ATR_L_prob_map.nii.gz",
                   "ATR_R_prob_map.nii.gz",
                   "CGC_roi1_L.nii.gz",
                   "CGC_roi1_R.nii.gz",
                   "CGC_roi2_L.nii.gz",
                   "CGC_roi2_R.nii.gz",
                   "CGC_L_prob_map.nii.gz",
                   "CGC_R_prob_map.nii.gz",
                   "CST_roi1_L.nii.gz",
                   "CST_roi1_R.nii.gz",
                   "CST_roi2_L.nii.gz",
                   "CST_roi2_R.nii.gz",
                   "CST_L_prob_map.nii.gz",
                   "CST_R_prob_map.nii.gz",
                   "FA_L.nii.gz",
                   "FA_R.nii.gz",
                   "FA_prob_map.nii.gz",
                   "FP_L.nii.gz",
                   "FP_R.nii.gz",
                   "FP_prob_map.nii.gz",
                   "HCC_roi1_L.nii.gz",
                   "HCC_roi1_R.nii.gz",
                   "HCC_roi2_L.nii.gz",
                   "HCC_roi2_R.nii.gz",
                   "HCC_L_prob_map.nii.gz",
                   "HCC_R_prob_map.nii.gz",
                   "IFO_roi1_L.nii.gz",
                   "IFO_roi1_R.nii.gz",
                   "IFO_roi2_L.nii.gz",
                   "IFO_roi2_R.nii.gz",
                   "IFO_L_prob_map.nii.gz",
                   "IFO_R_prob_map.nii.gz",
                   "ILF_roi1_L.nii.gz",
                   "ILF_roi1_R.nii.gz",
                   "ILF_roi2_L.nii.gz",
                   "ILF_roi2_R.nii.gz",
                   "ILF_L_prob_map.nii.gz",
                   "ILF_R_prob_map.nii.gz",
                   "SLF_roi1_L.nii.gz",
                   "SLF_roi1_R.nii.gz",
                   "SLF_roi2_L.nii.gz",
                   "SLF_roi2_R.nii.gz",
                   "SLFt_roi2_L.nii.gz",
                   "SLFt_roi2_R.nii.gz",
                   "SLF_L_prob_map.nii.gz",
                   "SLF_R_prob_map.nii.gz",
                   "UNC_roi1_L.nii.gz",
                   "UNC_roi1_R.nii.gz",
                   "UNC_roi2_L.nii.gz",
                   "UNC_roi2_R.nii.gz",
                   "UNC_L_prob_map.nii.gz",
                   "UNC_R_prob_map.nii.gz",
                   "ARC_L_prob_map.nii.gz",
                   "ARC_R_prob_map.nii.gz"]


template_remote_fnames = ["5273680", "5273683", "5273686", "5273689",
                          "11458274", "11458277",
                          "5273695", "5273692", "5273698", "5273701",
                          "11458268", "11458271",
                          "5273704", "5273707", "5273710", "5273713",
                          "11458262", "11458265",
                          "5273716", "5273719",
                          "11458220",
                          "5273722", "5273725",
                          "11458226",
                          "5273728", "5273731", "5273734", "5273746",
                          "11458259", "11458256",
                          "5273737", "5273740", "5273743", "5273749",
                          "11458250", "11458253",
                          "5273752", "5273755", "5273758", "5273761",
                          "11458244", "11458247",
                          "5273764", "5273767", "5273770", "5273773",
                          "5273776", "5273791",
                          "11458238", "11458241",
                          "5273779", "5273782", "5273785", "5273788",
                          "11458223", "11458229",
                          "11458232", "11458235"]


template_md5_hashes = ["6b7aaed1a2982fd0ea436a223133908b",
                       "fd60d46d4e3cbd906c86e4c9e4fd6e2a",
                       "3aba60b169a35c38640de4ec29d362c8",
                       "12716a5688a1809fbaed1d58d2e68b59",
                       "c5637f471df861d9bbb45604db34770b",
                       "850cc4c04d7241747063fe3cd440b2ce",
                       "8e8973bc7838c8744914d402f52d91ca",
                       "c5fa4e6e685e695c006823b6784d2407",
                       "e1fab77f21d5303ed52285f015e24f0b",
                       "5f89defec3753fd75cd688c7bfb20a36",
                       "a4f3cd65b06fb25f63d5dab7592f00f2",
                       "7e73ab02db30a3ad6bd9e82148c2486e",
                       "f9db3154955a20b67c2dda758800d14c",
                       "73941510c798c1ed1b03e2bd481cd5c7",
                       "660cdc031ee0716d60159c7d933119ea",
                       "660cdc031ee0716d60159c7d933119ea",
                       "fd012bc89f6bed7bd54530195496bac4",
                       "3406906a86e633cc102127cf210a1063",
                       "9040a7953dcbbf131d135c866182d8ef",
                       "a72e17194824fcd838a594a2eb50c72e",
                       "627d7bb2e6d55f8243da815a36d9ff1a",
                       "55adbe9b8279185eedbe342149e1ff90",
                       "5a7412a3cf0fb185eec53d1989df2f7c",
                       "1aa36e83ae7b5555bb19d776ede9c18d",
                       "ba453196ff179b0e31172806e313b52c",
                       "d85c6574526b296935f34bf4f65cd493",
                       "9b81646317f59c7db087f27e2f85679e",
                       "9806e82c250e4604534b96917f87b7e8",
                       "213d3fb1ccd756d878f9b50b765b1c8f",
                       "f1e7e6bc51aa0aa279c54fb3805fb5e3",
                       "0e68a9feaaddcc9b4d667c2f15903368",
                       "d45020a87ee4bb496edd350631d91f6a",
                       "75c2c911826ec4b23159f9bd80e3c039",
                       "55d616ea9e0c646adc1aafa0f5fbe625",
                       "dee83fa6b03cfa5e0f5c965953aa6778",
                       "a13eef7059c98568adfefbab660e434e",
                       "045b7d5c6341997f3f0120c3a4212ad8",
                       "d174b1359ba982b03840436c93b7bbb4",
                       "fff9753f394fc4c73fb2ae40b3b4dde0",
                       "cd278b4dd6ff77481ea9ac16485a5ae2",
                       "7bdf5111265107091c7a2fca9215de30",
                       "7d4a43714504e6e930f922c9bc2a13d5",
                       "af2bcedf47e193686af329b9a8e259da",
                       "9a1122943579d11ba169d3ad87a75625",
                       "627903f7a06627bfd4153dc9245fa390",
                       "1714cd7f989c3435bdd5a2076e6272a0",
                       "1fa2114049707a4e05b53f9d95730375",
                       "b6663067d5ea53c70cb8803948f8adf7",
                       "d3e068997ebc60407bd6e9576e47dede",
                       "27ecfbd1d2f98213e52d73b7d70fe0e7",
                       "fa141bb2d951bec486916acda3652d95",
                       "d391d073e86e28588be9a6d01b2e7a82",
                       "a3e085562e6b8111c7ebc358f9450c8b",
                       "d65c67910807504735e034f7ea92d590",
                       "93cb24a9128db1a6c34a09eaf79fe7f0",
                       "71a7455cb4062dc39b1677c118c7b5a5",
                       "19590c712f1776da1fdba64d4eb7f1f6",
                       "04d5af0feb2c1b5b52a87ccbbf148e4b",
                       "53c277be990d00f7de04f2ea35e74d73"]

fetch_templates = _make_fetcher("fetch_templates",
                                op.join(afq_home, 'templates'),
                                baseurl, template_remote_fnames,
                                template_fnames, md5_list=template_md5_hashes,
                                doc="Download AFQ templates")


def read_templates():
    """Load AFQ templates from file

    Returns
    -------
    dict with: keys: names of template ROIs and values: nibabel Nifti1Image
    objects from each of the ROI nifti files.
    """
    files, folder = fetch_templates()
    template_dict = {}
    for f in files:
        template_dict[f.split('.')[0]] = nib.load(op.join(folder, f))
    return template_dict


def fetch_hcp(subjects):
    """
    Fetch HCP diffusion data and arrange it in a manner that resembles the
    BIDS [1]_ specification.

    Parameters
    ----------
    subjects : list
       Each item is an integer, identifying one of the HCP subjects

    Returns
    -------
    dict with remote and local names of these files.

    Notes
    -----
    To use this function, you need to have a file '~/.aws/credentials', that
    includes a section:

    [hcp]
    AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXX
    AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXX

    The keys are credentials that you can get from HCP (see https://wiki.humanconnectome.org/display/PublicData/How+To+Connect+to+Connectome+Data+via+AWS)  # noqa

    Local filenames are changed to match our expected conventions.

    .. [1] Gorgolewski et al. (2016). The brain imaging data structure,
           a format for organizing and describing outputs of neuroimaging
           experiments. Scientific Data, 3::160044. DOI: 10.1038/sdata.2016.44.
    """
    boto3.setup_default_session(profile_name='hcp')
    s3 = boto3.resource('s3')
    try:
        bucket = s3.Bucket('hcp-openaccess')
        # This will trigger the client error in case this S3 bucket
        # doesn't exist
        list(bucket.objects.all())
    except botocore.exceptions.ClientError:
        bucket = s3.Bucket('hcp-openaccess-temp')

    base_dir = op.join(afq_home, 'HCP', 'derivatives', 'preafq')
    if not os.path.exists(base_dir):
        os.makedirs(base_dir, exist_ok=True)

    data_files = {}
    for subject in subjects:
        # We make a single session folder per subject for this case, because
        # AFQ api expects session structure:
        sub_dir = op.join(base_dir, 'sub-%s' % subject)
        sess_dir = op.join(sub_dir, "sess-01")
        if not os.path.exists(sub_dir):
            os.makedirs(os.path.join(sess_dir, 'dwi'), exist_ok=True)
            os.makedirs(os.path.join(sess_dir, 'anat'), exist_ok=True)
        data_files[op.join(sess_dir, 'dwi', 'sub-%s_dwi.bval' % subject)] =\
            'HCP/%s/T1w/Diffusion/bvals' % subject
        data_files[op.join(sess_dir, 'dwi', 'sub-%s_dwi.bvec' % subject)] =\
            'HCP/%s/T1w/Diffusion/bvecs' % subject
        data_files[op.join(sess_dir, 'dwi', 'sub-%s_dwi.nii.gz' % subject)] =\
            'HCP/%s/T1w/Diffusion/data.nii.gz' % subject
        data_files[op.join(sess_dir, 'anat', 'sub-%s_T1w.nii.gz' % subject)] =\
            'HCP/%s/T1w/T1w_acpc_dc.nii.gz' % subject
        data_files[op.join(sess_dir, 'anat',
                           'sub-%s_aparc+aseg.nii.gz' % subject)] =\
            'HCP/%s/T1w/aparc+aseg.nii.gz' % subject

    for k in data_files.keys():
        if not op.exists(k):
            bucket.download_file(data_files[k], k)
    # Create the BIDS dataset description file text
    dataset_description = {
         "BIDSVersion": "1.0.0",
         "Name": "HCP",
         "Acknowledgements": """Data were provided by the Human Connectome Project, WU-Minn Consortium (Principal Investigators: David Van Essen and Kamil Ugurbil; 1U54MH091657) funded by the 16 NIH Institutes and Centers that support the NIH Blueprint for Neuroscience Research; and by the McDonnell Center for Systems Neuroscience at Washington University.""",  # noqa
         "Subjects": subjects}

    with open(op.join(base_dir, 'dataset_description.json'), 'w') as outfile:
        json.dump(dataset_description, outfile)

    return data_files


stanford_hardi_tractography_remote_fnames = ["5325715", "5325718"]
stanford_hardi_tractography_hashes = ['6f4bdae702031a48d1cd3811e7a42ef9',
                                      'f20854b4f710577c58bd01072cfb4de6']
stanford_hardi_tractography_fnames = ['mapping.nii.gz',
                                      'tractography_subsampled.trk']

fetch_stanford_hardi_tractography = _make_fetcher(
    "fetch_stanford_hardi_tractography",
    op.join(afq_home,
            'stanford_hardi_tractography'),
    baseurl,
    stanford_hardi_tractography_remote_fnames,
    stanford_hardi_tractography_fnames,
    md5_list=stanford_hardi_tractography_hashes,
    doc="""Download Stanford HARDI tractography and mapping. For testing
           purposes""")


def read_stanford_hardi_tractography():
    """

    """
    files, folder = fetch_stanford_hardi_tractography()
    files_dict = {}
    files_dict['mapping.nii.gz'] = nib.load(
        op.join(afq_home,
                'stanford_hardi_tractography',
                'mapping.nii.gz'))
    files_dict['tractography_subsampled.trk'] = read_trk(
        op.join(afq_home,
                'stanford_hardi_tractography',
                'tractography_subsampled.trk'))
    return files_dict


def organize_stanford_data(path=None):
    """
    Create the expected file-system structure for the Stanford HARDI data-set
    """
    dpd.fetch_stanford_hardi()

    if path is None:
        if not op.exists(afq_home):
            os.mkdir(afq_home)
        base_folder = op.join(afq_home, 'stanford_hardi',
                              'derivatives', 'preafq')
    else:
        base_folder = op.join(path, 'stanford_hardi',
                              'derivatives', 'preafq')

    if not op.exists(base_folder):
        anat_folder = op.join(base_folder, 'sub-01', 'sess-01', 'anat')
        os.makedirs(anat_folder, exist_ok=True)
        dwi_folder = op.join(base_folder, 'sub-01', 'sess-01', 'dwi')
        os.makedirs(dwi_folder, exist_ok=True)
        t1_img = dpd.read_stanford_t1()
        nib.save(t1_img, op.join(anat_folder, 'sub-01_sess-01_T1w.nii.gz'))
        seg_img = dpd.read_stanford_labels()[-1]
        nib.save(seg_img, op.join(anat_folder,
                                  'sub-01_sess-01_aparc+aseg.nii.gz'))
        dwi_img, gtab = dpd.read_stanford_hardi()
        nib.save(dwi_img, op.join(dwi_folder, 'sub-01_sess-01_dwi.nii.gz'))
        np.savetxt(op.join(dwi_folder, 'sub-01_sess-01_dwi.bvecs'), gtab.bvecs)
        np.savetxt(op.join(dwi_folder, 'sub-01_sess-01_dwi.bvals'), gtab.bvals)
