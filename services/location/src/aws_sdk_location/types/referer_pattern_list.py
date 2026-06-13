"""Generated from Smithy shape ``com.amazonaws.location#RefererPatternList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_location.types.referer_pattern

RefererPatternList: TypeAlias = list[
    "aws_sdk_location.types.referer_pattern.RefererPattern"
]


# --- restJson1 ser/de ---
def serialize_json(value: RefererPatternList) -> list:
    return list(value)


def deserialize_json(data: list) -> RefererPatternList:
    return list(data)
