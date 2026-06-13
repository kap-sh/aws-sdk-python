"""Generated from Smithy shape ``com.amazonaws.qconnect#GenerativeContentFeedbackData``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.relevance


class GenerativeContentFeedbackData(TypedDict):
    relevance: "aws_sdk_qconnect.types.relevance.Relevance"
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
