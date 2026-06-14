"""Generated from Smithy shape ``com.amazonaws.workspaces#TargetWorkspaceState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

TargetWorkspaceState: TypeAlias = Literal[
    "AVAILABLE",
    "ADMIN_MAINTENANCE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "ADMIN_MAINTENANCE",
    )
)


def serialize_aws_json_1_1(value: TargetWorkspaceState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetWorkspaceState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown TargetWorkspaceState value: {data!r}")
    return cast(TargetWorkspaceState, data)
