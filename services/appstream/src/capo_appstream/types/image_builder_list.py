"""Generated from Smithy shape ``com.amazonaws.appstream#ImageBuilderList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appstream.types.image_builder

ImageBuilderList: TypeAlias = list["capo_appstream.types.image_builder.ImageBuilder"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBuilderList) -> list:
    import capo_appstream.types.image_builder

    out: list = []
    for item in value:
        out.append(capo_appstream.types.image_builder.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> ImageBuilderList:
    import capo_appstream.types.image_builder

    out: ImageBuilderList = []
    for item in data:
        out.append(capo_appstream.types.image_builder.deserialize_aws_json_1_1(item))
    return out
