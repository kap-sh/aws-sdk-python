"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspacesPoolState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkspacesPoolState: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "RUNNING",
    "STARTING",
    "STOPPED",
    "STOPPING",
    "UPDATING",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "RUNNING",
        "STARTING",
        "STOPPED",
        "STOPPING",
        "UPDATING",
    )
)


def serialize_aws_json_1_1(value: WorkspacesPoolState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspacesPoolState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspacesPoolState value: {data!r}")
    return cast(WorkspacesPoolState, data)
