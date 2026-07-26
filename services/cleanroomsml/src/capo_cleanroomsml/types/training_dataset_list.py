"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainingDatasetList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.training_dataset_summary

TrainingDatasetList: TypeAlias = list[
    "capo_cleanroomsml.types.training_dataset_summary.TrainingDatasetSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainingDatasetList) -> list:
    import capo_cleanroomsml.types.training_dataset_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.training_dataset_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TrainingDatasetList:
    import capo_cleanroomsml.types.training_dataset_summary

    out: TrainingDatasetList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.training_dataset_summary.deserialize_json(item)
        )
    return out
