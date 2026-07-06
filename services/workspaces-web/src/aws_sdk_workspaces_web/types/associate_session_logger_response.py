"""Generated from Smithy shape ``com.amazonaws.workspacesweb#AssociateSessionLoggerResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class AssociateSessionLoggerResponse(TypedDict, closed=True):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the portal.</p>"""
    session_logger_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateSessionLoggerResponse) -> dict:
    out: dict = {}
    out["portalArn"] = value["portal_arn"]
    out["sessionLoggerArn"] = value["session_logger_arn"]
    return out


def deserialize_json(data: dict) -> AssociateSessionLoggerResponse:
    out: AssociateSessionLoggerResponse = {}  # type: ignore[typeddict-item]
    if "portalArn" in data:
        out["portal_arn"] = data["portalArn"]
    else:
        raise DeserializationError("AssociateSessionLoggerResponse.portal_arn required")
    if "sessionLoggerArn" in data:
        out["session_logger_arn"] = data["sessionLoggerArn"]
    else:
        raise DeserializationError(
            "AssociateSessionLoggerResponse.session_logger_arn required"
        )
    return out
