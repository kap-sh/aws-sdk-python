"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#EntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.entity

EntityList: TypeAlias = list["capo_transcribe_streaming.types.entity.Entity"]


# --- restJson1 ser/de ---
def serialize_json(value: EntityList) -> list:
    import capo_transcribe_streaming.types.entity

    out: list = []
    for item in value:
        out.append(capo_transcribe_streaming.types.entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> EntityList:
    import capo_transcribe_streaming.types.entity

    out: EntityList = []
    for item in data:
        out.append(capo_transcribe_streaming.types.entity.deserialize_json(item))
    return out
