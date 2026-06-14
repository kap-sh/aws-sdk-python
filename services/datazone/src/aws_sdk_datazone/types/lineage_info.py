"""Generated from Smithy shape ``com.amazonaws.datazone#LineageInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.lineage_event_error_message
    import aws_sdk_datazone.types.lineage_event_processing_status


class LineageInfo(TypedDict):
    event_id: NotRequired["str"]
    """<p>The data lineage event ID.</p>"""
    event_status: NotRequired[
        "aws_sdk_datazone.types.lineage_event_processing_status.LineageEventProcessingStatus"
    ]
    """<p>The data lineage event status.</p>"""
    error_message: NotRequired[
        "aws_sdk_datazone.types.lineage_event_error_message.LineageEventErrorMessage"
    ]
    """<p>The data lineage error message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineageInfo) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_status" in value:
        import aws_sdk_datazone.types.lineage_event_processing_status

        out["eventStatus"] = (
            aws_sdk_datazone.types.lineage_event_processing_status.serialize_json(
                value["event_status"]
            )
        )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> LineageInfo:
    out: LineageInfo = {}  # type: ignore[typeddict-item]
    if "eventId" in data:
        out["event_id"] = data["eventId"]
    if "eventStatus" in data:
        import aws_sdk_datazone.types.lineage_event_processing_status

        out["event_status"] = (
            aws_sdk_datazone.types.lineage_event_processing_status.deserialize_json(
                data["eventStatus"]
            )
        )
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    return out
