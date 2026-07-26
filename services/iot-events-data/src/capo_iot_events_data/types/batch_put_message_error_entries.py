"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchPutMessageErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.batch_put_message_error_entry

BatchPutMessageErrorEntries: TypeAlias = list[
    "capo_iot_events_data.types.batch_put_message_error_entry.BatchPutMessageErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutMessageErrorEntries) -> list:
    import capo_iot_events_data.types.batch_put_message_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_iot_events_data.types.batch_put_message_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchPutMessageErrorEntries:
    import capo_iot_events_data.types.batch_put_message_error_entry

    out: BatchPutMessageErrorEntries = []
    for item in data:
        out.append(
            capo_iot_events_data.types.batch_put_message_error_entry.deserialize_json(
                item
            )
        )
    return out
