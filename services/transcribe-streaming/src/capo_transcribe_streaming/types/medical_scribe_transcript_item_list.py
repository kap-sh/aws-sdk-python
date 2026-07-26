"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeTranscriptItemList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.medical_scribe_transcript_item

MedicalScribeTranscriptItemList: TypeAlias = list[
    "capo_transcribe_streaming.types.medical_scribe_transcript_item.MedicalScribeTranscriptItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptItemList) -> list:
    import capo_transcribe_streaming.types.medical_scribe_transcript_item

    out: list = []
    for item in value:
        out.append(
            capo_transcribe_streaming.types.medical_scribe_transcript_item.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> MedicalScribeTranscriptItemList:
    import capo_transcribe_streaming.types.medical_scribe_transcript_item

    out: MedicalScribeTranscriptItemList = []
    for item in data:
        out.append(
            capo_transcribe_streaming.types.medical_scribe_transcript_item.deserialize_json(
                item
            )
        )
    return out
