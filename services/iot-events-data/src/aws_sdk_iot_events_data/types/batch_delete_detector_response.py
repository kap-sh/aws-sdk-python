"""Generated from Smithy shape ``com.amazonaws.ioteventsdata#BatchDeleteDetectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot_events_data.types.batch_delete_detector_error_entries


class BatchDeleteDetectorResponse(TypedDict):
    batch_delete_detector_error_entries: NotRequired[
        "aws_sdk_iot_events_data.types.batch_delete_detector_error_entries.BatchDeleteDetectorErrorEntries"
    ]
    """<p>A list of errors associated with the request, or an empty array (<code>[]</code>) if there are no errors. Each error entry contains a <code>messageId</code> that helps you identify the entry that failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchDeleteDetectorResponse) -> dict:
    out: dict = {}
    if "batch_delete_detector_error_entries" in value:
        import aws_sdk_iot_events_data.types.batch_delete_detector_error_entries

        out["batchDeleteDetectorErrorEntries"] = (
            aws_sdk_iot_events_data.types.batch_delete_detector_error_entries.serialize_json(
                value["batch_delete_detector_error_entries"]
            )
        )
    return out


def deserialize_json(data: dict) -> BatchDeleteDetectorResponse:
    out: BatchDeleteDetectorResponse = {}  # type: ignore[typeddict-item]
    if "batchDeleteDetectorErrorEntries" in data:
        import aws_sdk_iot_events_data.types.batch_delete_detector_error_entries

        out["batch_delete_detector_error_entries"] = (
            aws_sdk_iot_events_data.types.batch_delete_detector_error_entries.deserialize_json(
                data["batchDeleteDetectorErrorEntries"]
            )
        )
    return out
