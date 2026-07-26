"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#WorkspaceInstances``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces_instances.types.workspace_instance

WorkspaceInstances: TypeAlias = list[
    "capo_workspaces_instances.types.workspace_instance.WorkspaceInstance"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: WorkspaceInstances) -> list:
    import capo_workspaces_instances.types.workspace_instance

    out: list = []
    for item in value:
        out.append(
            capo_workspaces_instances.types.workspace_instance.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> WorkspaceInstances:
    import capo_workspaces_instances.types.workspace_instance

    out: WorkspaceInstances = []
    for item in data:
        out.append(
            capo_workspaces_instances.types.workspace_instance.deserialize_aws_json_1_0(
                item
            )
        )
    return out
