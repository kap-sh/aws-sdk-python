"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_workspaces.types.describe_workspaces_pools_filter_value

DescribeWorkspacesPoolsFilterValues: TypeAlias = list[
    "aws_sdk_workspaces.types.describe_workspaces_pools_filter_value.DescribeWorkspacesPoolsFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> DescribeWorkspacesPoolsFilterValues:
    return list(data)
