"""Generated from Smithy shape ``com.amazonaws.mailmanager#SnsNotificationEncoding``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

SnsNotificationEncoding: TypeAlias = Literal[
    "UTF-8",
    "BASE64",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "UTF-8",
        "BASE64",
    )
)


def serialize_aws_json_1_0(value: SnsNotificationEncoding) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> SnsNotificationEncoding:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SnsNotificationEncoding value: {data!r}")
    return cast(SnsNotificationEncoding, data)
