"""Generated from Smithy shape ``com.amazonaws.quicksight#TablePathElementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_path_element

TablePathElementList: TypeAlias = list[
    "aws_sdk_quicksight.types.table_path_element.TablePathElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: TablePathElementList) -> list:
    import aws_sdk_quicksight.types.table_path_element

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.table_path_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> TablePathElementList:
    import aws_sdk_quicksight.types.table_path_element

    out: TablePathElementList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.table_path_element.deserialize_json(item))
    return out
