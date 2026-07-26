"""Generated from Smithy shape ``com.amazonaws.iotevents#RecipientDetails``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events.types.recipient_detail

RecipientDetails: TypeAlias = list[
    "capo_iot_events.types.recipient_detail.RecipientDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: RecipientDetails) -> list:
    import capo_iot_events.types.recipient_detail

    out: list = []
    for item in value:
        out.append(capo_iot_events.types.recipient_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> RecipientDetails:
    import capo_iot_events.types.recipient_detail

    out: RecipientDetails = []
    for item in data:
        out.append(capo_iot_events.types.recipient_detail.deserialize_json(item))
    return out
