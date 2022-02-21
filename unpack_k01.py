import os
import glob
import zipfile
import pandas as pd
import math
from shutil import copyfile
import shutil

xls    = '~/Downloads/ankerlab-participant-data-log.xlsx'
zipdir = '/labs/ankerlab/data/k01/zips'
tmpdir = './tmpdir'
df = pd.read_excel(xls,sheet_name="Sheet1",header=0)

if not os.path.isdir(tmpdir):
  os.makedirs(tmpdir)
for ii in range(0,len(df)):
  cursub = str(df.subject[ii]).zfill(3) #str(df.subject[ii])
  curses = str(df.session[ii])
  ziparch= zipdir+'/'+cursub+'_'+str(df.npu_order[ii])+'_S'+curses+'.zip'
  if not os.path.isfile( ziparch ):
    ziparch= zipdir+'/'+cursub+'_'+str(df.npu_order[ii])+'_M1.zip' #kloodge, 2020-01-14
    if not os.path.isfile( ziparch ):
      ziparch= zipdir+'/'+cursub+'_'+str(df.npu_order[ii])+'_M4.zip' #kloodge, 2020-01-14

  if os.path.isfile( ziparch ):
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
        print('unpack_k01.py; unable to process '+curdat[0]+', not 3 cdt files...')
           
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
        print('unpack_k01.py; unable to process '+curdat[0]+', not 3 cdt files...')

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
        print('unpack_k01.py; unable to process '+curdat[0]+', not 3 cdt files...')

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
        print('unpack_k01.py; unable to process '+curdat[0]+', not 3 cdt files...')

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
        print('unpack_k01.py; unable to process '+curdat[0]+', not 3 cdt files...')
    
    #delete the tmpdir contents
    cursubdir = tmpdir+'/'+ziparch.split('/')[-1].split('.zip')[0]
    if os.path.isdir(cursubdir):
       shutil.rmtree(cursubdir)
    if os.path.isfile(tmpdir + '/tmp.zip'):
       os.remove(tmpdir + '/tmp.zip')


  


