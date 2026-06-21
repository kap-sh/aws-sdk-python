"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#PushNotificationType``."""

from typing import Literal, TypeAlias, cast

PushNotificationType: TypeAlias = Literal[
    "DEFAULT",
    "VOIP",
]


# --- restJson1 ser/de ---
def serialize_json(value: PushNotificationType) -> str:
    return value


def deserialize_json(data: str) -> PushNotificationType:
    return cast(PushNotificationType, data)
