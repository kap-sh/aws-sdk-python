"""Generated from Smithy shape ``com.amazonaws.workspacesweb#CreateSessionLoggerResponse``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_workspaces_web.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class CreateSessionLoggerResponse(TypedDict):
    session_logger_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CreateSessionLoggerResponse) -> dict:
    out: dict = {}
    out["sessionLoggerArn"] = value["session_logger_arn"]
    return out


def deserialize_json(data: dict) -> CreateSessionLoggerResponse:
    out: CreateSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if "sessionLoggerArn" in data:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    else:
        raise DeserializationError("CreateSessionLoggerResponse.session_logger_arn required")
    return out