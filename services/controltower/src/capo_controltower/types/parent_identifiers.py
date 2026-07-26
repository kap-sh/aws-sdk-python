"""Generated from Smithy shape ``com.amazonaws.controltower#ParentIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.parent_identifier

ParentIdentifiers: TypeAlias = list[
    "capo_controltower.types.parent_identifier.ParentIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ParentIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> ParentIdentifiers:
    return list(data)
