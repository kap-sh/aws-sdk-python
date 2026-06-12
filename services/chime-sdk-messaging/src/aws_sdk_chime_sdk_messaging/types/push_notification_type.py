"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PushNotificationType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime_sdk_messaging.errors import DeserializationError

PushNotificationType: TypeAlias = Literal[
    "DEFAULT",
    "VOIP",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "VOIP",
    )
)


def serialize_json(value: PushNotificationType) -> str:
    return value


def deserialize_json(data: str) -> PushNotificationType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PushNotificationType value: {data!r}")
    return cast(PushNotificationType, data)
