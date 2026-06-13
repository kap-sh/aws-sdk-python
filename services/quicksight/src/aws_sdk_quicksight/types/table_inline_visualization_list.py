"""Generated from Smithy shape ``com.amazonaws.quicksight#TableInlineVisualizationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.table_inline_visualization

TableInlineVisualizationList: TypeAlias = list[
    "aws_sdk_quicksight.types.table_inline_visualization.TableInlineVisualization"
]


# --- restJson1 ser/de ---
def serialize_json(value: TableInlineVisualizationList) -> list:
    import aws_sdk_quicksight.types.table_inline_visualization

    out: list = []
    for item in value:
        out.append(
            aws_sdk_quicksight.types.table_inline_visualization.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> TableInlineVisualizationList:
    import aws_sdk_quicksight.types.table_inline_visualization

    out: TableInlineVisualizationList = []
    for item in data:
        out.append(
            aws_sdk_quicksight.types.table_inline_visualization.deserialize_json(item)
        )
    return out
