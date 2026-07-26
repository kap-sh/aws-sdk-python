"""Generated from Smithy shape ``com.amazonaws.fis#ExperimentActionStartAfterList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_fis.types.experiment_action_start_after

ExperimentActionStartAfterList: TypeAlias = list[
    "capo_fis.types.experiment_action_start_after.ExperimentActionStartAfter"
]


# --- restJson1 ser/de ---
def serialize_json(value: ExperimentActionStartAfterList) -> list:
    return list(value)


def deserialize_json(data: list) -> ExperimentActionStartAfterList:
    return list(data)
