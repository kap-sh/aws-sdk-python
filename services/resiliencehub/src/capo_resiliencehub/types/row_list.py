"""Generated from Smithy shape ``com.amazonaws.resiliencehub#RowList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_resiliencehub.types.row

RowList: TypeAlias = list["capo_resiliencehub.types.row.Row"]


# --- restJson1 ser/de ---
def serialize_json(value: RowList) -> list:
    import capo_resiliencehub.types.row

    out: list = []
    for item in value:
        out.append(capo_resiliencehub.types.row.serialize_json(item))
    return out


def deserialize_json(data: list) -> RowList:
    import capo_resiliencehub.types.row

    out: RowList = []
    for item in data:
        out.append(capo_resiliencehub.types.row.deserialize_json(item))
    return out
