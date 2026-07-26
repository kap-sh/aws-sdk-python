"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#StringMap``."""

from typing import TypeAlias

StringMap: TypeAlias = dict["str", "str"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(input_to_serialize: StringMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_0(data: dict) -> StringMap:
    out: StringMap = {}
    for key, value in data.items():
        out[key] = value
    return out
