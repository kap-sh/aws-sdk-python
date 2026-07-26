"""Generated from Smithy shape ``com.amazonaws.guardduty#Sources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

Sources: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: Sources) -> list:
    return list(value)


def deserialize_json(data: list) -> Sources:
    return list(data)
