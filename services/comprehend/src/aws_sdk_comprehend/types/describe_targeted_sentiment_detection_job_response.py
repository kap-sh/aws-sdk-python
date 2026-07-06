"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeTargetedSentimentDetectionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties


class DescribeTargetedSentimentDetectionJobResponse(TypedDict, closed=True):
    targeted_sentiment_detection_job_properties: NotRequired[
        "aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties.TargetedSentimentDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with a targeted sentiment detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeTargetedSentimentDetectionJobResponse,
) -> dict:
    out: dict = {}
    if "targeted_sentiment_detection_job_properties" in value:
        import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties

        out["TargetedSentimentDetectionJobProperties"] = (
            aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties.serialize_aws_json_1_1(
                value["targeted_sentiment_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeTargetedSentimentDetectionJobResponse:
    out: DescribeTargetedSentimentDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "TargetedSentimentDetectionJobProperties" in data:
        import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties

        out["targeted_sentiment_detection_job_properties"] = (
            aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties.deserialize_aws_json_1_1(
                data["TargetedSentimentDetectionJobProperties"]
            )
        )
    return out
