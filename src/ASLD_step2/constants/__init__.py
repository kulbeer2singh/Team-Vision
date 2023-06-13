"""
author:@ kumar dahal
date: june 6 2023
"""
import os
from datetime import datetime
from pathlib import Path

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"



CONFIG_FILE_PATH = Path("configs/config.yaml")