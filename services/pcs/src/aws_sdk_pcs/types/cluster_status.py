"""Generated from Smithy shape ``com.amazonaws.pcs#ClusterStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

ClusterStatus: TypeAlias = Literal[
    "CREATING",
    "ACTIVE",
    "UPDATING",
    "DELETING",
    "CREATE_FAILED",
    "DELETE_FAILED",
    "UPDATE_FAILED",
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
        "SUSPENDING",
        "SUSPENDED",
        "RESUMING",
    )
)


def serialize_aws_json_1_0(value: ClusterStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ClusterStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ClusterStatus value: {data!r}")
    return cast(ClusterStatus, data)
