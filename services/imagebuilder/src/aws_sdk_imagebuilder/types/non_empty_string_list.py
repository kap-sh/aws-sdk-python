"""Generated from Smithy shape ``com.amazonaws.imagebuilder#NonEmptyStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string

NonEmptyStringList: TypeAlias = list[
    "aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: NonEmptyStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> NonEmptyStringList:
    return list(data)
