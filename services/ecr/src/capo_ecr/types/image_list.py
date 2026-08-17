"""Generated from Smithy shape ``com.amazonaws.ecr#ImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecr.types.image

ImageList: TypeAlias = list["capo_ecr.types.image.Image"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageList) -> list:
    import capo_ecr.types.image

    out: list = []
    for item in value:
        out.append(capo_ecr.types.image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageList:
    import capo_ecr.types.image

    out: ImageList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecr.types.image.deserialize_aws_json_1_1(item))
    return out
