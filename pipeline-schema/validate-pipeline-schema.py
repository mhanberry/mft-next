import sys, yaml, jsonschema

# Check for valid usage
if len(sys.argv) != 2:
    print(f'usage: {sys.argv[0]} pipeline.yaml')
    exit()

# Load the pipeline
pipeline_file = open(sys.argv[1], 'r')
pipeline = yaml.full_load(pipeline_file)

# Load the schema
schema_file = open('schema.yaml', 'r')
schema = yaml.full_load(schema_file)

# Validate the pipeline
jsonschema.validate(pipeline, schema)

print("The pipeline is valid.")
