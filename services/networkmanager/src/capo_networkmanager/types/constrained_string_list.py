"""Generated from Smithy shape ``com.amazonaws.networkmanager#ConstrainedStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.constrained_string

ConstrainedStringList: TypeAlias = list[
    "capo_networkmanager.types.constrained_string.ConstrainedString"
]


# --- restJson1 ser/de ---
def serialize_json(value: ConstrainedStringList) -> list:
    return list(value)


def deserialize_json(data: list) -> ConstrainedStringList:
    return list(data)
