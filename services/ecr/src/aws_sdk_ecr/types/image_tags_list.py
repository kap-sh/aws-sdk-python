"""Generated from Smithy shape ``com.amazonaws.ecr#ImageTagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image_tag

ImageTagsList: TypeAlias = list["aws_sdk_ecr.types.image_tag.ImageTag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagsList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ImageTagsList:
    return list(data)
