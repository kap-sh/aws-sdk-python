"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#MedicalEntity``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_transcribe_streaming.types.confidence
    import capo_transcribe_streaming.types.double
    import capo_transcribe_streaming.types.string


class MedicalEntity(TypedDict, closed=True):
    start_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The start time, in seconds, of the utterance that was identified as PHI.</p>"""
    end_time: "capo_transcribe_streaming.types.double.Double"
    """<p>The end time, in seconds, of the utterance that was identified as PHI.</p>"""
    category: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>The category of information identified. The only category is <code>PHI</code>.</p>"""
    content: NotRequired["capo_transcribe_streaming.types.string.String"]
    """<p>The word or words identified as PHI.</p>"""
    confidence: NotRequired["capo_transcribe_streaming.types.confidence.Confidence"]
    """<p>The confidence score associated with the identified PHI entity in your audio.</p> <p>Confidence scores are values between 0 and 1. A larger value indicates a higher probability that the identified entity correctly matches the entity spoken in your media.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MedicalEntity) -> dict:
    out: dict = {}
    out["StartTime"] = value.get("start_time", 0)
    out["EndTime"] = value.get("end_time", 0)
    if "category" in value:
        out["Category"] = value["category"]
    if "content" in value:
        out["Content"] = value["content"]
    if "confidence" in value:
        out["Confidence"] = value["confidence"]
    return out


def deserialize_json(data: dict) -> MedicalEntity:
    out: MedicalEntity = {}  # type: ignore[typeddict-item]
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
    if "Content" in data:
        out["content"] = data["Content"]
    if "Confidence" in data:
        out["confidence"] = data["Confidence"]
    return out
