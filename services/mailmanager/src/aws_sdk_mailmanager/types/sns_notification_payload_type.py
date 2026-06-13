"""Generated from Smithy shape ``com.amazonaws.mailmanager#SnsNotificationPayloadType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

SnsNotificationPayloadType: TypeAlias = Literal[
    "HEADERS",
    "CONTENT",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HEADERS",
        "CONTENT",
    )
)


def serialize_aws_json_1_0(value: SnsNotificationPayloadType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SnsNotificationPayloadType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SnsNotificationPayloadType value: {data!r}"
        )
    return cast(SnsNotificationPayloadType, data)
