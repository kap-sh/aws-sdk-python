"""Generated from Smithy shape ``com.amazonaws.ecr#ImageDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image_detail

ImageDetailList: TypeAlias = list["capo_ecr.types.image_detail.ImageDetail"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageDetailList) -> list:
    import capo_ecr.types.image_detail

    out: list = []
    for item in value:
        out.append(capo_ecr.types.image_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageDetailList:
    import capo_ecr.types.image_detail

    out: ImageDetailList = []
    for item in data:
        out.append(capo_ecr.types.image_detail.deserialize_aws_json_1_1(item))
    return out
