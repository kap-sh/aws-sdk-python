"""Generated from Smithy shape ``com.amazonaws.sagemaker#BedrockProvisionedModelThroughputMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string1024


class BedrockProvisionedModelThroughputMetadata(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p> The Amazon Resource Name (ARN) of the Amazon Bedrock provisioned model throughput. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BedrockProvisionedModelThroughputMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BedrockProvisionedModelThroughputMetadata:
    out: BedrockProvisionedModelThroughputMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
