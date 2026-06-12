"""Generated from Smithy shape ``com.amazonaws.comprehend#KeyPhrasesDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.key_phrases_detection_job_properties

KeyPhrasesDetectionJobPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.key_phrases_detection_job_properties.KeyPhrasesDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyPhrasesDetectionJobPropertiesList) -> list:
    import aws_sdk_comprehend.types.key_phrases_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.key_phrases_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> KeyPhrasesDetectionJobPropertiesList:
    import aws_sdk_comprehend.types.key_phrases_detection_job_properties

    out: KeyPhrasesDetectionJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.key_phrases_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
