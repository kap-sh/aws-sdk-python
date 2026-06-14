"""Generated from Smithy shape ``com.amazonaws.storagegateway#ActiveDirectoryStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_storage_gateway.errors import DeserializationError

ActiveDirectoryStatus: TypeAlias = Literal[
    "ACCESS_DENIED",
    "DETACHED",
    "JOINED",
    "JOINING",
    "NETWORK_ERROR",
    "TIMEOUT",
    "UNKNOWN_ERROR",
    "INSUFFICIENT_PERMISSIONS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCESS_DENIED",
        "DETACHED",
        "JOINED",
        "JOINING",
        "NETWORK_ERROR",
        "TIMEOUT",
        "UNKNOWN_ERROR",
        "INSUFFICIENT_PERMISSIONS",
    )
)


def serialize_aws_json_1_1(value: ActiveDirectoryStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ActiveDirectoryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActiveDirectoryStatus value: {data!r}")
    return cast(ActiveDirectoryStatus, data)
