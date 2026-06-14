"""Generated from Smithy shape ``com.amazonaws.workspaces#DescribeWorkspaceDirectoriesFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

DescribeWorkspaceDirectoriesFilterName: TypeAlias = Literal[
    "USER_IDENTITY_TYPE",
    "WORKSPACE_TYPE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER_IDENTITY_TYPE",
        "WORKSPACE_TYPE",
    )
)


def serialize_aws_json_1_1(value: DescribeWorkspaceDirectoriesFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DescribeWorkspaceDirectoriesFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DescribeWorkspaceDirectoriesFilterName value: {data!r}"
        )
    return cast(DescribeWorkspaceDirectoriesFilterName, data)
