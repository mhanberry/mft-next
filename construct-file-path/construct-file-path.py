import sys

# returns a relative path to a current pipeline run's output file
def construct_file_path(
    run_id : str, # unique identifier for the current pipeline step
    input_file : str, # relative path to a file
    next_step : str or None = None # the name of the next pipeline step
) -> str:

    core_path = '/'.join(input_file.split('/')[2:]) # path w/o state and run id
    new_state = 'processing' if next_step != None else 'processed'
    
    return f'{new_state}/{run_id}/{core_path}'

if __name__ == '__main__':

    # check for correct usage
    if not (2 < len(sys.argv) < 5):
        print(f'usage: {sys.argv[0]} run_id input_file [next_step]')
        exit()

    path = construct_file_path(*sys.argv[1:])
    print(path)
