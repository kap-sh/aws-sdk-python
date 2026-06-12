"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfAudienceMedia``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.audience_media

__listOfAudienceMedia: TypeAlias = list[
    "aws_sdk_mediatailor.types.audience_media.AudienceMedia"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudienceMedia) -> list:
    import aws_sdk_mediatailor.types.audience_media

    out: list = []
    for item in value:
        out.append(aws_sdk_mediatailor.types.audience_media.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudienceMedia:
    import aws_sdk_mediatailor.types.audience_media

    out: __listOfAudienceMedia = []
    for item in data:
        out.append(aws_sdk_mediatailor.types.audience_media.deserialize_json(item))
    return out
