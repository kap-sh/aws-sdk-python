"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeEventsDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.events_detection_job_properties


class DescribeEventsDetectionJobResponse(TypedDict, closed=True):
    events_detection_job_properties: NotRequired[
        "aws_sdk_comprehend.types.events_detection_job_properties.EventsDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with an event detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeEventsDetectionJobResponse) -> dict:
    out: dict = {}
    if "events_detection_job_properties" in value:
        import aws_sdk_comprehend.types.events_detection_job_properties

        out["EventsDetectionJobProperties"] = (
            aws_sdk_comprehend.types.events_detection_job_properties.serialize_aws_json_1_1(
                value["events_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeEventsDetectionJobResponse:
    out: DescribeEventsDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "EventsDetectionJobProperties" in data:
        import aws_sdk_comprehend.types.events_detection_job_properties

        out["events_detection_job_properties"] = (
            aws_sdk_comprehend.types.events_detection_job_properties.deserialize_aws_json_1_1(
                data["EventsDetectionJobProperties"]
            )
        )
    return out
