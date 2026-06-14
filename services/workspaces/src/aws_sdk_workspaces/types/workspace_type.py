"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkspaceType: TypeAlias = Literal[
    "PERSONAL",
    "POOLS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERSONAL",
        "POOLS",
    )
)


def serialize_aws_json_1_1(value: WorkspaceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspaceType value: {data!r}")
    return cast(WorkspaceType, data)
