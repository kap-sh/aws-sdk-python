"""Generated from Smithy shape ``com.amazonaws.inspector2#Targets``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.target

Targets: TypeAlias = list["capo_inspector2.types.target.Target"]


# --- restJson1 ser/de ---
def serialize_json(value: Targets) -> list:
    return list(value)


def deserialize_json(data: list) -> Targets:
    return list(data)
