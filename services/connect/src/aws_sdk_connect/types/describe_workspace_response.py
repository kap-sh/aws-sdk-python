"""Generated from Smithy shape ``com.amazonaws.connect#DescribeWorkspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.workspace


class DescribeWorkspaceResponse(TypedDict):
    workspace: "aws_sdk_connect.types.workspace.Workspace"
    """<p>Information about the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeWorkspaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_connect.types.workspace

    out["Workspace"] = aws_sdk_connect.types.workspace.serialize_json(
        value["workspace"]
    )
    return out


def deserialize_json(data: dict) -> DescribeWorkspaceResponse:
    out: DescribeWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "Workspace" in data:
        import aws_sdk_connect.types.workspace

        out["workspace"] = aws_sdk_connect.types.workspace.deserialize_json(
            data["Workspace"]
        )
    else:
        raise DeserializationError("DescribeWorkspaceResponse.workspace required")
    return out
