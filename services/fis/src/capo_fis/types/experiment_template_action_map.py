"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateActionMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_action
    import capo_fis.types.experiment_template_action_name

ExperimentTemplateActionMap: TypeAlias = dict[
    "capo_fis.types.experiment_template_action_name.ExperimentTemplateActionName",
    "capo_fis.types.experiment_template_action.ExperimentTemplateAction",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentTemplateActionMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fis.types.experiment_template_action

        out[key] = capo_fis.types.experiment_template_action.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ExperimentTemplateActionMap:
    out: ExperimentTemplateActionMap = {}
    for key, value in data.items():
        import capo_fis.types.experiment_template_action

        out[key] = capo_fis.types.experiment_template_action.deserialize_json(value)
    return out
