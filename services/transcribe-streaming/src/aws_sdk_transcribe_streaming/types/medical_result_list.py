"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.medical_result

MedicalResultList: TypeAlias = list[
    "aws_sdk_transcribe_streaming.types.medical_result.MedicalResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalResultList) -> list:
    import aws_sdk_transcribe_streaming.types.medical_result

    out: list = []
    for item in value:
        out.append(
            aws_sdk_transcribe_streaming.types.medical_result.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> MedicalResultList:
    import aws_sdk_transcribe_streaming.types.medical_result

    out: MedicalResultList = []
    for item in data:
        out.append(
            aws_sdk_transcribe_streaming.types.medical_result.deserialize_json(item)
        )
    return out
