"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfThumbnailDetail``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_medialive.types.thumbnail_detail

__listOfThumbnailDetail: TypeAlias = list[
    "aws_sdk_medialive.types.thumbnail_detail.ThumbnailDetail"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfThumbnailDetail) -> list:
    import aws_sdk_medialive.types.thumbnail_detail

    out: list = []
    for item in value:
        out.append(aws_sdk_medialive.types.thumbnail_detail.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfThumbnailDetail:
    import aws_sdk_medialive.types.thumbnail_detail

    out: __listOfThumbnailDetail = []
    for item in data:
        out.append(aws_sdk_medialive.types.thumbnail_detail.deserialize_json(item))
    return out
