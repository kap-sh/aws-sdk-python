"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateActionTargetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_action_target_name
    import capo_fis.types.experiment_template_target_name

ExperimentTemplateActionTargetMap: TypeAlias = dict[
    "capo_fis.types.experiment_template_action_target_name.ExperimentTemplateActionTargetName",
    "capo_fis.types.experiment_template_target_name.ExperimentTemplateTargetName",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentTemplateActionTargetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExperimentTemplateActionTargetMap:
    out: ExperimentTemplateActionTargetMap = {}
    for key, value in data.items():
        out[key] = value
    return out
