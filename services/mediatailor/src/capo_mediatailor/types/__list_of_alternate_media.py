"""Generated from Smithy shape ``com.amazonaws.mediatailor#__listOfAlternateMedia``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediatailor.types.alternate_media

__listOfAlternateMedia: TypeAlias = list[
    "capo_mediatailor.types.alternate_media.AlternateMedia"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfAlternateMedia) -> list:
    import capo_mediatailor.types.alternate_media

    out: list = []
    for item in value:
        out.append(capo_mediatailor.types.alternate_media.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfAlternateMedia:
    import capo_mediatailor.types.alternate_media

    out: __listOfAlternateMedia = []
    for item in data:
        out.append(capo_mediatailor.types.alternate_media.deserialize_json(item))
    return out
