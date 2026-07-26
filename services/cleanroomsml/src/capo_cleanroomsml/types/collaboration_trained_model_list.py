"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationTrainedModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.collaboration_trained_model_summary

CollaborationTrainedModelList: TypeAlias = list[
    "capo_cleanroomsml.types.collaboration_trained_model_summary.CollaborationTrainedModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationTrainedModelList) -> list:
    import capo_cleanroomsml.types.collaboration_trained_model_summary

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.collaboration_trained_model_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationTrainedModelList:
    import capo_cleanroomsml.types.collaboration_trained_model_summary

    out: CollaborationTrainedModelList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.collaboration_trained_model_summary.deserialize_json(
                item
            )
        )
    return out
