"""Generated from Smithy shape ``com.amazonaws.comprehend#TopicsDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.topics_detection_job_properties

TopicsDetectionJobPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.topics_detection_job_properties.TopicsDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TopicsDetectionJobPropertiesList) -> list:
    import aws_sdk_comprehend.types.topics_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.topics_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> TopicsDetectionJobPropertiesList:
    import aws_sdk_comprehend.types.topics_detection_job_properties

    out: TopicsDetectionJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.topics_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
