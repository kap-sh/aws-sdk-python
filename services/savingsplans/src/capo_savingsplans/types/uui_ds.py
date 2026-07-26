"""Generated from Smithy shape ``com.amazonaws.savingsplans#UUIDs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_savingsplans.types.uuid

UUIDs: TypeAlias = list["capo_savingsplans.types.uuid.UUID"]


# --- restJson1 ser/de ---
def serialize_json(value: UUIDs) -> list:
    return list(value)


def deserialize_json(data: list) -> UUIDs:
    return list(data)
