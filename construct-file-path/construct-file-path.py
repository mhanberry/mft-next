import sys

# check for correct usage
if not (2 < len(sys.argv) < 5):
    print(f'usage: {sys.argv[0]} run_id input_file [next_step]')
    exit()
    
run_id = sys.argv[1] # unique identifier for the current pipeline step
input_file = sys.argv[2] # path to a file, excluding bucket address
next_step = sys.argv[3] if len(sys.argv) == 4 else None # name of the next step

core_path = '/'.join(input_file.split('/')[2:]) # path w/o state and run id
new_state = 'processing' if next_step != None else 'processed'

print(f'{new_state}/{run_id}/{core_path}')
