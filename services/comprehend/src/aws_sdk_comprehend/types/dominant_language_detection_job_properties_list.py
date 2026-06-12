"""Generated from Smithy shape ``com.amazonaws.comprehend#DominantLanguageDetectionJobPropertiesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_comprehend.types.dominant_language_detection_job_properties

DominantLanguageDetectionJobPropertiesList: TypeAlias = list[
    "aws_sdk_comprehend.types.dominant_language_detection_job_properties.DominantLanguageDetectionJobProperties"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DominantLanguageDetectionJobPropertiesList) -> list:
    import aws_sdk_comprehend.types.dominant_language_detection_job_properties

    out: list = []
    for item in value:
        out.append(
            aws_sdk_comprehend.types.dominant_language_detection_job_properties.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> DominantLanguageDetectionJobPropertiesList:
    import aws_sdk_comprehend.types.dominant_language_detection_job_properties

    out: DominantLanguageDetectionJobPropertiesList = []
    for item in data:
        out.append(
            aws_sdk_comprehend.types.dominant_language_detection_job_properties.deserialize_aws_json_1_1(
                item
            )
        )
    return out
