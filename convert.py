import os, subprocess

try:
    from progress.bar import ShadyBar
except ImportError:
    has_progress_bar = False
else:
    has_progress_bar = True

VGMSTREAM_PATH = os.path.join(os.path.dirname(__file__), "vgmstream", "vgmstream.exe")
SUPPORTED_FORMATS = ["bfstm", "bfstp", "bfwav"]

def convert_bfstm_to_mp3(input_file_path, output_dir_path, stereo_channels=0, verbose=True):
    input_file_parent_dir_path : str        = os.path.dirname(input_file_path)
    input_file_name_with_extension : str    = os.path.basename(input_file_path)
    input_file_name_without_extension : str = os.path.splitext(input_file_name_with_extension)[0]
    input_file_extension : str              = os.path.splitext(input_file_name_with_extension)[1].lower().replace('.', '')

    ### Error handling (in red)
    if input_file_extension not in SUPPORTED_FORMATS:
        raise ValueError( "\033[91m"
            + f"{input_file_name_with_extension} isn't in a supported file format ({input_file_extension})"
            + "\nSupported formats are : " + ", ".join(SUPPORTED_FORMATS)
            + "\033[0m"
        )
    if not os.path.exists(input_file_path): raise FileNotFoundError( "\033[91m" +  f"The file \"{input_file_path}\" doesn't exist."    + "\033[0m" )
    if not os.path.exists(output_dir_path): raise FileNotFoundError( "\033[91m" +  f"The folder \"{output_dir_path}\" doesn't exist."  + "\033[0m" )
    if not os.path.isfile(input_file_path): raise FileNotFoundError( "\033[91m" +  f"\"{input_file_path}\" isn't a file."              + "\033[0m" )
    if not os.path.isdir(output_dir_path):  raise FileNotFoundError( "\033[91m" +  f"\"{output_dir_path}\" isn't a folder."            + "\033[0m" )

    ### BFSTM -> MP3
    print(f"Converting {input_file_name_with_extension} to MP3...") if verbose else None
    output_file_name_with_extension = f"{input_file_name_without_extension}.mp3"
    output_file_path = os.path.join(output_dir_path, output_file_name_with_extension)

    # Run VGMSTREAM
    cmd = [
        VGMSTREAM_PATH,             # Path to VGMSTREAM executable
        "-2", str(stereo_channels), # Stereo channels
        input_file_path,            # Input file
        "-o", output_file_path      # Output file
    ]

    result = subprocess.run(
        cmd,
        stdout=subprocess.DEVNULL,  # Hide output
        stderr=subprocess.PIPE,     # Capture errors
    )

    if result.returncode != 0:
        print("\033[91m" + "An error occured while converting the file :\n" + result.stderr.decode() + "\033[0m")
    else:
        print(f"{input_file_name_with_extension} converted to MP3 as {output_file_name_with_extension}") if verbose else None


def convert_folder(input_dir_path, output_dir, stereo_channels=0):
    total_files = sum([len(files) for _, _, files in os.walk(input_dir_path)])
    bar = ShadyBar(max=total_files, suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds') if has_progress_bar else None

    for root, _, files in os.walk(input_dir_path):
        
        for current_file in files:
            current_file_path_absolute = os.path.join(root, current_file)
            current_file_path_relative = os.path.relpath(current_file_path_absolute, input_dir_path)
            root_relative = os.path.relpath(root, input_dir_path)

            # print(current_file_path_relative)
            bar.next() if bar else None

            file_extension : str = os.path.splitext(current_file)[1]
            if file_extension.lower().replace('.', '') in SUPPORTED_FORMATS:
                os.makedirs(os.path.join(output_dir, root_relative), exist_ok=True)

                output_file_dir_path = os.path.join(output_dir, root_relative)
                convert_bfstm_to_mp3(current_file_path_absolute, output_file_dir_path, verbose=False)
                # print(f"{current_file_path_absolute} converted to MP3")
    bar.finish() if bar else None
