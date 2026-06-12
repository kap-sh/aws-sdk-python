"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalEntityList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_entity

MedicalEntityList: TypeAlias = list[
    "aws_sdk_transcribe_streaming.types.medical_entity.MedicalEntity"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalEntityList) -> list:
    import aws_sdk_transcribe_streaming.types.medical_entity

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe_streaming.types.medical_entity.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MedicalEntityList:
    import aws_sdk_transcribe_streaming.types.medical_entity

    out: MedicalEntityList = []
    for item in data:
        out.append(
            aws_sdk_transcribe_streaming.types.medical_entity.deserialize_json(item)
        )
    return out
