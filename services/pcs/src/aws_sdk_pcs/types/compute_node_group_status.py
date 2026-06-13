"""Generated from Smithy shape ``com.amazonaws.pcs#ComputeNodeGroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

ComputeNodeGroupStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
    "UPDATE_FAILED",
    "DELETED",
    "SUSPENDING",
    "SUSPENDED",
    "RESUMING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "ACTIVE",
        "UPDATING",
        "DELETING",
        "CREATE_FAILED",
        "DELETE_FAILED",
        "UPDATE_FAILED",
        "DELETED",
        "SUSPENDING",
        "SUSPENDED",
        "RESUMING",
    )
)


def serialize_aws_json_1_0(value: ComputeNodeGroupStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ComputeNodeGroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ComputeNodeGroupStatus value: {data!r}")
    return cast(ComputeNodeGroupStatus, data)
