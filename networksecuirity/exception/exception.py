import os
from networksecuirity.logging.logger import logging
import sys

logging.info("NetworkSecurityException NetworkSecurityException module loaded successfully")
class NetworkSecurityException(Exception):
    def __init__(self,err_msg,error_details:sys):
        self.err_msg = err_msg
        _,_,exc_tb = error_details.exc_info()

        self.line_number = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return f"Error occurred in script: {self.file_name} at line number: {self.line_number} with error message: {self.err_msg}"

