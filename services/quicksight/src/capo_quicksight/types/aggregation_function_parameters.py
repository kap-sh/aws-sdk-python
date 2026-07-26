"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationFunctionParameters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.limited_string

AggregationFunctionParameters: TypeAlias = dict[
    "capo_quicksight.types.limited_string.LimitedString",
    "capo_quicksight.types.limited_string.LimitedString",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AggregationFunctionParameters) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AggregationFunctionParameters:
    out: AggregationFunctionParameters = {}
    for key, value in data.items():
        out[key] = value
    return out
