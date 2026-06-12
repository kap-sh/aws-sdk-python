"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateActionInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.create_experiment_template_action_input
    import aws_sdk_fis.types.experiment_template_action_name

CreateExperimentTemplateActionInputMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_template_action_name.ExperimentTemplateActionName",
    "aws_sdk_fis.types.create_experiment_template_action_input.CreateExperimentTemplateActionInput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CreateExperimentTemplateActionInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fis.types.create_experiment_template_action_input

        out[key] = (
            aws_sdk_fis.types.create_experiment_template_action_input.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateActionInputMap:
    out: CreateExperimentTemplateActionInputMap = {}
    for key, value in data.items():
        import aws_sdk_fis.types.create_experiment_template_action_input

        out[key] = (
            aws_sdk_fis.types.create_experiment_template_action_input.deserialize_json(
                value
            )
        )
    return out
