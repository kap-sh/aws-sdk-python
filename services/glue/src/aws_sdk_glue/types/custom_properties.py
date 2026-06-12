"""Generated from Smithy shape ``com.amazonaws.glue#CustomProperties``."""

from typing import TypeAlias

CustomProperties: TypeAlias = dict["str", "str"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: CustomProperties) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomProperties:
    out: CustomProperties = {}
    for key, value in data.items():
        out[key] = value
    return out
