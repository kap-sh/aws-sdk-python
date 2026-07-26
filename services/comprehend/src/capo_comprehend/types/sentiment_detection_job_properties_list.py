"""Generated from Smithy shape ``com.amazonaws.comprehend#SentimentDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_comprehend.types.sentiment_detection_job_properties

SentimentDetectionJobPropertiesList: TypeAlias = list[
    "capo_comprehend.types.sentiment_detection_job_properties.SentimentDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SentimentDetectionJobPropertiesList) -> list:
    import capo_comprehend.types.sentiment_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            capo_comprehend.types.sentiment_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> SentimentDetectionJobPropertiesList:
    import capo_comprehend.types.sentiment_detection_job_properties

    out: SentimentDetectionJobPropertiesList = []
    for item in data:
        out.append(
            capo_comprehend.types.sentiment_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
