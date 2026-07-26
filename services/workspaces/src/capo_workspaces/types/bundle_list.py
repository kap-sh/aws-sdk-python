"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_workspaces.types.workspace_bundle

BundleList: TypeAlias = list["capo_workspaces.types.workspace_bundle.WorkspaceBundle"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleList) -> list:
    import capo_workspaces.types.workspace_bundle

    out: list = []
    for item in value:
        out.append(capo_workspaces.types.workspace_bundle.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> BundleList:
    import capo_workspaces.types.workspace_bundle

    out: BundleList = []
    for item in data:
        out.append(
            capo_workspaces.types.workspace_bundle.deserialize_aws_json_1_1(item)
        )
    return out
