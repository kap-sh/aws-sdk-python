"""Generated from Smithy shape ``com.amazonaws.grafana#UpdateWorkspaceResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_grafana.types.workspace_description


class UpdateWorkspaceResponse(TypedDict):
    workspace: "aws_sdk_grafana.types.workspace_description.WorkspaceDescription"
    """<p>A structure containing data about the workspace that was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateWorkspaceResponse) -> dict:
    out: dict = {}
    import aws_sdk_grafana.types.workspace_description

    out["workspace"] = aws_sdk_grafana.types.workspace_description.serialize_json(
        value["workspace"]
    )
    return out


def deserialize_json(data: dict) -> UpdateWorkspaceResponse:
    out: UpdateWorkspaceResponse = {}  # type: ignore[typeddict-item]
    if "workspace" in data:
        import aws_sdk_grafana.types.workspace_description

        out["workspace"] = aws_sdk_grafana.types.workspace_description.deserialize_json(
            data["workspace"]
        )
    else:
        raise DeserializationError("UpdateWorkspaceResponse.workspace required")
    return out
