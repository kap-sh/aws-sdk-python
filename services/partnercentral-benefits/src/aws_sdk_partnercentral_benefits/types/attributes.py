"""Generated from Smithy shape ``com.amazonaws.partnercentralbenefits#Attributes``."""

from typing import TypeAlias

Attributes: TypeAlias = dict["str", "str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: Attributes) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> Attributes:
    out: Attributes = {}
    for key, value in data.items():
        out[key] = value
    return out
