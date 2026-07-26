"""Generated from Smithy shape ``com.amazonaws.imagebuilder#SecurityGroupIds``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_imagebuilder.types.non_empty_string

SecurityGroupIds: TypeAlias = list[
    "capo_imagebuilder.types.non_empty_string.NonEmptyString"
]


# --- restJson1 ser/de ---
def serialize_json(value: SecurityGroupIds) -> list:
    return list(value)


def deserialize_json(data: list) -> SecurityGroupIds:
    return list(data)
