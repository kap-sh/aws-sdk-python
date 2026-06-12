"""Generated from Smithy shape ``com.amazonaws.cloudtrail#FederationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cloudtrail.errors import DeserializationError

FederationStatus: TypeAlias = Literal[
    "ENABLING",
    "ENABLED",
    "DISABLING",
    "DISABLED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLING",
        "ENABLED",
        "DISABLING",
        "DISABLED",
    )
)


def serialize_aws_json_1_1(value: FederationStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> FederationStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown FederationStatus value: {data!r}")
    return cast(FederationStatus, data)
