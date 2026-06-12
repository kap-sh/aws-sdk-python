"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalAlternativeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_alternative

MedicalAlternativeList: TypeAlias = list[
    "aws_sdk_transcribe_streaming.types.medical_alternative.MedicalAlternative"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalAlternativeList) -> list:
    import aws_sdk_transcribe_streaming.types.medical_alternative

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe_streaming.types.medical_alternative.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MedicalAlternativeList:
    import aws_sdk_transcribe_streaming.types.medical_alternative

    out: MedicalAlternativeList = []
    for item in data:
        out.append(
            aws_sdk_transcribe_streaming.types.medical_alternative.deserialize_json(
                item
            )
        )
    return out
