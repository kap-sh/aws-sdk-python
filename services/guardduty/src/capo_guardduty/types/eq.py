"""Generated from Smithy shape ``com.amazonaws.guardduty#Eq``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

Eq: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Eq) -> list:
    return list(value)


def deserialize_json(data: list) -> Eq:
    return list(data)
