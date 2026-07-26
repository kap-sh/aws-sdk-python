"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobPayloadConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.recommendation_job_supported_content_types
    import capo_sagemaker.types.s3_uri


class RecommendationJobPayloadConfig(TypedDict, closed=True):
    sample_payload_url: NotRequired["capo_sagemaker.types.s3_uri.S3Uri"]
    """<p>The Amazon Simple Storage Service (Amazon S3) path where the sample payload is stored. This path must point to a single gzip compressed tar archive (.tar.gz suffix).</p>"""
    supported_content_types: NotRequired[
        "capo_sagemaker.types.recommendation_job_supported_content_types.RecommendationJobSupportedContentTypes"
    ]
    """<p>The supported MIME types for the input data.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobPayloadConfig) -> dict:
    out: dict = {}
    if "sample_payload_url" in value:
        out["SamplePayloadUrl"] = value["sample_payload_url"]
    if "supported_content_types" in value:
        import capo_sagemaker.types.recommendation_job_supported_content_types

        out["SupportedContentTypes"] = (
            capo_sagemaker.types.recommendation_job_supported_content_types.serialize_aws_json_1_1(
                value["supported_content_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobPayloadConfig:
    out: RecommendationJobPayloadConfig = {}  # type: ignore[typeddict-item]
    if "SamplePayloadUrl" in data:
        out["sample_payload_url"] = data["SamplePayloadUrl"]
    if "SupportedContentTypes" in data:
        import capo_sagemaker.types.recommendation_job_supported_content_types

        out["supported_content_types"] = (
            capo_sagemaker.types.recommendation_job_supported_content_types.deserialize_aws_json_1_1(
                data["SupportedContentTypes"]
            )
        )
    return out
