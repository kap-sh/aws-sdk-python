"""Generated from Smithy shape ``com.amazonaws.guardduty#Neq``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

Neq: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Neq) -> list:
    return list(value)


def deserialize_json(data: list) -> Neq:
    return list(data)
