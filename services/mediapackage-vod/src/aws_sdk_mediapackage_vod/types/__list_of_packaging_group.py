"""Generated from Smithy shape ``com.amazonaws.mediapackagevod#__listOfPackagingGroup``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediapackage_vod.types.packaging_group

__listOfPackagingGroup: TypeAlias = list[
    "aws_sdk_mediapackage_vod.types.packaging_group.PackagingGroup"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfPackagingGroup) -> list:
    import aws_sdk_mediapackage_vod.types.packaging_group

    out: list = []
    for item in value:
        out.append(aws_sdk_mediapackage_vod.types.packaging_group.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfPackagingGroup:
    import aws_sdk_mediapackage_vod.types.packaging_group

    out: __listOfPackagingGroup = []
    for item in data:
        out.append(
            aws_sdk_mediapackage_vod.types.packaging_group.deserialize_json(item)
        )
    return out
