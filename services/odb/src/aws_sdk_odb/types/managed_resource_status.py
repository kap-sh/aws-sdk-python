"""Generated from Smithy shape ``com.amazonaws.odb#ManagedResourceStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_odb.errors import DeserializationError

ManagedResourceStatus: TypeAlias = Literal[
    "ENABLED",
    "ENABLING",
    "DISABLED",
    "DISABLING",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "ENABLING",
        "DISABLED",
        "DISABLING",
    )
)


def serialize_aws_json_1_0(value: ManagedResourceStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ManagedResourceStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ManagedResourceStatus value: {data!r}")
    return cast(ManagedResourceStatus, data)
