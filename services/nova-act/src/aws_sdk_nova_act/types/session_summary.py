"""Generated from Smithy shape ``com.amazonaws.novaact#SessionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_nova_act.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.uuid_string


class SessionSummary(TypedDict):
    session_id: "aws_sdk_nova_act.types.uuid_string.UuidString"
    """<p>The unique identifier of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionSummary.session_id required")
    return out
