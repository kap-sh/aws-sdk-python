"""Generated from Smithy shape ``com.amazonaws.comprehend#TargetedSentimentDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties

TargetedSentimentDetectionJobPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties.TargetedSentimentDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetedSentimentDetectionJobPropertiesList) -> list:
    import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TargetedSentimentDetectionJobPropertiesList:
    import aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties

    out: TargetedSentimentDetectionJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.targeted_sentiment_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
