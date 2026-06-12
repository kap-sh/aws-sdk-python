"""Generated from Smithy shape ``com.amazonaws.ecr#ImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr.types.image

ImageList: TypeAlias = list["aws_sdk_ecr.types.image.Image"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageList) -> list:
    import aws_sdk_ecr.types.image

    out: list = []
    for item in value:
        out.append(aws_sdk_ecr.types.image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageList:
    import aws_sdk_ecr.types.image

    out: ImageList = []
    for item in data:
        out.append(aws_sdk_ecr.types.image.deserialize_aws_json_1_1(item))
    return out
