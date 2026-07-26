"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.item

ItemList: TypeAlias = list["capo_transcribe_streaming.types.item.Item"]


# --- restJson1 ser/de ---
def serialize_json(value: ItemList) -> list:
    import capo_transcribe_streaming.types.item

    out: list = []
    for item in value:
        out.append(capo_transcribe_streaming.types.item.serialize_json(item))
    return out


def deserialize_json(data: list) -> ItemList:
    import capo_transcribe_streaming.types.item

    out: ItemList = []
    for item in data:
        out.append(capo_transcribe_streaming.types.item.deserialize_json(item))
    return out
