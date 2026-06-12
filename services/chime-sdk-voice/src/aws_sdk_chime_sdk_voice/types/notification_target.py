"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#NotificationTarget``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_voice.errors import DeserializationError

NotificationTarget: TypeAlias = Literal[
    "EventBridge",
    "SNS",
    "SQS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "EventBridge",
        "SNS",
        "SQS",
    )
)


def serialize_json(value: NotificationTarget) -> str:
    return value


def deserialize_json(data: str) -> NotificationTarget:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationTarget value: {data!r}")
    return cast(NotificationTarget, data)
