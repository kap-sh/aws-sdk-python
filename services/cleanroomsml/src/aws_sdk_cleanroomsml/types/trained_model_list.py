"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_summary

TrainedModelList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.trained_model_summary.TrainedModelSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelList) -> list:
    import aws_sdk_cleanroomsml.types.trained_model_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.trained_model_summary.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TrainedModelList:
    import aws_sdk_cleanroomsml.types.trained_model_summary

    out: TrainedModelList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.trained_model_summary.deserialize_json(item)
        )
    return out
