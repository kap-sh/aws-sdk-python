"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspacesPoolsFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

DescribeWorkspacesPoolsFilterName: TypeAlias = Literal["PoolName",]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PoolName",))


def serialize_aws_json_1_1(value: DescribeWorkspacesPoolsFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeWorkspacesPoolsFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DescribeWorkspacesPoolsFilterName value: {data!r}"
        )
    return cast(DescribeWorkspacesPoolsFilterName, data)
