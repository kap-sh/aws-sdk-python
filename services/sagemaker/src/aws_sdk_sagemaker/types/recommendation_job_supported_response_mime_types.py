"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobSupportedResponseMIMETypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_supported_response_mime_type

RecommendationJobSupportedResponseMIMETypes: TypeAlias = list[
    "aws_sdk_sagemaker.types.recommendation_job_supported_response_mime_type.RecommendationJobSupportedResponseMIMEType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobSupportedResponseMIMETypes) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> RecommendationJobSupportedResponseMIMETypes:
    return list(data)
