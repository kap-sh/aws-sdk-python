"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__integer``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__integer

__listOf__integer: TypeAlias = list["aws_sdk_mediaconvert.types.__integer.__integer"]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__integer) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__integer:
    return list(data)
