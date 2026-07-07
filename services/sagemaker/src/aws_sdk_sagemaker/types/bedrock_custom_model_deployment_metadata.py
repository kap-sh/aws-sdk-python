"""Generated from Smithy shape ``com.amazonaws.sagemaker#BedrockCustomModelDeploymentMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string1024


class BedrockCustomModelDeploymentMetadata(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p> The Amazon Resource Name (ARN) for the Amazon Bedrock custom model deployment. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BedrockCustomModelDeploymentMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BedrockCustomModelDeploymentMetadata:
    out: BedrockCustomModelDeploymentMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
