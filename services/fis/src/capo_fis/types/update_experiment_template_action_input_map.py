"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateActionInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_action_name
    import capo_fis.types.update_experiment_template_action_input_item

UpdateExperimentTemplateActionInputMap: TypeAlias = dict[
    "capo_fis.types.experiment_template_action_name.ExperimentTemplateActionName",
    "capo_fis.types.update_experiment_template_action_input_item.UpdateExperimentTemplateActionInputItem",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UpdateExperimentTemplateActionInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fis.types.update_experiment_template_action_input_item

        out[key] = (
            capo_fis.types.update_experiment_template_action_input_item.serialize_json(
                value
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateActionInputMap:
    out: UpdateExperimentTemplateActionInputMap = {}
    for key, value in data.items():
        import capo_fis.types.update_experiment_template_action_input_item

        out[key] = (
            capo_fis.types.update_experiment_template_action_input_item.deserialize_json(
                value
            )
        )
    return out
