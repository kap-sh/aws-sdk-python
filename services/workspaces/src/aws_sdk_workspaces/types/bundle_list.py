"""Generated from Smithy shape ``com.amazonaws.workspaces#BundleList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.workspace_bundle

BundleList: TypeAlias = list[
    "aws_sdk_workspaces.types.workspace_bundle.WorkspaceBundle"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BundleList) -> list:
    import aws_sdk_workspaces.types.workspace_bundle

    out: list = []
    for item in value:
        out.append(
            aws_sdk_workspaces.types.workspace_bundle.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> BundleList:
    import aws_sdk_workspaces.types.workspace_bundle

    out: BundleList = []
    for item in data:
        out.append(
            aws_sdk_workspaces.types.workspace_bundle.deserialize_aws_json_1_1(item)
        )
    return out
