"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobSupportedContentTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_supported_content_type

RecommendationJobSupportedContentTypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.recommendation_job_supported_content_type.RecommendationJobSupportedContentType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobSupportedContentTypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RecommendationJobSupportedContentTypes:
    return list(data)
