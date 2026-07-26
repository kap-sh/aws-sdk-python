"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageTagDetailList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr_public.types.image_tag_detail

ImageTagDetailList: TypeAlias = list[
    "capo_ecr_public.types.image_tag_detail.ImageTagDetail"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagDetailList) -> list:
    import capo_ecr_public.types.image_tag_detail

    out: list = []
    for item in value:
        out.append(capo_ecr_public.types.image_tag_detail.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageTagDetailList:
    import capo_ecr_public.types.image_tag_detail

    out: ImageTagDetailList = []
    for item in data:
        out.append(
            capo_ecr_public.types.image_tag_detail.deserialize_aws_json_1_1(item)
        )
    return out
