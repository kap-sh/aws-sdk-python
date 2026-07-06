"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#CallAnalyticsItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_transcribe_streaming.types.boolean
    import aws_sdk_transcribe_streaming.types.confidence
    import aws_sdk_transcribe_streaming.types.item_type
    import aws_sdk_transcribe_streaming.types.long
    import aws_sdk_transcribe_streaming.types.stable
    import aws_sdk_transcribe_streaming.types.string


class CallAnalyticsItem(TypedDict, closed=True):
    begin_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the start of the identified item.</p>"""
    end_offset_millis: NotRequired["aws_sdk_transcribe_streaming.types.long.Long"]
    """<p>The time, in milliseconds, from the beginning of the audio stream to the end of the identified item.</p>"""
    type: NotRequired["aws_sdk_transcribe_streaming.types.item_type.ItemType"]
    """<p>The type of item identified. Options are: <code>PRONUNCIATION</code> (spoken words) and <code>PUNCTUATION</code>.</p>"""
    content: NotRequired["aws_sdk_transcribe_streaming.types.string.String"]
    """<p>The word or punctuation that was transcribed.</p>"""
    confidence: NotRequired["aws_sdk_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with a word or phrase in your transcript.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified item correctly matches the item spoken in your media.</p>"""
    vocabulary_filter_match: "aws_sdk_transcribe_streaming.types.boolean.Boolean"
    """<p>Indicates whether the specified item matches a word in the vocabulary filter included in your Call Analytics request. If <code>true</code>, there is a vocabulary filter match.</p>"""
    stable: NotRequired["aws_sdk_transcribe_streaming.types.stable.Stable"]
    """<p>If partial result stabilization is enabled, <code>Stable</code> indicates whether the specified item is stable (<code>true</code>) or if it may change when the segment is complete (<code>false</code>).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CallAnalyticsItem) -> dict:
    out: dict = {}
    if "begin_offset_millis" in value:
        out["BeginOffsetMillis"] = value["begin_offset_millis"]
    if "end_offset_millis" in value:
        out["EndOffsetMillis"] = value["end_offset_millis"]
    if "type" in value:
        import aws_sdk_transcribe_streaming.types.item_type

        out["Type"] = aws_sdk_transcribe_streaming.types.item_type.serialize_json(
            value["type"]
        )
    if "content" in value:
        out["Content"] = value["content"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    out["VocabularyFilterMatch"] = value.get("vocabulary_filter_match", False)
    if "stable" in value:
        out["Stable"] = value["stable"]
    return out


def deserialize_json(data: dict) -> CallAnalyticsItem:
    out: CallAnalyticsItem = {}  # type: ignore[typeddict-item]
    if "BeginOffsetMillis" in data:
        out["begin_offset_millis"] = data["BeginOffsetMillis"]
    if "EndOffsetMillis" in data:
        out["end_offset_millis"] = data["EndOffsetMillis"]
    if "Type" in data:
        import aws_sdk_transcribe_streaming.types.item_type

        out["type"] = aws_sdk_transcribe_streaming.types.item_type.deserialize_json(
            data["Type"]
        )
    if "Content" in data:
        out["content"] = data["Content"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    if "VocabularyFilterMatch" in data:
        out["vocabulary_filter_match"] = data["VocabularyFilterMatch"]
    else:
        out["vocabulary_filter_match"] = False
    if "Stable" in data:
        out["stable"] = data["Stable"]
    return out
