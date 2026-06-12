"""Generated from Smithy shape ``com.amazonaws.mediaconvert#__listOf__doubleMinNegative60Max6``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_mediaconvert.types.__double_min_negative60_max6

__listOf__doubleMinNegative60Max6: TypeAlias = list[
    "aws_sdk_mediaconvert.types.__double_min_negative60_max6.__doubleMinNegative60Max6"
]


# --- restJson1 ser/de ---
def serialize_json(value: __listOf__doubleMinNegative60Max6) -> list:
    return list(value)


def deserialize_json(data: list) -> __listOf__doubleMinNegative60Max6:
    return list(data)
