"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#Rows``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.row

Rows: TypeAlias = list["capo_iottwinmaker.types.row.Row"]


# --- restJson1 ser/de ---
def serialize_json(value: Rows) -> list:
    import capo_iottwinmaker.types.row

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.row.serialize_json(item))
    return out


def deserialize_json(data: list) -> Rows:
    import capo_iottwinmaker.types.row

    out: Rows = []
    for item in data:
        out.append(capo_iottwinmaker.types.row.deserialize_json(item))
    return out
