"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#Entity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.confidence
    import aws_sdk_transcribe_streaming.types.double
    import aws_sdk_transcribe_streaming.types.string


class Entity(TypedDict):
    start_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The start time of the utterance that was identified as PII in seconds, with millisecond precision (e.g., 1.056)</p>"""
    end_time: "aws_sdk_transcribe_streaming.types.double.Double"
    """<p>The end time of the utterance that was identified as PII in seconds, with millisecond precision (e.g., 1.056)</p>"""
    category: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The category of information identified. The only category is <code>PII</code>.</p>"""
    type: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The type of PII identified. For example, <code>NAME</code> or <code>CREDIT_DEBIT_NUMBER</code>.</p>"""
    content: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The word or words identified as PII.</p>"""
    confidence: NotRequired["aws_sdk_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with the identified PII entity in your audio.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Entity) -> dict:
    out: dict = {}
    out["StartTime"] = value.get("start_time", 0)
    out["EndTime"] = value.get("end_time", 0)
    if "category" in value:
        out["Category"] = value["category"]
    if "type" in value:
        out["Type"] = value["type"]
    if "content" in value:
        out["Content"] = value["content"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_json(data: dict) -> Entity:
    out: Entity = {}  # type: ignore[typeddict-item]
    if "StartTime" in data:
        out["start_time"] = data["StartTime"]
    else:
        out["start_time"] = 0
    if "EndTime" in data:
        out["end_time"] = data["EndTime"]
    else:
        out["end_time"] = 0
    if "Category" in data:
        out["category"] = data["Category"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
