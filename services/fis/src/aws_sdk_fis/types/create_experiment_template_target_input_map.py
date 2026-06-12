"""Generated from Smithy shape ``com.amazonaws.fis#CreateExperimentTemplateTargetInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.create_experiment_template_target_input
    import aws_sdk_fis.types.experiment_template_target_name

CreateExperimentTemplateTargetInputMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_template_target_name.ExperimentTemplateTargetName",
    "aws_sdk_fis.types.create_experiment_template_target_input.CreateExperimentTemplateTargetInput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: CreateExperimentTemplateTargetInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fis.types.create_experiment_template_target_input

        out[key] = (
            aws_sdk_fis.types.create_experiment_template_target_input.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> CreateExperimentTemplateTargetInputMap:
    out: CreateExperimentTemplateTargetInputMap = {}
    for key, value in data.items():
        import aws_sdk_fis.types.create_experiment_template_target_input

        out[key] = (
            aws_sdk_fis.types.create_experiment_template_target_input.deserialize_json(
                value
            )
        )
    return out
