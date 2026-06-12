"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfId3Insertion``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.id3_insertion

__listOfId3Insertion: TypeAlias = list[
    "aws_sdk_mediaconvert.types.id3_insertion.Id3Insertion"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfId3Insertion) -> list:
    import aws_sdk_mediaconvert.types.id3_insertion

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.id3_insertion.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfId3Insertion:
    import aws_sdk_mediaconvert.types.id3_insertion

    out: __listOfId3Insertion = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.id3_insertion.deserialize_json(item))
    return out
