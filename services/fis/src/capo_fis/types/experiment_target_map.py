"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentTargetMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_target
    import capo_fis.types.experiment_target_name

ExperimentTargetMap: TypeAlias = dict[
    "capo_fis.types.experiment_target_name.ExperimentTargetName",
    "capo_fis.types.experiment_target.ExperimentTarget",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: ExperimentTargetMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        import capo_fis.types.experiment_target

        out[key] = capo_fis.types.experiment_target.serialize_json(value)
    return out


def deserialize_json(data: dict) -> ExperimentTargetMap:
    out: ExperimentTargetMap = {}
    for key, value in data.items():
        import capo_fis.types.experiment_target

        out[key] = capo_fis.types.experiment_target.deserialize_json(value)
    return out
