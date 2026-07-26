"""Generated from Smithy shape ``com.amazonaws.macie2#Ranges``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.range

Ranges: TypeAlias = list["capo_macie2.types.range.Range"]


# --- restJson1 ser/de ---
def serialize_json(value: Ranges) -> list:
    import capo_macie2.types.range

    out: list = []
    for item in value:
        out.append(capo_macie2.types.range.serialize_json(item))
    return out


def deserialize_json(data: list) -> Ranges:
    import capo_macie2.types.range

    out: Ranges = []
    for item in data:
        out.append(capo_macie2.types.range.deserialize_json(item))
    return out
