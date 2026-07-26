"""Generated from Smithy shape ``com.amazonaws.m2#BatchJobParametersMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_m2.types.batch_param_key
    import capo_m2.types.batch_param_value

BatchJobParametersMap: TypeAlias = dict[
    "capo_m2.types.batch_param_key.BatchParamKey",
    "capo_m2.types.batch_param_value.BatchParamValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: BatchJobParametersMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> BatchJobParametersMap:
    out: BatchJobParametersMap = {}
    for key, value in data.items():
        out[key] = value
    return out
