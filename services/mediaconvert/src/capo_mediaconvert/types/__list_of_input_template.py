"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfInputTemplate``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mediaconvert.types.input_template

__listOfInputTemplate: TypeAlias = list[
    "capo_mediaconvert.types.input_template.InputTemplate"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputTemplate) -> list:
    import capo_mediaconvert.types.input_template

    out: list = []
    for item in value:
        out.append(capo_mediaconvert.types.input_template.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputTemplate:
    import capo_mediaconvert.types.input_template

    out: __listOfInputTemplate = []
    for item in data:
        out.append(capo_mediaconvert.types.input_template.deserialize_json(item))
    return out
