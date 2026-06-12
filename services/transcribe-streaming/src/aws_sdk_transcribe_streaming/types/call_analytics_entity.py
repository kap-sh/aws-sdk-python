"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CallAnalyticsEntity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.confidence
    import aws_sdk_transcribe_streaming.types.long
    import aws_sdk_transcribe_streaming.types.string


class CallAnalyticsEntity(TypedDict):
    begin_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the start of the identified entity.</p>"""
    end_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the end of the identified entity.</p>"""
    category: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The category of information identified. For example, <code>PII</code>.</p>"""
    type: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The type of PII identified. For example, <code>NAME</code> or <code>CREDIT_DEBIT_NUMBER</code>.</p>"""
    content: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The word or words that represent the identified entity.</p>"""
    confidence: NotRequired["aws_sdk_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with the identification of an entity in your transcript.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsEntity) -> dict:
    out: dict = {}
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    if "category" in value:
        out["Category"] = value["category"]
    if "type" in value:
        out["Type"] = value["type"]
    if "content" in value:
        out["Content"] = value["content"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_json(data: dict) -> CallAnalyticsEntity:
    out: CallAnalyticsEntity = {}  # type: ignore[typeddict-item]
    if "BeginOffsetMillis" in data:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if "EndOffsetMillis" in data:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    if "Category" in data:
        out["category"] = data["Category"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "Content" in data:
        out["content"] = data["Content"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
