"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#WorkspaceInstanceErrors``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.workspace_instance_error

WorkspaceInstanceErrors: TypeAlias = list[
    "capo_workspaces_instances.types.workspace_instance_error.WorkspaceInstanceError"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkspaceInstanceErrors) -> list:
    import capo_workspaces_instances.types.workspace_instance_error

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.workspace_instance_error.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkspaceInstanceErrors:
    import capo_workspaces_instances.types.workspace_instance_error

    out: WorkspaceInstanceErrors = []
    for item in data:
        out.append(
            capo_workspaces_instances.types.workspace_instance_error.deserialize_aws_json_1_0(
                item
            )
        )
    return out
