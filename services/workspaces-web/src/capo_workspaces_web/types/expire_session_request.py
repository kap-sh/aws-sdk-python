"""Generated from Smithy shape ``com.amazonaws.workspacesweb#ExpireSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.portal_id
    import capo_workspaces_web.types.session_id


class ExpireSessionRequest(TypedDict, closed=True):
    portal_id: "capo_workspaces_web.types.portal_id.PortalId"
    """<p>The ID of the web portal for the session.</p>"""
    session_id: "capo_workspaces_web.types.session_id.SessionId"
    """<p>The ID of the session to expire.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ExpireSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ExpireSessionRequest:
    out: ExpireSessionRequest = {}  # type: ignore[typeddict-item]
    return out
