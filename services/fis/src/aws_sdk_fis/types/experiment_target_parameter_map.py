"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTargetParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_target_parameter_name
    import aws_sdk_fis.types.experiment_target_parameter_value

ExperimentTargetParameterMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_target_parameter_name.ExperimentTargetParameterName",
    "aws_sdk_fis.types.experiment_target_parameter_value.ExperimentTargetParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentTargetParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExperimentTargetParameterMap:
    out: ExperimentTargetParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
