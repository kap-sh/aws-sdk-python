"""Generated from Smithy shape ``com.amazonaws.cleanrooms#JobParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanrooms.types.job_parameter_name
    import capo_cleanrooms.types.job_parameter_value

JobParameterMap: TypeAlias = dict[
    "capo_cleanrooms.types.job_parameter_name.JobParameterName",
    "capo_cleanrooms.types.job_parameter_value.JobParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: JobParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> JobParameterMap:
    out: JobParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
