"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#CollaborationTrainedModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_summary

CollaborationTrainedModelList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.collaboration_trained_model_summary.CollaborationTrainedModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: CollaborationTrainedModelList) -> list:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.collaboration_trained_model_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CollaborationTrainedModelList:
    import aws_sdk_cleanroomsml.types.collaboration_trained_model_summary

    out: CollaborationTrainedModelList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.collaboration_trained_model_summary.deserialize_json(
                item
            )
        )
    return out
