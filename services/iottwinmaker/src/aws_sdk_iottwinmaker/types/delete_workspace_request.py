"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteWorkspaceRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id


class DeleteWorkspaceRequest(TypedDict):
    workspace_id: "aws_sdk_iottwinmaker.types.id.Id"
    """<p>The ID of the workspace to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceRequest:
    out: DeleteWorkspaceRequest = {}  # type: ignore[typeddict-item]
    return out
