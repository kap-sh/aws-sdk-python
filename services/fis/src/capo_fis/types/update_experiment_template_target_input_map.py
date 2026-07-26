"""Generated from Smithy shape ``com.amazonaws.fis#UpdateExperimentTemplateTargetInputMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_target_name
    import capo_fis.types.update_experiment_template_target_input

UpdateExperimentTemplateTargetInputMap: TypeAlias = dict[
    "capo_fis.types.experiment_template_target_name.ExperimentTemplateTargetName",
    "capo_fis.types.update_experiment_template_target_input.UpdateExperimentTemplateTargetInput",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: UpdateExperimentTemplateTargetInputMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fis.types.update_experiment_template_target_input

        out[key] = (
            capo_fis.types.update_experiment_template_target_input.serialize_json(value)
        )
    return out


def deserialize_json(data: dict) -> UpdateExperimentTemplateTargetInputMap:
    out: UpdateExperimentTemplateTargetInputMap = {}
    for key, value in data.items():
        import capo_fis.types.update_experiment_template_target_input

        out[key] = (
            capo_fis.types.update_experiment_template_target_input.deserialize_json(
                value
            )
        )
    return out
