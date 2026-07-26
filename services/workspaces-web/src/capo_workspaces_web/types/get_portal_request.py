"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetPortalRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_workspaces_web.types.arn


class GetPortalRequest(TypedDict, closed=True):
    portal_arn: "capo_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPortalRequest:
    out: GetPortalRequest = {}  # type: ignore[typeddict-item]
    return out
