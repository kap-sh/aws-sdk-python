"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.confidence
    import aws_sdk_transcribe_streaming.types.double
    import aws_sdk_transcribe_streaming.types.item_type
    import aws_sdk_transcribe_streaming.types.string


class MedicalItem(TypedDict, closed=True):
    start_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The start time, in seconds, of the transcribed item.</p>"""
    end_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The end time, in seconds, of the transcribed item.</p>"""
    type: NotRequired["aws_sdk_transcribe_streaming.types.item_type.ItemType"]
    """<p>The type of item identified. Options are: <code>PRONUNCIATION</code> (spoken words) and <code>PUNCTUATION</code>.</p>"""
    content: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The word or punctuation that was transcribed.</p>"""
    confidence: NotRequired["aws_sdk_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with a word or phrase in your transcript.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.</p>"""
    speaker: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>If speaker partitioning is enabled, <code>Speaker</code> labels the speaker of the specified item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalItem) -> dict:
    out: dict = {}
    out["StartTime"] = value.get("start_time", 0)
    out["EndTime"] = value.get("end_time", 0)
    if "type" in value:
        import aws_sdk_transcribe_streaming.types.item_type

        out["Type"] = aws_sdk_transcribe_streaming.types.item_type.serialize_json(
            value["type"]
        )
    if "content" in value:
        out["Content"] = value["content"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    if "speaker" in value:
        out["Speaker"] = value["speaker"]
    return out


def deserialize_json(data: dict) -> MedicalItem:
    out: MedicalItem = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    else:
        out["start_time"] = 0
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    else:
        out["end_time"] = 0
    if "Type" in data:
        import aws_sdk_transcribe_streaming.types.item_type

        out["type"] = aws_sdk_transcribe_streaming.types.item_type.deserialize_json(
            data["Type"]
        )
    if "Content" in data:
        out["content"] = data["Content"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "Speaker" in data:
        out["speaker"] = data["Speaker"]
    return out
