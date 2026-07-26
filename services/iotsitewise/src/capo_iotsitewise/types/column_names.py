"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ColumnNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotsitewise.types.column_name

ColumnNames: TypeAlias = list["capo_iotsitewise.types.column_name.ColumnName"]


# --- restJson1 ser/de ---
def serialize_json(value: ColumnNames) -> list:
    import capo_iotsitewise.types.column_name

    out: list = []
    for item in value:
        out.append(capo_iotsitewise.types.column_name.serialize_json(item))
    return out


def deserialize_json(data: list) -> ColumnNames:
    import capo_iotsitewise.types.column_name

    out: ColumnNames = []
    for item in data:
        out.append(capo_iotsitewise.types.column_name.deserialize_json(item))
    return out
