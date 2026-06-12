"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchUpdateDetectorErrorEntries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.batch_update_detector_error_entry

BatchUpdateDetectorErrorEntries: TypeAlias = list[
    "aws_sdk_iot_events_data.types.batch_update_detector_error_entry.BatchUpdateDetectorErrorEntry"
]


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDetectorErrorEntries) -> list:
    import aws_sdk_iot_events_data.types.batch_update_detector_error_entry

    out: list = []
    for item in value:
        out.append(
            aws_sdk_iot_events_data.types.batch_update_detector_error_entry.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> BatchUpdateDetectorErrorEntries:
    import aws_sdk_iot_events_data.types.batch_update_detector_error_entry

    out: BatchUpdateDetectorErrorEntries = []
    for item in data:
        out.append(
            aws_sdk_iot_events_data.types.batch_update_detector_error_entry.deserialize_json(
                item
            )
        )
    return out
