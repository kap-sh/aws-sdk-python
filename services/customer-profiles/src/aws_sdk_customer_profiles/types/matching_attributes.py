"""Generated from Smithy shape ``com.amazonaws.customerprofiles#MatchingAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.string1_to255

MatchingAttributes: TypeAlias = list[
    "aws_sdk_customer_profiles.types.string1_to255.string1To255"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchingAttributes) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchingAttributes:
    return list(data)
