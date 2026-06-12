"""Generated from Smithy shape ``com.amazonaws.grafana#DescribeWorkspaceAuthenticationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_grafana.types.workspace_id

class DescribeWorkspaceAuthenticationRequest(TypedDict):
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to return authentication information about.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceAuthenticationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceAuthenticationRequest:
    out: DescribeWorkspaceAuthenticationRequest = {}  # type: ignore[typeddict-item]
    return out