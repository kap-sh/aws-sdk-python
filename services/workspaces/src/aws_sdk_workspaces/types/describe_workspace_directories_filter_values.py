"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.describe_workspace_directories_filter_value

DescribeWorkspaceDirectoriesFilterValues: TypeAlias = list[
    "aws_sdk_workspaces.types.describe_workspace_directories_filter_value.DescribeWorkspaceDirectoriesFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeWorkspaceDirectoriesFilterValues:
    return list(data)
