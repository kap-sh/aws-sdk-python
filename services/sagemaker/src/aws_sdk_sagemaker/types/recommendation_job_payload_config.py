"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobPayloadConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.recommendation_job_supported_content_types
    import aws_sdk_sagemaker.types.s3_uri


class RecommendationJobPayloadConfig(TypedDict):
    sample_payload_url: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).</p>"""
    supported_content_types: NotRequired[
        "aws_sdk_sagemaker.types.recommendation_job_supported_content_types.RecommendationJobSupportedContentTypes"
    ]
    """<p>The supported MIME types for the input data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobPayloadConfig) -> dict:
    out: dict = {}
    if "sample_payload_url" in value:
        out["SamplePayloadUrl"] = value["sample_payload_url"]
    if "supported_content_types" in value:
        import aws_sdk_sagemaker.types.recommendation_job_supported_content_types

        out["SupportedContentTypes"] = (
            aws_sdk_sagemaker.types.recommendation_job_supported_content_types.serialize_aws_json_1_1(
                value["supported_content_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobPayloadConfig:
    out: RecommendationJobPayloadConfig = {}  # type: ignore[typeddict-item]
    if "SamplePayloadUrl" in data:
        out["sample_payload_url"] = data["SamplePayloadUrl"]
    if "SupportedContentTypes" in data:
        import aws_sdk_sagemaker.types.recommendation_job_supported_content_types

        out["supported_content_types"] = (
            aws_sdk_sagemaker.types.recommendation_job_supported_content_types.deserialize_aws_json_1_1(
                data["SupportedContentTypes"]
            )
        )
    return out
