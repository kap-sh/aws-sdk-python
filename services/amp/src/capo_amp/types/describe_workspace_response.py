"""Generated from Smithy shape ``com.amazonaws.amp#DescribeWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_amp.errors import DeserializationError

if TYPE_CHECKING:
    import capo_amp.types.workspace_description


class DescribeWorkspaceResponse(TypedDict, closed=True):
    workspace: "capo_amp.types.workspace_description.WorkspaceDescription"
    """<p>A structure that contains details about the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceResponse) -> dict:
    out: dict = {}
    import capo_amp.types.workspace_description

    out["workspace"] = capo_amp.types.workspace_description.serialize_json(
        value["workspace"]
    )
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceResponse:
    out: DescribeWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "workspace" in data:
        import capo_amp.types.workspace_description

        out["workspace"] = capo_amp.types.workspace_description.deserialize_json(
            data["workspace"]
        )
    else:
        raise DeserializationError("DescribeWorkspaceResponse.workspace required")
    return out
