"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilterOperator``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

DescribeWorkspacesPoolsFilterOperator: TypeAlias = Literal[
    "EQUALS",
    "NOTEQUALS",
    "CONTAINS",
    "NOTCONTAINS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EQUALS",
        "NOTEQUALS",
        "CONTAINS",
        "NOTCONTAINS",
    )
)


def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilterOperator) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeWorkspacesPoolsFilterOperator:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DescribeWorkspacesPoolsFilterOperator value: {data!r}"
        )
    return cast(DescribeWorkspacesPoolsFilterOperator, data)
