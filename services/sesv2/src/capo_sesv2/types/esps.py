"""Generated from Smithy shape ``com.amazonaws.sesv2#Esps``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.esp

Esps: TypeAlias = list["capo_sesv2.types.esp.Esp"]


# --- restJson1 ser/de ---
def serialize_json(value: Esps) -> list:
    return list(value)


def deserialize_json(data: list) -> Esps:
    return list(data)
