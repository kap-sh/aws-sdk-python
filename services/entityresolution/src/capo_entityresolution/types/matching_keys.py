"""Generated from Smithy shape ``com.amazonaws.entityresolution#MatchingKeys``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_entityresolution.types.attribute_name

MatchingKeys: TypeAlias = list[
    "capo_entityresolution.types.attribute_name.AttributeName"
]


# --- restJson1 ser/de ---
def serialize_json(value: MatchingKeys) -> list:
    return list(value)


def deserialize_json(data: list) -> MatchingKeys:
    return list(data)
