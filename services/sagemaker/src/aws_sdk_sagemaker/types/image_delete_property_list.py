"""Generated from Smithy shape ``com.amazonaws.sagemaker#ImageDeletePropertyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.image_delete_property

ImageDeletePropertyList: TypeAlias = list[
    "aws_sdk_sagemaker.types.image_delete_property.ImageDeleteProperty"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageDeletePropertyList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ImageDeletePropertyList:
    return list(data)
