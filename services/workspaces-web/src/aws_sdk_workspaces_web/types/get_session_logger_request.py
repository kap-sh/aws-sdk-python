"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetSessionLoggerRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class GetSessionLoggerRequest(TypedDict):
    session_logger_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionLoggerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionLoggerRequest:
    out: GetSessionLoggerRequest = {}  # type: ignore[typeddict-item]
    return out
