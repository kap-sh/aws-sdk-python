"""Generated from Smithy shape ``com.amazonaws.lakeformation#TableObjectList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_lakeformation.types.table_object

TableObjectList: TypeAlias = list["capo_lakeformation.types.table_object.TableObject"]


# --- restJson1 ser/de ---
def serialize_json(value: TableObjectList) -> list:
    import capo_lakeformation.types.table_object

    out: list = []
    for item in value:
        out.append(capo_lakeformation.types.table_object.serialize_json(item))
    return out


def deserialize_json(data: list) -> TableObjectList:
    import capo_lakeformation.types.table_object

    out: TableObjectList = []
    for item in data:
        out.append(capo_lakeformation.types.table_object.deserialize_json(item))
    return out
