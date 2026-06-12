"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#Context``."""

from typing import TypeAlias

Context: TypeAlias = dict["str", "str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: Context) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> Context:
    out: Context = {}
    for key, value in data.items():
        out[key] = value
    return out
