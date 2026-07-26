"""Generated from Smithy shape ``com.amazonaws.quicksight#AggFunctionParamMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.agg_function_param_key
    import capo_quicksight.types.agg_function_param_value

AggFunctionParamMap: TypeAlias = dict[
    "capo_quicksight.types.agg_function_param_key.AggFunctionParamKey",
    "capo_quicksight.types.agg_function_param_value.AggFunctionParamValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: AggFunctionParamMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> AggFunctionParamMap:
    out: AggFunctionParamMap = {}
    for key, value in data.items():
        out[key] = value
    return out
