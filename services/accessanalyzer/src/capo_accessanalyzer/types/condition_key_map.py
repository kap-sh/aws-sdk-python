"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#ConditionKeyMap``."""

from typing import TypeAlias

ConditionKeyMap: TypeAlias = dict["str", "str"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ConditionKeyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ConditionKeyMap:
    out: ConditionKeyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
