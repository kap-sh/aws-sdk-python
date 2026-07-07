"""Generated from Smithy shape ``com.amazonaws.notifications#MessageComponentsSummary``."""

from typing_extensions import TypedDict

from aws_sdk_notifications.errors import DeserializationError


class MessageComponentsSummary(TypedDict, closed=True):
    headline: "str"
    """<p>A sentence long summary. For example, titles or an email subject line.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageComponentsSummary) -> dict:
    out: dict = {}
    out["headline"] = value["headline"]
    return out


def deserialize_json(data: dict) -> MessageComponentsSummary:
    out: MessageComponentsSummary = {}  # type: ignore[typeddict-item]
    if "headline" in data:
        out["headline"] = data["headline"]
    else:
        raise DeserializationError("MessageComponentsSummary.headline required")
    return out
