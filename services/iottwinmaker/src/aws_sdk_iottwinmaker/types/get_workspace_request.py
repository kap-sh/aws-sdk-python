"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#GetWorkspaceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_iottwinmaker.types.id_or_arn


class GetWorkspaceRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_iottwinmaker.types.id_or_arn.IdOrArn"
    """<p>The ID of the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetWorkspaceRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetWorkspaceRequest:
    out: GetWorkspaceRequest = {}  # type: ignore[typeddict-item]
    return out
