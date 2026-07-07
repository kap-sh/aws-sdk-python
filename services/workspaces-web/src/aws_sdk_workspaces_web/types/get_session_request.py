"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.portal_id
    import aws_sdk_workspaces_web.types.session_id


class GetSessionRequest(TypedDict, closed=True):
    portal_id: "aws_sdk_workspaces_web.types.portal_id.PortalId"
    """<p>The ID of the web portal for the session.</p>"""
    session_id: "aws_sdk_workspaces_web.types.session_id.SessionId"
    """<p>The ID of the session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSessionRequest:
    out: GetSessionRequest = {}  # type: ignore[typeddict-item]
    return out
