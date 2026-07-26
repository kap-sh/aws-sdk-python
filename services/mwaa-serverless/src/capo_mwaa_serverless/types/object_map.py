"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#ObjectMap``."""

from typing import TypeAlias

ObjectMap: TypeAlias = dict["str", "object"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: ObjectMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> ObjectMap:
    out: ObjectMap = {}
    for key, value in data.items():
        out[key] = value
    return out
