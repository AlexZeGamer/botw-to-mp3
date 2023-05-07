import os

from utils import select_folder, select_file
from convert import convert_bfstm_to_mp3, convert_folder, SUPPORTED_FORMATS


if __name__ == "__main__":
    ### Select input and output folders/files
    
    # input_file_path = select_file(
    #     title = f"Select a file ({', '.join(SUPPORTED_FORMATS)}) to convert to MP3",
    #     initialdir = os.path.join(os.path.dirname(__file__), "input"),
    #     filetypes = [
    #         ("Supported formats", f"{' '.join([f'*.{f}' for f in SUPPORTED_FORMATS])}"),
    #         ("All files", "*.*"),
    #     ],
    # )

    input_dir_path = select_folder(
        title="Select an input folder",
    )

    output_dir_path = select_folder(
        title = "Select an output folder",
        initialdir = os.path.dirname(input_dir_path),
    )

    # input_dir_path = r"C:\ProgramData\cemu_1.26.2\games\The Legend of Zelda Breath of the Wild [ALZP01]"
    # output_dir_path = r"C:\ProgramData\cemu_1.26.2\tools\botw-to-mp3\output"


    ### Convert BFSTM files to MP3 files
    convert_folder(input_dir_path, output_dir_path)
    # convert_bfstm_to_mp3(input_file_path, output_dir_path)
