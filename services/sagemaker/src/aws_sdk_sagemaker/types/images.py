"""Generated from Smithy shape ``com.amazonaws.sagemaker#Images``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image

Images: TypeAlias = list["aws_sdk_sagemaker.types.image.Image"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Images) -> list:
    import aws_sdk_sagemaker.types.image

    out: list = []
    for item in value:
        out.append(aws_sdk_sagemaker.types.image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Images:
    import aws_sdk_sagemaker.types.image

    out: Images = []
    for item in data:
        out.append(aws_sdk_sagemaker.types.image.deserialize_aws_json_1_1(item))
    return out
