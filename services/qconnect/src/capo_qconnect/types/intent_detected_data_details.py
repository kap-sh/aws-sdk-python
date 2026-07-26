"""Generated from Smithy shape ``com.amazonaws.qconnect#IntentDetectedDataDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.relevance_level
    import capo_qconnect.types.sensitive_string
    import capo_qconnect.types.uuid


class IntentDetectedDataDetails(TypedDict, closed=True):
    intent: "capo_qconnect.types.sensitive_string.SensitiveString"
    """<p>The detected intent.</p>"""
    intent_id: "capo_qconnect.types.uuid.Uuid"
    """<p>The identifier of the detected intent.</p>"""
    relevance_level: NotRequired["capo_qconnect.types.relevance_level.RelevanceLevel"]
    """<p>The relevance level of the detected intent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntentDetectedDataDetails) -> dict:
    out: dict = {}
    out["intent"] = value["intent"]
    out["intentId"] = value["intent_id"]
    if "relevance_level" in value:
        out["relevanceLevel"] = value["relevance_level"]
    return out


def deserialize_json(data: dict) -> IntentDetectedDataDetails:
    out: IntentDetectedDataDetails = {}  # type: ignore[typeddict-item]
    if "intent" in data:
        out["intent"] = data["intent"]
    else:
        raise DeserializationError("IntentDetectedDataDetails.intent required")
    if "intentId" in data:
        out["intent_id"] = data["intentId"]
    else:
        raise DeserializationError("IntentDetectedDataDetails.intent_id required")
    if "relevanceLevel" in data:
        out["relevance_level"] = data["relevanceLevel"]
    return out
