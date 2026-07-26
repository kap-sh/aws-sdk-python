"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#ColumnDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iottwinmaker.types.column_description

ColumnDescriptions: TypeAlias = list[
    "capo_iottwinmaker.types.column_description.ColumnDescription"
]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnDescriptions) -> list:
    import capo_iottwinmaker.types.column_description

    out: list = []
    for item in value:
        out.append(capo_iottwinmaker.types.column_description.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnDescriptions:
    import capo_iottwinmaker.types.column_description

    out: ColumnDescriptions = []
    for item in data:
        out.append(capo_iottwinmaker.types.column_description.deserialize_json(item))
    return out
