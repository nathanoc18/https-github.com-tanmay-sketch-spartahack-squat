#Importing the libraries
import av
import os
import sys
import streamlit as st
import cv2
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.join(__file__, '../../')))
sys.path.append(BASE_DIR)

from utils import get_media_pipe_pose
from process_frame import ProcessFrame
from thresholds import get_thresholds_beginner, get_thresholds_pro

st.title("Squat Analysis")

mode = st.radio('Select Radio',['Beginner','Pro'], horizontal=True)

thresholds = None

if mode == 'Beginner': 
    thresholds = get_thresholds_beginner()

elif mode == 'Pro':
    thresholds = get_thresholds_pro()
