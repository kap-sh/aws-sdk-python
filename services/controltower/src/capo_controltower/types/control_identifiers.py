"""Generated from Smithy shape ``com.amazonaws.controltower#ControlIdentifiers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_controltower.types.control_identifier

ControlIdentifiers: TypeAlias = list[
    "capo_controltower.types.control_identifier.ControlIdentifier"
]


# --- restJson1 ser/de ---
def serialize_json(value: ControlIdentifiers) -> list:
    return list(value)


def deserialize_json(data: list) -> ControlIdentifiers:
    return list(data)
