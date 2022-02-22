# unpack_k01

For detailed instructions on how to use this script, please [request access to this Google Doc](https://docs.google.com/document/d/1I0cIUKkvH8K5GQ4wWuXPmANDKxs_DCkQIo48Eggvzvc/edit?usp=sharing)

## Setup
* Need to have Conda installed, e.g., 
```
cd ~/Downloads
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
* Once Conda is installed, create the conda environment, which contains all the Python packages needed to run the script
```
conda env create
conda activate unpack_k01
```

## Unpacking data files
1. Next, run the "unpacking" script to take the Zip files you downloaded and sort them into their respective directories. 
```
python unpack_k01.py
```
2. This will pop-up two sequential dialog boxes, the first dialog box will ask you to point the program towards the "Participant Data Log.xlsx" that you downloaded from Box. E.g., you may have to navigate to `/home/<your_x500>/Downloads/Participant Data Log.xlsx`.
3. When the second dialog box pops up, you should select the `.zip` file(s) you downloaded from Box. Selecting multiple zip files is fine. 

## Notes:
- Not my best work, a bit of a kludge, etc. etc. etc.
