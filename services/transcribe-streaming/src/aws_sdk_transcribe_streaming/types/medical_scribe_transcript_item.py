"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalScribeTranscriptItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.confidence
    import aws_sdk_transcribe_streaming.types.double
    import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_type
    import aws_sdk_transcribe_streaming.types.nullable_boolean
    import aws_sdk_transcribe_streaming.types.string


class MedicalScribeTranscriptItem(TypedDict, closed=True):
    begin_audio_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The start time, in milliseconds, of the transcribed item.</p>"""
    end_audio_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The end time, in milliseconds, of the transcribed item.</p>"""
    type: NotRequired[
        "aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_type.MedicalScribeTranscriptItemType"
    ]
    """<p>The type of item identified. Options are: <code>PRONUNCIATION</code> (spoken words) and <code>PUNCTUATION</code>. </p>"""
    confidence: NotRequired["aws_sdk_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with a word or phrase in your transcript.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media. </p>"""
    content: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The word, phrase or punctuation mark that was transcribed.</p>"""
    vocabulary_filter_match: NotRequired[
        "aws_sdk_transcribe_streaming.types.nullable_boolean.NullableBoolean"
    ]
    """<p>Indicates whether the specified item matches a word in the vocabulary filter included in your configuration event. If <code>true</code>, there is a vocabulary filter match. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalScribeTranscriptItem) -> dict:
    out: dict = {}
    out["BeginAudioTime"] = value.get("begin_audio_time", 0)
    out["EndAudioTime"] = value.get("end_audio_time", 0)
    if "type" in value:
        import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_type

        out["Type"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_type.serialize_json(
                value["type"]
            )
        )
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "content" in value:
        out["Content"] = value["content"]
    if "vocabulary_filter_match" in value:
        out["VocabularyFilterMatch"] = value["vocabulary_filter_match"]
    return out


def deserialize_json(data: dict) -> MedicalScribeTranscriptItem:
    out: MedicalScribeTranscriptItem = {}  # type: ignore[typeddict-item]
    if "BeginAudioTime" in data:
        out["begin_audio_time"] = data["BeginAudioTime"]
    else:
        out["begin_audio_time"] = 0
    if "EndAudioTime" in data:
        out["end_audio_time"] = data["EndAudioTime"]
    else:
        out["end_audio_time"] = 0
    if "Type" in data:
        import aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_type

        out["type"] = (
            aws_sdk_transcribe_streaming.types.medical_scribe_transcript_item_type.deserialize_json(
                data["Type"]
            )
        )
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "VocabularyFilterMatch" in data:
        out["vocabulary_filter_match"] = data["VocabularyFilterMatch"]
    return out
