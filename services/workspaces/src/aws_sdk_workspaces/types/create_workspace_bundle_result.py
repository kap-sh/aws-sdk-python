"""Generated from Smithy shape ``com.amazonaws.workspaces#CreateWorkspaceBundleResult``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_bundle


class CreateWorkspaceBundleResult(TypedDict):
    workspace_bundle: NotRequired[
        "aws_sdk_workspaces.types.workspace_bundle.WorkspaceBundle"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateWorkspaceBundleResult) -> dict:
    out: dict = {}
    if "workspace_bundle" in value:
        import aws_sdk_workspaces.types.workspace_bundle

        out["WorkspaceBundle"] = (
            aws_sdk_workspaces.types.workspace_bundle.serialize_aws_json_1_1(
                value["workspace_bundle"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateWorkspaceBundleResult:
    out: CreateWorkspaceBundleResult = {}  # type: ignore[typeddict-item]
    if "WorkspaceBundle" in data:
        import aws_sdk_workspaces.types.workspace_bundle

        out["workspace_bundle"] = (
            aws_sdk_workspaces.types.workspace_bundle.deserialize_aws_json_1_1(
                data["WorkspaceBundle"]
            )
        )
    return out
