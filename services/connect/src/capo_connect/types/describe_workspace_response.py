"""Generated from Smithy shape ``com.amazonaws.connect#DescribeWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.workspace


class DescribeWorkspaceResponse(TypedDict, closed=True):
    workspace: "capo_connect.types.workspace.Workspace"
    """<p>Information about the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceResponse) -> dict:
    out: dict = {}
    import capo_connect.types.workspace

    out["Workspace"] = capo_connect.types.workspace.serialize_json(value["workspace"])
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceResponse:
    out: DescribeWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "Workspace" in data:
        import capo_connect.types.workspace

        out["workspace"] = capo_connect.types.workspace.deserialize_json(
            data["Workspace"]
        )
    else:
        raise DeserializationError("DescribeWorkspaceResponse.workspace required")
    return out
