"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#ManagedWorkgroupStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_redshift_serverless.errors import DeserializationError

ManagedWorkgroupStatus: TypeAlias = Literal[
    "CREATING",
    "DELETING",
    "MODIFYING",
    "AVAILABLE",
    "NOT_AVAILABLE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "DELETING",
        "MODIFYING",
        "AVAILABLE",
        "NOT_AVAILABLE",
    )
)


def serialize_aws_json_1_1(value: ManagedWorkgroupStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ManagedWorkgroupStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedWorkgroupStatus value: {data!r}")
    return cast(ManagedWorkgroupStatus, data)
