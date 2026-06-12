"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeployedImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.deployed_image

DeployedImages: TypeAlias = list["aws_sdk_sagemaker.types.deployed_image.DeployedImage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeployedImages) -> list:
    import aws_sdk_sagemaker.types.deployed_image

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.deployed_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> DeployedImages:
    import aws_sdk_sagemaker.types.deployed_image

    out: DeployedImages = []
    for item in data:
        out.append(
            aws_sdk_sagemaker.types.deployed_image.deserialize_aws_json_1_1(item)
        )
    return out
