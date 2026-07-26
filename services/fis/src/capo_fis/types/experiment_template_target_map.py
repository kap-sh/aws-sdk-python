"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTemplateTargetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_template_target
    import capo_fis.types.experiment_template_target_name

ExperimentTemplateTargetMap: TypeAlias = dict[
    "capo_fis.types.experiment_template_target_name.ExperimentTemplateTargetName",
    "capo_fis.types.experiment_template_target.ExperimentTemplateTarget",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentTemplateTargetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fis.types.experiment_template_target

        out[key] = capo_fis.types.experiment_template_target.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ExperimentTemplateTargetMap:
    out: ExperimentTemplateTargetMap = {}
    for key, value in data.items():
        import capo_fis.types.experiment_template_target

        out[key] = capo_fis.types.experiment_template_target.deserialize_json(value)
    return out
