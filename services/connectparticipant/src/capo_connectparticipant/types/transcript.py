"""Generated from Smithy shape ``com.amazonaws.connectparticipant#Transcript``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connectparticipant.types.item

Transcript: TypeAlias = list["capo_connectparticipant.types.item.Item"]


# --- restJson1 ser/de ---
def serialize_json(value: Transcript) -> list:
    import capo_connectparticipant.types.item

    out: list = []
    for item in value:
        out.append(capo_connectparticipant.types.item.serialize_json(item))
    return out


def deserialize_json(data: list) -> Transcript:
    import capo_connectparticipant.types.item

    out: Transcript = []
    for item in data:
        out.append(capo_connectparticipant.types.item.deserialize_json(item))
    return out
