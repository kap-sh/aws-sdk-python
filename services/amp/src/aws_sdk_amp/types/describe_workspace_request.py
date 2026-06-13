"""Generated from Smithy shape ``com.amazonaws.amp#DescribeWorkspaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_id


class DescribeWorkspaceRequest(TypedDict):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to describe.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceRequest:
    out: DescribeWorkspaceRequest = {}  # type: ignore[typeddict-item]
    return out
