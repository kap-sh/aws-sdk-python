"""Generated from Smithy shape ``com.amazonaws.connectcontactlens#MatchedCategories``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect_contact_lens.types.category_name

MatchedCategories: TypeAlias = list[
    "aws_sdk_connect_contact_lens.types.category_name.CategoryName"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchedCategories) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchedCategories:
    return list(data)
