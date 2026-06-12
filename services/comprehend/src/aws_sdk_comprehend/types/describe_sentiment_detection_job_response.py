"""Generated from Smithy shape ``com.amazonaws.comprehend#DescribeSentimentDetectionJobResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.sentiment_detection_job_properties


class DescribeSentimentDetectionJobResponse(TypedDict):
    sentiment_detection_job_properties: NotRequired[
        "aws_sdk_comprehend.types.sentiment_detection_job_properties.SentimentDetectionJobProperties"
    ]
    """<p>An object that contains the properties associated with a sentiment detection job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeSentimentDetectionJobResponse) -> dict:
    out: dict = {}
    if "sentiment_detection_job_properties" in value:
        import aws_sdk_comprehend.types.sentiment_detection_job_properties

        out["SentimentDetectionJobProperties"] = (
            aws_sdk_comprehend.types.sentiment_detection_job_properties.serialize_aws_json_1_1(
                value["sentiment_detection_job_properties"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeSentimentDetectionJobResponse:
    out: DescribeSentimentDetectionJobResponse = {}  # type: ignore[typeddict-item]
    if "SentimentDetectionJobProperties" in data:
        import aws_sdk_comprehend.types.sentiment_detection_job_properties

        out["sentiment_detection_job_properties"] = (
            aws_sdk_comprehend.types.sentiment_detection_job_properties.deserialize_aws_json_1_1(
                data["SentimentDetectionJobProperties"]
            )
        )
    return out
