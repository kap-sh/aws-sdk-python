"""Generated from Smithy shape ``com.amazonaws.comprehend#ListTopicsDetectionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.string
    import aws_sdk_comprehend.types.topics_detection_job_properties_list


class ListTopicsDetectionJobsResponse(TypedDict, closed=True):
    topics_detection_job_properties_list: NotRequired[
        "aws_sdk_comprehend.types.topics_detection_job_properties_list.TopicsDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTopicsDetectionJobsResponse) -> dict:
    out: dict = {}
    if "topics_detection_job_properties_list" in value:
        import aws_sdk_comprehend.types.topics_detection_job_properties_list

        out["TopicsDetectionJobPropertiesList"] = (
            aws_sdk_comprehend.types.topics_detection_job_properties_list.serialize_aws_json_1_1(
                value["topics_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTopicsDetectionJobsResponse:
    out: ListTopicsDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if "TopicsDetectionJobPropertiesList" in data:
        import aws_sdk_comprehend.types.topics_detection_job_properties_list

        out["topics_detection_job_properties_list"] = (
            aws_sdk_comprehend.types.topics_detection_job_properties_list.deserialize_aws_json_1_1(
                data["TopicsDetectionJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
