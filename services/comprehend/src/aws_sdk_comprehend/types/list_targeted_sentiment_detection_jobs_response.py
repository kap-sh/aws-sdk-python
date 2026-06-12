"""Generated from Smithy shape ``com.amazonaws.comprehend#ListTargetedSentimentDetectionJobsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.string
    import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties_list


class ListTargetedSentimentDetectionJobsResponse(TypedDict):
    targeted_sentiment_detection_job_properties_list: NotRequired[
        "aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties_list.TargetedSentimentDetectionJobPropertiesList"
    ]
    """<p>A list containing the properties of each job that is returned.</p>"""
    next_token: NotRequired["aws_sdk_comprehend.types.string.String"]
    """<p>Identifies the next page of results to return.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListTargetedSentimentDetectionJobsResponse) -> dict:
    out: dict = {}
    if "targeted_sentiment_detection_job_properties_list" in value:
        import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties_list

        out["TargetedSentimentDetectionJobPropertiesList"] = (
            aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties_list.serialize_aws_json_1_1(
                value["targeted_sentiment_detection_job_properties_list"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListTargetedSentimentDetectionJobsResponse:
    out: ListTargetedSentimentDetectionJobsResponse = {}  # type: ignore[typeddict-item]
    if "TargetedSentimentDetectionJobPropertiesList" in data:
        import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties_list

        out["targeted_sentiment_detection_job_properties_list"] = (
            aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties_list.deserialize_aws_json_1_1(
                data["TargetedSentimentDetectionJobPropertiesList"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
