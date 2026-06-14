"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectoryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkspaceDirectoryType: TypeAlias = Literal[
    "SIMPLE_AD",
    "AD_CONNECTOR",
    "CUSTOMER_MANAGED",
    "AWS_IAM_IDENTITY_CENTER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SIMPLE_AD",
        "AD_CONNECTOR",
        "CUSTOMER_MANAGED",
        "AWS_IAM_IDENTITY_CENTER",
    )
)


def serialize_aws_json_1_1(value: WorkspaceDirectoryType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceDirectoryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspaceDirectoryType value: {data!r}")
    return cast(WorkspaceDirectoryType, data)
