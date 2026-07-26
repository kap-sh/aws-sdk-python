"""Generated from Smithy shape ``com.amazonaws.inspector2#ArchitectureList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.architecture

ArchitectureList: TypeAlias = list["capo_inspector2.types.architecture.Architecture"]


# --- restJson1 ser/de ---
def serialize_json(value: ArchitectureList) -> list:
    return list(value)


def deserialize_json(data: list) -> ArchitectureList:
    return list(data)
