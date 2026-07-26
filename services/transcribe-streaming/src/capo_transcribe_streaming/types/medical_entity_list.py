"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_entity

MedicalEntityList: TypeAlias = list[
    "capo_transcribe_streaming.types.medical_entity.MedicalEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalEntityList) -> list:
    import capo_transcribe_streaming.types.medical_entity

    out: list = []
    for item in value:
        out.append(capo_transcribe_streaming.types.medical_entity.serialize_json(item))
    return out


def deserialize_json(data: list) -> MedicalEntityList:
    import capo_transcribe_streaming.types.medical_entity

    out: MedicalEntityList = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.medical_entity.deserialize_json(item)
        )
    return out
