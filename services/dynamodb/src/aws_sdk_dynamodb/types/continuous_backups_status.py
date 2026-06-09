"""Generated from Smithy shape ``com.amazonaws.dynamodb#ContinuousBackupsStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_dynamodb.errors import DeserializationError

ContinuousBackupsStatus: TypeAlias = Literal[
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


def serialize_aws_json_1_0(value: ContinuousBackupsStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> ContinuousBackupsStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContinuousBackupsStatus value: {data!r}")
    return cast(ContinuousBackupsStatus, data)
