"""Generated from Smithy shape ``com.amazonaws.grafana#CreateWorkspaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.workspace_description


class CreateWorkspaceResponse(TypedDict, closed=True):
    workspace: "aws_sdk_grafana.types.workspace_description.WorkspaceDescription"
    """<p>A structure containing data about the workspace that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateWorkspaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.workspace_description

    out["workspace"] = aws_sdk_grafana.types.workspace_description.serialize_json(
        value["workspace"]
    )
    return out


def deserialize_json(data: dict) -> CreateWorkspaceResponse:
    out: CreateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "workspace" in data:
        import aws_sdk_grafana.types.workspace_description

        out["workspace"] = aws_sdk_grafana.types.workspace_description.deserialize_json(
            data["workspace"]
        )
    else:
        raise DeserializationError("CreateWorkspaceResponse.workspace required")
    return out
