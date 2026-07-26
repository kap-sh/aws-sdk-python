"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#Participants``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_chime_sdk_voice.types.participant

Participants: TypeAlias = list["capo_chime_sdk_voice.types.participant.Participant"]


# --- restJson1 ser/de ---
def serialize_json(value: Participants) -> list:
    import capo_chime_sdk_voice.types.participant

    out: list = []
    for item in value:
        out.append(capo_chime_sdk_voice.types.participant.serialize_json(item))
    return out


def deserialize_json(data: list) -> Participants:
    import capo_chime_sdk_voice.types.participant

    out: Participants = []
    for item in data:
        out.append(capo_chime_sdk_voice.types.participant.deserialize_json(item))
    return out
