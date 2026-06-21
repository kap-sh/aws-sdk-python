"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilterName``."""

from typing import Literal, TypeAlias, cast

DescribeWorkspacesPoolsFilterName: TypeAlias = Literal["PoolName",]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeWorkspacesPoolsFilterName:
    return cast(DescribeWorkspacesPoolsFilterName, data)
