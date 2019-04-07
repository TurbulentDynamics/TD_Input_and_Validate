#!/usr/bin/env python3

import argparse

import json
# import fastjsonschema

import jsonschema


filepath = "input_lb_halo_schema.json"



parser = argparse.ArgumentParser(description='Arguments for TD_LB_Halo_3dmpi')

parser.add_argument('json_path', type=str)
parser.add_argument('schema_path', type=str)
args = parser.parse_args()


with open(args.schema_path) as f:  
    schema = json.load(f)
print("Schema: " + str(schema))

with open(args.json_path) as f:  
    unval_data = json.load(f)
print("\nUnValidated JSON: " + str(unval_data))


# validate = fastjsonschema.compile(schema)
# validated_json = validate(unval_data)
# print("\n\nValidated JSON: " + str(validated_json))

# with open("Validated_" + args.json_path, 'w') as outfile:
#     json.dump(validated_json, outfile)


jsonschema.validate(unval_data, schema=schema)






