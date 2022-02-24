import os
import glob
import zipfile
import pandas as pd
import math
from shutil import copyfile
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

root = tk.Tk()
root.withdraw()
xls = filedialog.askopenfilename(
  title='Identify Participant Data Log:',
  multiple=False,
  initialdir=str(Path.home())+'/Downloads',
  filetypes=[('Excel files','.xlsx','.xls')]
)
df = pd.read_excel(xls,sheet_name="Data Log",header=0)

ziparchs = filedialog.askopenfilename(
  title='Identify Session Zip file(s):',
  multiple=True,
  filetypes=[('Zip files','.zip')]
)

ses_dict = {
  '1': 'S1',
  '2': 'S2',
  '3': 'S3', # this is occasionally labeled 'M1', need to rename to S3 on Box
  '4': 'S4'  # this is occasionally labeled 'M4', need to rename to S4 on Box
};

donezips = []
tmpdir = './tmpdir'
if not os.path.isdir(tmpdir):
  os.makedirs(tmpdir)
for ii in range(0,len(df)):
  try:
    cursub = str(int(df.subject[ii])).zfill(3)
    curses = str(int(df.session[ii]))
  except:
    pass

  ziparch = None
  for arch in ziparchs:
    zipdir, zipfilename = os.path.split(arch)
    ses_ext = ses_dict[curses]
    ses_file = cursub+'_'+str(df.npu_order[ii])+'_'+ses_ext+'.zip'
    if ses_file==zipfilename:
      ziparch = arch
      donezips = donezips+[arch]

  if ziparch:
    print('Unpacking '+ziparch+' matched to participant data log entry from '+str(df.loc[ii,'date']).split(' ')[0])

  if ziparch:
    #copyfile(glob.glob(zipdir+'/'+str(df.subject[ii])+'*.zip')[0], tmpdir+'/tmp.zip')
    copyfile( ziparch, tmpdir+'/tmp.zip' )
    zipfile.ZipFile(tmpdir + '/tmp.zip').extractall(tmpdir+'/')

    #resting-state (pre)
    if not math.isnan(df.run_rest_pre[ii]):
      curdat = glob.glob( tmpdir+'/'+ziparch.split('/')[-1].split('.zip')[0]+'/'+str(df.file_prefix[ii])+'*'+str(int(df.run_rest_pre[ii]))+'.cdt*' )
      if len(curdat)==3:
        froot = curdat[0].split('.cdt')[0]
        file1 = glob.glob(froot + '*cdt')[0]
        file2 = glob.glob(froot + '*dpa')[0]
        file3 = glob.glob(froot + '*ceo')[0]
        copyfile(file1,'/labs/ankerlab/data/k01/rest.pre/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'restpre'+'_acq-'+'A1'+'_run-1.cdt')
        copyfile(file2,'/labs/ankerlab/data/k01/rest.pre/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'restpre'+'_acq-'+'A1'+'_run-1.cdt.dpa')
        copyfile(file3,'/labs/ankerlab/data/k01/rest.pre/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'restpre'+'_acq-'+'A1'+'_run-1.cdt.ceo')
      else:
        print('unpack_k01.py; unable to process **rest.pre**, not 3 cdt files or files are named incorrectly...')
           
    #resting-state (post)
    if not math.isnan(df.run_rest_post[ii]):
      curdat = glob.glob(tmpdir+'/'+ziparch.split('/')[-1].split('.zip')[0]+'/'+str(df.file_prefix[ii])+'*'+str(int(df.run_rest_post[ii]))+'.cdt*')
      if len(curdat)==3:
        froot = curdat[0].split('.cdt')[0]
        file1 = glob.glob(froot + '*cdt')[0]
        file2 = glob.glob(froot + '*dpa')[0]
        file3 = glob.glob(froot + '*ceo')[0]
        copyfile(file1,'/labs/ankerlab/data/k01/rest.post/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'restpost'+'_acq-'+'A1'+'_run-1.cdt')
        copyfile(file2,'/labs/ankerlab/data/k01/rest.post/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'restpost'+'_acq-'+'A1'+'_run-1.cdt.dpa')
        copyfile(file3,'/labs/ankerlab/data/k01/rest.post/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'restpost'+'_acq-'+'A1'+'_run-1.cdt.ceo')
      else:
        print('unpack_k01.py; unable to process **rest.post**, not 3 cdt files or files are named incorrectly...')

    #npu (block 1, [+block 2])
    if not math.isnan(df.run_npu[ii]):
      curdat = glob.glob(tmpdir+'/'+ziparch.split('/')[-1].split('.zip')[0]+'/'+str(df.file_prefix[ii])+'*'+str(int(df.run_npu[ii]))+'.cdt*')
      if len(curdat)==3:
        froot = curdat[0].split('.cdt')[0]
        file1 = glob.glob(froot + '*cdt')[0]
        file2 = glob.glob(froot + '*dpa')[0]
        file3 = glob.glob(froot + '*ceo')[0]
        npuacq= df.npu_order[ii]+str(int(df.npu_version[ii]))
        copyfile(file1,'/labs/ankerlab/data/k01/npu/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'npu'+'_acq-'+npuacq+'_run-1.cdt')
        copyfile(file2,'/labs/ankerlab/data/k01/npu/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'npu'+'_acq-'+npuacq+'_run-1.cdt.dpa')
        copyfile(file3,'/labs/ankerlab/data/k01/npu/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'npu'+'_acq-'+npuacq+'_run-1.cdt.ceo')
      else:
        print('unpack_k01.py; unable to process **npu**, not 3 cdt files or files named incorrectly...')

    #npu (block 2, optional)
    if not math.isnan(df.run_npu_optional2nd[ii]):
      curdat = glob.glob(tmpdir+'/'+ziparch.split('/')[-1].split('.zip')[0]+'/'+str(df.file_prefix[ii])+'*'+str(int(df.run_npu_optional2nd[ii]))+'.cdt*')
      if len(curdat)==3:
        froot = curdat[0].split('.cdt')[0]
        file1 = glob.glob(froot + '*cdt')[0]
        file2 = glob.glob(froot + '*dpa')[0]
        file3 = glob.glob(froot + '*ceo')[0]
        npuacq= df.npu_order[ii]+str(int(df.npu_version[ii]))
        copyfile(file1,'/labs/ankerlab/data/k01/npu/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'npu'+'_acq-'+npuacq+'_run-2.cdt')
        copyfile(file2,'/labs/ankerlab/data/k01/npu/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'npu'+'_acq-'+npuacq+'_run-2.cdt.dpa')
        copyfile(file3,'/labs/ankerlab/data/k01/npu/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'npu'+'_acq-'+npuacq+'_run-2.cdt.ceo')
      else:
        print('unpack_k01.py; unable to process **npu (2nd optional file)**, not 3 cdt files or files named incorrectly...')

    #startle workup
    if not math.isnan(df.run_startle_workup[ii]):
      curdat = glob.glob(tmpdir+'/'+ziparch.split('/')[-1].split('.zip')[0]+'/'+str(df.file_prefix[ii])+'*'+str(int(df.run_startle_workup[ii]))+'.cdt*')
      if len(curdat)==3:
        froot = curdat[0].split('.cdt')[0]
        file1 = glob.glob(froot + '*cdt')[0]
        file2 = glob.glob(froot + '*dpa')[0]
        file3 = glob.glob(froot + '*ceo')[0]
        npuacq= df.npu_order[ii]+str(int(df.npu_version[ii]))
        copyfile(file1,'/labs/ankerlab/data/k01/startle.workup/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'startle'+'_acq-'+'A1'+'_run-1.cdt')
        copyfile(file2,'/labs/ankerlab/data/k01/startle.workup/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'startle'+'_acq-'+'A1'+'_run-1.cdt.dpa')
        copyfile(file3,'/labs/ankerlab/data/k01/startle.workup/'+'sub-'+cursub+'_ses-'+curses+'_task-'+'startle'+'_acq-'+'A1'+'_run-1.cdt.ceo')
      else:
        print('unpack_k01.py; unable to process **startle.workup**, not 3 cdt files or files named incorrectly...')
    
    #delete the tmpdir contents
    cursubdir = tmpdir+'/'+ziparch.split('/')[-1].split('.zip')[0]
    if os.path.isdir(cursubdir):
       shutil.rmtree(cursubdir)
    if os.path.isfile(tmpdir + '/tmp.zip'):
       os.remove(tmpdir + '/tmp.zip')

print('Completed: the following Zips were processed: ')
print(donezips)
print('Warning: the following Zips were ignored (hint: check how the zipfile is named and how it is labeled in the Participants Data Log): ')
print(list(set(list(ziparchs)) - set(donezips)))

