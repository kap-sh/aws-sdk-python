"""Generated from Smithy shape ``com.amazonaws.quicksight#GridLayoutElementList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.grid_layout_element

GridLayoutElementList: TypeAlias = list[
    "aws_sdk_quicksight.types.grid_layout_element.GridLayoutElement"
]


# --- restJson1 ser/de ---
def serialize_json(value: GridLayoutElementList) -> list:
    import aws_sdk_quicksight.types.grid_layout_element

    out: list = []
    for item in value:
        out.append(aws_sdk_quicksight.types.grid_layout_element.serialize_json(item))
    return out


def deserialize_json(data: list) -> GridLayoutElementList:
    import aws_sdk_quicksight.types.grid_layout_element

    out: GridLayoutElementList = []
    for item in data:
        out.append(aws_sdk_quicksight.types.grid_layout_element.deserialize_json(item))
    return out
