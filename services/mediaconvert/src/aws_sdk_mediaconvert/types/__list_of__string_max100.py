"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__stringMax100``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_max100

__listOf__stringMax100: TypeAlias = list[
    "aws_sdk_mediaconvert.types.__string_max100.__stringMax100"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMax100) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMax100:
    return list(data)
