"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkspaceBundleState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkspaceBundleState: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "ERROR",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "PENDING",
        "ERROR",
    )
)


def serialize_aws_json_1_1(value: WorkspaceBundleState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkspaceBundleState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkspaceBundleState value: {data!r}")
    return cast(WorkspaceBundleState, data)
