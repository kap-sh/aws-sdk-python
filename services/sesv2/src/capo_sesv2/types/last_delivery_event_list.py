"""Generated from Smithy shape ``com.amazonaws.sesv2#LastDeliveryEventList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.delivery_event_type

LastDeliveryEventList: TypeAlias = list[
    "capo_sesv2.types.delivery_event_type.DeliveryEventType"
]


# --- restJson1 ser/de ---
def serialize_json(value: LastDeliveryEventList) -> list:
    import capo_sesv2.types.delivery_event_type

    out: list = []
    for item in value:
        out.append(capo_sesv2.types.delivery_event_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> LastDeliveryEventList:
    import capo_sesv2.types.delivery_event_type

    out: LastDeliveryEventList = []
    for item in data:
        out.append(capo_sesv2.types.delivery_event_type.deserialize_json(item))
    return out
