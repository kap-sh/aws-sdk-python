"""Generated from Smithy shape ``com.amazonaws.inspector2#Cwes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_inspector2.types.cwe

Cwes: TypeAlias = list["capo_inspector2.types.cwe.Cwe"]


# --- restJson1 ser/de ---
def serialize_json(value: Cwes) -> list:
    return list(value)


def deserialize_json(data: list) -> Cwes:
    return list(data)
