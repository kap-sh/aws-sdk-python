"""Generated from Smithy shape ``com.amazonaws.medialive#__listOfCaptionDescription``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_medialive.types.caption_description

__listOfCaptionDescription: TypeAlias = list[
    "capo_medialive.types.caption_description.CaptionDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfCaptionDescription) -> list:
    import capo_medialive.types.caption_description

    out: list = []
    for item in value:
        out.append(capo_medialive.types.caption_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfCaptionDescription:
    import capo_medialive.types.caption_description

    out: __listOfCaptionDescription = []
    for item in data:
        out.append(capo_medialive.types.caption_description.deserialize_json(item))
    return out
