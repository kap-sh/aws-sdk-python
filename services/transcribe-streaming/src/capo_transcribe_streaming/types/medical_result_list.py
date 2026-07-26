"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalResultList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_result

MedicalResultList: TypeAlias = list[
    "capo_transcribe_streaming.types.medical_result.MedicalResult"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalResultList) -> list:
    import capo_transcribe_streaming.types.medical_result

    out: list = []
    for item in value:
        out.append(capo_transcribe_streaming.types.medical_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> MedicalResultList:
    import capo_transcribe_streaming.types.medical_result

    out: MedicalResultList = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.medical_result.deserialize_json(item)
        )
    return out
