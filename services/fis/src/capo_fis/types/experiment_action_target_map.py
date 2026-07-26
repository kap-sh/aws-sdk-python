"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionTargetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_action_target_name
    import capo_fis.types.experiment_target_name

ExperimentActionTargetMap: TypeAlias = dict[
    "capo_fis.types.experiment_action_target_name.ExperimentActionTargetName",
    "capo_fis.types.experiment_target_name.ExperimentTargetName",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentActionTargetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> ExperimentActionTargetMap:
    out: ExperimentActionTargetMap = {}
    for key, value in data.items():
        out[key] = value
    return out
