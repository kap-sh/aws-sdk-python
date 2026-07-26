"""Generated from Smithy shape ``com.amazonaws.quicksight#TablePathElementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_quicksight.types.table_path_element

TablePathElementList: TypeAlias = list[
    "capo_quicksight.types.table_path_element.TablePathElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: TablePathElementList) -> list:
    import capo_quicksight.types.table_path_element

    out: list = []
    for item in value:
        out.append(capo_quicksight.types.table_path_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> TablePathElementList:
    import capo_quicksight.types.table_path_element

    out: TablePathElementList = []
    for item in data:
        out.append(capo_quicksight.types.table_path_element.deserialize_json(item))
    return out
