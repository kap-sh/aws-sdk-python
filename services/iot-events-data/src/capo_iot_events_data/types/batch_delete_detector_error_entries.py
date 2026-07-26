"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchDeleteDetectorErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot_events_data.types.batch_delete_detector_error_entry

BatchDeleteDetectorErrorEntries: TypeAlias = list[
    "capo_iot_events_data.types.batch_delete_detector_error_entry.BatchDeleteDetectorErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDetectorErrorEntries) -> list:
    import capo_iot_events_data.types.batch_delete_detector_error_entry

    out: list = []
    for item in value:
        out.append(
            capo_iot_events_data.types.batch_delete_detector_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchDeleteDetectorErrorEntries:
    import capo_iot_events_data.types.batch_delete_detector_error_entry

    out: BatchDeleteDetectorErrorEntries = []
    for item in data:
        out.append(
            capo_iot_events_data.types.batch_delete_detector_error_entry.deserialize_json(
                item
            )
        )
    return out
