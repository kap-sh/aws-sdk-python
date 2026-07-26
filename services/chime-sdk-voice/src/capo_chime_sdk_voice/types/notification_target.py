"""Generated from Smithy shape ``com.amazonaws.chimesdkvoice#NotificationTarget``."""

from typing import Literal, TypeAlias, cast

NotificationTarget: TypeAlias = Literal[
    "EventBridge",
    "SNS",
    "SQS",
]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationTarget) -> str:
    return value


def deserialize_json(data: str) -> NotificationTarget:
    return cast(NotificationTarget, data)
