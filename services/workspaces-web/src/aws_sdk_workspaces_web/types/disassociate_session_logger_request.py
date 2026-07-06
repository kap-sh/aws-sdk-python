"""Generated from Smithy shape ``com.amazonaws.workspacesweb#DisassociateSessionLoggerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class DisassociateSessionLoggerRequest(TypedDict, closed=True):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the portal to disassociate from the a session logger.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateSessionLoggerRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateSessionLoggerRequest:
    out: DisassociateSessionLoggerRequest = {}  # type: ignore[typeddict-item]
    return out
