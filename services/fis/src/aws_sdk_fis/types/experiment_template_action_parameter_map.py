"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateActionParameterMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_action_parameter
    import aws_sdk_fis.types.experiment_template_action_parameter_name

ExperimentTemplateActionParameterMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_template_action_parameter_name.ExperimentTemplateActionParameterName",
    "aws_sdk_fis.types.experiment_template_action_parameter.ExperimentTemplateActionParameter",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentTemplateActionParameterMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExperimentTemplateActionParameterMap:
    out: ExperimentTemplateActionParameterMap = {}
    for key, value in data.items():
        out[key] = value
    return out
