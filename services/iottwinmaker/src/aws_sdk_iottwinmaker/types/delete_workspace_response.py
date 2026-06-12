"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#DeleteWorkspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.workspace_delete_message


class DeleteWorkspaceResponse(TypedDict):
    message: NotRequired[
        "aws_sdk_iottwinmaker.types.workspace_delete_message.WorkspaceDeleteMessage"
    ]
    """<p>The string that specifies the delete result for the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteWorkspaceResponse) -> dict:
    out: dict = {}
    if "message" in value:
        out["message"] = value["message"]
    return out


def deserialize_json(data: dict) -> DeleteWorkspaceResponse:
    out: DeleteWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "message" in data:
        out["message"] = data["message"]
    return out
