"""Generated from Smithy shape ``com.amazonaws.ecrpublic#ImageTagList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr_public.types.image_tag

ImageTagList: TypeAlias = list["capo_ecr_public.types.image_tag.ImageTag"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageTagList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ImageTagList:
    return list(data)
