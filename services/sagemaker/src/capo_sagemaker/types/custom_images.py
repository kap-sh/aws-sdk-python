"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomImages``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.custom_image

CustomImages: TypeAlias = list["capo_sagemaker.types.custom_image.CustomImage"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomImages) -> list:
    import capo_sagemaker.types.custom_image

    out: list = []
    for item in value:
        out.append(capo_sagemaker.types.custom_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomImages:
    import capo_sagemaker.types.custom_image

    out: CustomImages = []
    for item in data:
        out.append(capo_sagemaker.types.custom_image.deserialize_aws_json_1_1(item))
    return out
