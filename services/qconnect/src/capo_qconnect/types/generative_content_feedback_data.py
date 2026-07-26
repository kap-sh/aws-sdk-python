"""Generated from Smithy shape ``com.amazonaws.qconnect#GenerativeContentFeedbackData``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.relevance


class GenerativeContentFeedbackData(TypedDict, closed=True):
    relevance: "capo_qconnect.types.relevance.Relevance"
    """<p>The relevance of the feedback.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerativeContentFeedbackData) -> dict:
    out: dict = {}
    out["relevance"] = value["relevance"]
    return out


def deserialize_json(data: dict) -> GenerativeContentFeedbackData:
    out: GenerativeContentFeedbackData = {}  # type: ignore[typeddict-item]
    if "relevance" in data:
        out["relevance"] = data["relevance"]
    else:
        raise DeserializationError("GenerativeContentFeedbackData.relevance required")
    return out
