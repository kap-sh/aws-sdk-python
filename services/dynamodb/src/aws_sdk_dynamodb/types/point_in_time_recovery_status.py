"""Generated from Smithy shape ``com.amazonaws.dynamodb#PointInTimeRecoveryStatus``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_dynamodb.errors import DeserializationError

PointInTimeRecoveryStatus: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ENABLED",
        "DISABLED",
    )
)


def serialize_aws_json_1_0(value: PointInTimeRecoveryStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PointInTimeRecoveryStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PointInTimeRecoveryStatus value: {data!r}")
    return cast(PointInTimeRecoveryStatus, data)
