"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceDirectoryState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkspaceDirectoryState: TypeAlias = Literal[
    "REGISTERING",
    "REGISTERED",
    "DEREGISTERING",
    "DEREGISTERED",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "REGISTERING",
        "REGISTERED",
        "DEREGISTERING",
        "DEREGISTERED",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: WorkspaceDirectoryState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceDirectoryState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspaceDirectoryState value: {data!r}")
    return cast(WorkspaceDirectoryState, data)
