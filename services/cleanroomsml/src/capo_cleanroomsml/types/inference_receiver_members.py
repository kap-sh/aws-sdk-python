"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#InferenceReceiverMembers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.inference_receiver_member

InferenceReceiverMembers: TypeAlias = list[
    "capo_cleanroomsml.types.inference_receiver_member.InferenceReceiverMember"
]


# --- restJson1 ser/de ---
def serialize_json(value: InferenceReceiverMembers) -> list:
    import capo_cleanroomsml.types.inference_receiver_member

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.inference_receiver_member.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> InferenceReceiverMembers:
    import capo_cleanroomsml.types.inference_receiver_member

    out: InferenceReceiverMembers = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.inference_receiver_member.deserialize_json(item)
        )
    return out
