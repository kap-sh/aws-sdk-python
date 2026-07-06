"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetDeleteEventsByEventTypeStatusResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_frauddetector.types.async_job_status
    import aws_sdk_frauddetector.types.identifier


class GetDeleteEventsByEventTypeStatusResult(TypedDict, closed=True):
    event_type_name: NotRequired["aws_sdk_frauddetector.types.identifier.identifier"]
    """<p>The event type name.</p>"""
    events_deletion_status: NotRequired[
        "aws_sdk_frauddetector.types.async_job_status.AsyncJobStatus"
    ]
    """<p>The deletion status.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDeleteEventsByEventTypeStatusResult) -> dict:
    out: dict = {}
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "events_deletion_status" in value:
        import aws_sdk_frauddetector.types.async_job_status

        out["eventsDeletionStatus"] = (
            aws_sdk_frauddetector.types.async_job_status.serialize_aws_json_1_1(
                value["events_deletion_status"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDeleteEventsByEventTypeStatusResult:
    out: GetDeleteEventsByEventTypeStatusResult = {}  # type: ignore[typeddict-item]
    if "eventTypeName" in data:
        out["event_type_name"] = data["eventTypeName"]
    if "eventsDeletionStatus" in data:
        import aws_sdk_frauddetector.types.async_job_status

        out["events_deletion_status"] = (
            aws_sdk_frauddetector.types.async_job_status.deserialize_aws_json_1_1(
                data["eventsDeletionStatus"]
            )
        )
    return out
