"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#TrainedModelExportReceiverMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.trained_model_export_receiver_member

TrainedModelExportReceiverMembers: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.trained_model_export_receiver_member.TrainedModelExportReceiverMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: TrainedModelExportReceiverMembers) -> list:
    import aws_sdk_cleanroomsml.types.trained_model_export_receiver_member

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.trained_model_export_receiver_member.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> TrainedModelExportReceiverMembers:
    import aws_sdk_cleanroomsml.types.trained_model_export_receiver_member

    out: TrainedModelExportReceiverMembers = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.trained_model_export_receiver_member.deserialize_json(
                item
            )
        )
    return out
