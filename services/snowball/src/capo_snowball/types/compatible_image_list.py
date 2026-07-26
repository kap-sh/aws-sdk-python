"""Generated from Smithy shape ``com.amazonaws.snowball#CompatibleImageList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_snowball.types.compatible_image

CompatibleImageList: TypeAlias = list[
    "capo_snowball.types.compatible_image.CompatibleImage"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CompatibleImageList) -> list:
    import capo_snowball.types.compatible_image

    out: list = []
    for item in value:
        out.append(capo_snowball.types.compatible_image.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CompatibleImageList:
    import capo_snowball.types.compatible_image

    out: CompatibleImageList = []
    for item in data:
        out.append(capo_snowball.types.compatible_image.deserialize_aws_json_1_1(item))
    return out
