"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfAlternateMedia``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.alternate_media

__listOfAlternateMedia: TypeAlias = list[
    "aws_sdk_mediatailor.types.alternate_media.AlternateMedia"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAlternateMedia) -> list:
    import aws_sdk_mediatailor.types.alternate_media

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.alternate_media.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAlternateMedia:
    import aws_sdk_mediatailor.types.alternate_media

    out: __listOfAlternateMedia = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.alternate_media.deserialize_json(item))
    return out
