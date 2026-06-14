"""Generated from Smithy shape ``com.amazonaws.workspaces#WorkSpaceApplicationState``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_workspaces.errors import DeserializationError

WorkSpaceApplicationState: TypeAlias = Literal[
    "PENDING",
    "ERROR",
    "AVAILABLE",
    "UNINSTALL_ONLY",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PENDING",
        "ERROR",
        "AVAILABLE",
        "UNINSTALL_ONLY",
    )
)


def serialize_aws_json_1_1(value: WorkSpaceApplicationState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WorkSpaceApplicationState:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WorkSpaceApplicationState value: {data!r}")
    return cast(WorkSpaceApplicationState, data)
