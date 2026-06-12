"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__stringMin1``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__string_min1

__listOf__stringMin1: TypeAlias = list[
    "aws_sdk_mediaconvert.types.__string_min1.__stringMin1"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__stringMin1) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__stringMin1:
    return list(data)
