"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_target_parameter_name
    import aws_sdk_fis.types.experiment_template_target_parameter_value

ExperimentTemplateTargetParameterMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_template_target_parameter_name.ExperimentTemplateTargetParameterName",
    "aws_sdk_fis.types.experiment_template_target_parameter_value.ExperimentTemplateTargetParameterValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentTemplateTargetParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExperimentTemplateTargetParameterMap:
    out: ExperimentTemplateTargetParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
