"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateActionInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_fis.types.experiment_template_action_name
    import aws_sdk_fis.types.update_experiment_template_action_input_item

UpdateExperimentTemplateActionInputMap: TypeAlias = dict[
    "aws_sdk_fis.types.experiment_template_action_name.ExperimentTemplateActionName",
    "aws_sdk_fis.types.update_experiment_template_action_input_item.UpdateExperimentTemplateActionInputItem",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UpdateExperimentTemplateActionInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import aws_sdk_fis.types.update_experiment_template_action_input_item

        out[key] = (
            aws_sdk_fis.types.update_experiment_template_action_input_item.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateActionInputMap:
    out: UpdateExperimentTemplateActionInputMap = {}
    for key, value in data.items():
        import aws_sdk_fis.types.update_experiment_template_action_input_item

        out[key] = (
            aws_sdk_fis.types.update_experiment_template_action_input_item.deserialize_json(
                value
            )
        )
    return out
