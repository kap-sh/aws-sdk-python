"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilterOperator``."""

from typing import Literal, TypeAlias, cast

DescribeWorkspacesPoolsFilterOperator: TypeAlias = Literal[
    "EQUALS",
    "NOTEQUALS",
    "CONTAINS",
    "NOTCONTAINS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeWorkspacesPoolsFilterOperator:
    return cast(DescribeWorkspacesPoolsFilterOperator, data)
