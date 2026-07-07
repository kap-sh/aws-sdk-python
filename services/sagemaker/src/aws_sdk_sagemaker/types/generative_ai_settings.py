"""Generated from Smithy shape ``com.amazonaws.sagemaker#GenerativeAiSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.role_arn


class GenerativeAiSettings(TypedDict, closed=True):
    amazon_bedrock_role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of an Amazon Web Services IAM role that allows fine-tuning of large language models (LLMs) in Amazon Bedrock. The IAM role should have Amazon S3 read and write permissions, as well as a trust relationship that establishes <code>bedrock.amazonaws.com</code> as a service principal.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GenerativeAiSettings) -> dict:
    out: dict = {}
    if "amazon_bedrock_role_arn" in value:
        out["AmazonBedrockRoleArn"] = value["amazon_bedrock_role_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GenerativeAiSettings:
    out: GenerativeAiSettings = {}  # type: ignore[typeddict-item]
    if "AmazonBedrockRoleArn" in data:
        out["amazon_bedrock_role_arn"] = data["AmazonBedrockRoleArn"]
    return out
