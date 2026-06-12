"""Generated from Smithy shape ``com.amazonaws.grafana#DescribeWorkspaceConfigurationRequest``."""

from typing import TYPE_CHECKING, TypedDict
if TYPE_CHECKING:
    import aws_sdk_grafana.types.workspace_id

class DescribeWorkspaceConfigurationRequest(TypedDict):
    workspace_id: "aws_sdk_grafana.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to get configuration information for.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceConfigurationRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceConfigurationRequest:
    out: DescribeWorkspaceConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out