"""Generated from Smithy shape ``com.amazonaws.connect#NotificationDeliveryType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

NotificationDeliveryType: TypeAlias = Literal["EMAIL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("EMAIL",))


def serialize_json(value: NotificationDeliveryType) -> str:
    return value


def deserialize_json(data: str) -> NotificationDeliveryType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown NotificationDeliveryType value: {data!r}")
    return cast(NotificationDeliveryType, data)
