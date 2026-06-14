"""Generated from Smithy shape ``com.amazonaws.workspacesweb#GetPortalRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.arn


class GetPortalRequest(TypedDict):
    portal_arn: "aws_sdk_workspaces_web.types.arn.ARN"
    """<p>The ARN of the web portal.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPortalRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPortalRequest:
    out: GetPortalRequest = {}  # type: ignore[typeddict-item]
    return out
