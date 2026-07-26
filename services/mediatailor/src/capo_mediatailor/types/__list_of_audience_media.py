"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfAudienceMedia``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.audience_media

__listOfAudienceMedia: TypeAlias = list[
    "capo_mediatailor.types.audience_media.AudienceMedia"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAudienceMedia) -> list:
    import capo_mediatailor.types.audience_media

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.audience_media.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAudienceMedia:
    import capo_mediatailor.types.audience_media

    out: __listOfAudienceMedia = []
    for item in data:
        out.append(capo_mediatailor.types.audience_media.deserialize_json(item))
    return out
