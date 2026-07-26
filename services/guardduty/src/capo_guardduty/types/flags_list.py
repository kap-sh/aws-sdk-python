"""Generated from Smithy shape ``com.amazonaws.guardduty#FlagsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.string

FlagsList: TypeAlias = list["capo_guardduty.types.string.String"]


# --- restJson1 ser/de ---
def serialize_json(value: FlagsList) -> list:
    return list(value)


def deserialize_json(data: list) -> FlagsList:
    return list(data)
