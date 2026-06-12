"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_action_parameter
    import aws_sdk_fis.types.experiment_action_parameter_name

ExperimentActionParameterMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_action_parameter_name.ExperimentActionParameterName",
    "aws_sdk_fis.types.experiment_action_parameter.ExperimentActionParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentActionParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExperimentActionParameterMap:
    out: ExperimentActionParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
