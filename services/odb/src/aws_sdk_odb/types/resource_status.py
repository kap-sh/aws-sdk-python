"""Generated from Smithy shape ``com.amazonaws.odb#ResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

ResourceStatus: TypeAlias = Literal[
    "AVAILABLE",
    "FAILED",
    "PROVISIONING",
    "TERMINATED",
    "TERMINATING",
    "UPDATING",
    "MAINTENANCE_IN_PROGRESS",
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
        "MAINTENANCE_IN_PROGRESS",
    )
)


def serialize_aws_json_1_0(value: ResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ResourceStatus value: {data!r}")
    return cast(ResourceStatus, data)
