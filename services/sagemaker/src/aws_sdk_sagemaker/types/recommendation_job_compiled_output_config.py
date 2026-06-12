"""Generated from Smithy shape ``com.amazonaws.sagemaker#RecommendationJobCompiledOutputConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_uri


class RecommendationJobCompiledOutputConfig(TypedDict):
    s3_output_uri: NotRequired["aws_sdk_sagemaker.types.s3_uri.S3Uri"]
    """<p>Identifies the Amazon S3 bucket where you want SageMaker to store the compiled model artifacts.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RecommendationJobCompiledOutputConfig) -> dict:
    out: dict = {}
    if "s3_output_uri" in value:
        out["S3OutputUri"] = value["s3_output_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RecommendationJobCompiledOutputConfig:
    out: RecommendationJobCompiledOutputConfig = {}  # type: ignore[typeddict-item]
    if "S3OutputUri" in data:
        out["s3_output_uri"] = data["S3OutputUri"]
    return out
