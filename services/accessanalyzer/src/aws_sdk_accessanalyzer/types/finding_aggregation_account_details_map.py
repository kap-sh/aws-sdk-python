"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingAggregationAccountDetailsMap``."""

from typing import TypeAlias

FindingAggregationAccountDetailsMap: TypeAlias = dict["str", "int"]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: FindingAggregationAccountDetailsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> FindingAggregationAccountDetailsMap:
    out: FindingAggregationAccountDetailsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
