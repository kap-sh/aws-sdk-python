"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateSessionLoggerRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn

class AssociateSessionLoggerRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the portal to associate to the session logger ARN.</p>"""
    session_logger_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger to associate to the portal ARN.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: AssociateSessionLoggerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> AssociateSessionLoggerRequest:
    out: AssociateSessionLoggerRequest = {}  # type: ignore[typeddict-item]
    return out