"""Generated from Smithy shape ``com.amazonaws.comprehend#ListEventsDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.events_detection_job_properties_list
    import aws_sdk_comprehend.types.string


class ListEventsDetectionJobsResponse(TypedDict, closed=True):
    events_detection_job_properties_list: NotRequired[
        "aws_sdk_comprehend.types.events_detection_job_properties_list.EventsDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListEventsDetectionJobsResponse) -> dict:
    out: dict = {}
    if "events_detection_job_properties_list" in value:
        import aws_sdk_comprehend.types.events_detection_job_properties_list

        out["EventsDetectionJobPropertiesList"] = (
            aws_sdk_comprehend.types.events_detection_job_properties_list.serialize_aws_json_1_1(
                value["events_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListEventsDetectionJobsResponse:
    out: ListEventsDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if "EventsDetectionJobPropertiesList" in data:
        import aws_sdk_comprehend.types.events_detection_job_properties_list

        out["events_detection_job_properties_list"] = (
            aws_sdk_comprehend.types.events_detection_job_properties_list.deserialize_aws_json_1_1(
                data["EventsDetectionJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
