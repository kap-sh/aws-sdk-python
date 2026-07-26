"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_item

MedicalItemList: TypeAlias = list[
    "capo_transcribe_streaming.types.medical_item.MedicalItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalItemList) -> list:
    import capo_transcribe_streaming.types.medical_item

    out: list = []
    for item in value:
        out.append(capo_transcribe_streaming.types.medical_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> MedicalItemList:
    import capo_transcribe_streaming.types.medical_item

    out: MedicalItemList = []
    for item in data:
        out.append(capo_transcribe_streaming.types.medical_item.deserialize_json(item))
    return out
