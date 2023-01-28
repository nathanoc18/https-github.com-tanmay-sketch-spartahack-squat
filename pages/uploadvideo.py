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