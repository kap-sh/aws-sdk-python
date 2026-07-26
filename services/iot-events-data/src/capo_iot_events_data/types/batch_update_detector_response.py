"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchUpdateDetectorResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot_events_data.types.batch_update_detector_error_entries


class BatchUpdateDetectorResponse(TypedDict, closed=True):
    batch_update_detector_error_entries: NotRequired[
        "capo_iot_events_data.types.batch_update_detector_error_entries.BatchUpdateDetectorErrorEntries"
    ]
    """<p>A list of those detector updates that resulted in errors. (If an error is listed here, the specific update did not occur.)</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchUpdateDetectorResponse) -> dict:
    out: dict = {}
    if "batch_update_detector_error_entries" in value:
        import capo_iot_events_data.types.batch_update_detector_error_entries

        out["batchUpdateDetectorErrorEntries"] = (
            capo_iot_events_data.types.batch_update_detector_error_entries.serialize_json(
                value["batch_update_detector_error_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchUpdateDetectorResponse:
    out: BatchUpdateDetectorResponse = {}  # type: ignore[typeddict-item]
    if "batchUpdateDetectorErrorEntries" in data:
        import capo_iot_events_data.types.batch_update_detector_error_entries

        out["batch_update_detector_error_entries"] = (
            capo_iot_events_data.types.batch_update_detector_error_entries.deserialize_json(
                data["batchUpdateDetectorErrorEntries"]
            )
        )
    return out
