"""Generated from Smithy shape ``com.amazonaws.connect#NotificationDeliveryType``."""

from typing import Literal, TypeAlias, cast

NotificationDeliveryType: TypeAlias = Literal["EMAIL",]


# --- restJson1 ser/de ---
def serialize_json(value: NotificationDeliveryType) -> str:
    return value


def deserialize_json(data: str) -> NotificationDeliveryType:
    return cast(NotificationDeliveryType, data)
