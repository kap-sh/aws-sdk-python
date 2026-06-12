"""Generated from Smithy shape ``com.amazonaws.rekognition#MediaAnalysisJobDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_rekognition.types.media_analysis_job_description

MediaAnalysisJobDescriptions: TypeAlias = list[
    "aws_sdk_rekognition.types.media_analysis_job_description.MediaAnalysisJobDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MediaAnalysisJobDescriptions) -> list:
    import aws_sdk_rekognition.types.media_analysis_job_description

    out: list = []
    for item in value:
        out.append(
            aws_sdk_rekognition.types.media_analysis_job_description.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> MediaAnalysisJobDescriptions:
    import aws_sdk_rekognition.types.media_analysis_job_description

    out: MediaAnalysisJobDescriptions = []
    for item in data:
        out.append(
            aws_sdk_rekognition.types.media_analysis_job_description.deserialize_aws_json_1_1(
                item
            )
        )
    return out
