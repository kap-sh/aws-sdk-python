"""Generated from Smithy shape ``com.amazonaws.wisdom#SessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.arn
    import aws_sdk_wisdom.types.uuid


class SessionSummary(TypedDict, closed=True):
    session_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the session.</p>"""
    session_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    assistant_id: "aws_sdk_wisdom.types.uuid.Uuid"
    """<p>The identifier of the Wisdom assistant.</p>"""
    assistant_arn: "aws_sdk_wisdom.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Wisdom assistant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if "sessionId" in data:
        out["session_id"] = data["sessionId"]
    else:
        raise DeserializationError("SessionSummary.session_id required")
    if "sessionArn" in data:
        out["session_arn"] = data["sessionArn"]
    else:
        raise DeserializationError("SessionSummary.session_arn required")
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("SessionSummary.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("SessionSummary.assistant_arn required")
    return out
