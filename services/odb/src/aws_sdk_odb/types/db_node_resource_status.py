"""Generated from Smithy shape ``com.amazonaws.odb#DbNodeResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

DbNodeResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "FAILED",
    "PROVISIONING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
    "STOPPING",
    "STOPPED",
    "STARTING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AVAILABLE",
        "FAILED",
        "PROVISIONING",
        "TERMINATED",
        "TERMINATING",
        "UPDATING",
        "STOPPING",
        "STOPPED",
        "STARTING",
    )
)


def serialize_aws_json_1_0(value: DbNodeResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DbNodeResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DbNodeResourceStatus value: {data!r}")
    return cast(DbNodeResourceStatus, data)
