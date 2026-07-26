"""Generated from Smithy shape ``com.amazonaws.macie2#Cells``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_macie2.types.cell

Cells: TypeAlias = list["capo_macie2.types.cell.Cell"]


# --- restJson1 ser/de ---
def serialize_json(value: Cells) -> list:
    import capo_macie2.types.cell

    out: list = []
    for item in value:
        out.append(capo_macie2.types.cell.serialize_json(item))
    return out


def deserialize_json(data: list) -> Cells:
    import capo_macie2.types.cell

    out: Cells = []
    for item in data:
        out.append(capo_macie2.types.cell.deserialize_json(item))
    return out
