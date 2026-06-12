"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOfInput``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.input

__listOfInput: TypeAlias = list["aws_sdk_mediaconvert.types.input.Input"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOfInput) -> list:
    import aws_sdk_mediaconvert.types.input

    out: list = []
    for item in value:
        out.append(aws_sdk_mediaconvert.types.input.serialize_json(item))
    return out


def deserialize_json(data: list) -> __listOfInput:
    import aws_sdk_mediaconvert.types.input

    out: __listOfInput = []
    for item in data:
        out.append(aws_sdk_mediaconvert.types.input.deserialize_json(item))
    return out
