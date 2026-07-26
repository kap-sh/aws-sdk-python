"""Generated from Smithy shape ``com.amazonaws.guardduty#Matches``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_guardduty.types.match

Matches: TypeAlias = list["capo_guardduty.types.match.Match"]


# --- restJson1 ser/de ---
def serialize_json(value: Matches) -> list:
    return list(value)


def deserialize_json(data: list) -> Matches:
    return list(data)
