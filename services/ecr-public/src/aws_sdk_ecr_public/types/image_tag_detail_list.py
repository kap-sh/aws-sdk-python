"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageTagDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecr_public.types.image_tag_detail

ImageTagDetailList: TypeAlias = list[
    "aws_sdk_ecr_public.types.image_tag_detail.ImageTagDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagDetailList) -> list:
    import aws_sdk_ecr_public.types.image_tag_detail

    out: list = []
    for item in value:
        out.append(
            aws_sdk_ecr_public.types.image_tag_detail.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ImageTagDetailList:
    import aws_sdk_ecr_public.types.image_tag_detail

    out: ImageTagDetailList = []
    for item in data:
        out.append(
            aws_sdk_ecr_public.types.image_tag_detail.deserialize_aws_json_1_1(item)
        )
    return out
