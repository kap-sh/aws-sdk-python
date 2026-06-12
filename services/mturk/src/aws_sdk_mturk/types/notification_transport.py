"""Generated from Smithy shape ``com.amazonaws.mturk#NotificationTransport``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mturk.errors import DeserializationError

NotificationTransport: TypeAlias = Literal[
    "Email",
    "SQS",
    "SNS",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Email",
        "SQS",
        "SNS",
    )
)


def serialize_aws_json_1_1(value: NotificationTransport) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> NotificationTransport:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationTransport value: {data!r}")
    return cast(NotificationTransport, data)
