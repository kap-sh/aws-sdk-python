"""Generated from Smithy shape ``com.amazonaws.sagemaker#BedrockCustomModelMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.string1024


class BedrockCustomModelMetadata(TypedDict, closed=True):
    arn: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p> The Amazon Resource Name (ARN) of the Amazon Bedrock custom model. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BedrockCustomModelMetadata) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BedrockCustomModelMetadata:
    out: BedrockCustomModelMetadata = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    return out
