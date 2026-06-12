"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfInputClipping``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.input_clipping

__listOfInputClipping: TypeAlias = list[
    "aws_sdk_mediaconvert.types.input_clipping.InputClipping"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInputClipping) -> list:
    import aws_sdk_mediaconvert.types.input_clipping

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.input_clipping.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInputClipping:
    import aws_sdk_mediaconvert.types.input_clipping

    out: __listOfInputClipping = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.input_clipping.deserialize_json(item))
    return out
