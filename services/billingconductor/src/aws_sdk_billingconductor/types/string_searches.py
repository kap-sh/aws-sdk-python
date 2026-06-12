"""Generated from Smithy shape ``com.amazonaws.billingconductor#StringSearches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_billingconductor.types.string_search

StringSearches: TypeAlias = list[
    "aws_sdk_billingconductor.types.string_search.StringSearch"
]


# --- restJson1 ser/de ---
def serialize_json(value: StringSearches) -> list:
    import aws_sdk_billingconductor.types.string_search

    out: list = []
    for item in value:
        out.append(aws_sdk_billingconductor.types.string_search.serialize_json(item))
    return out


def deserialize_json(data: list) -> StringSearches:
    import aws_sdk_billingconductor.types.string_search

    out: StringSearches = []
    for item in data:
        out.append(aws_sdk_billingconductor.types.string_search.deserialize_json(item))
    return out
