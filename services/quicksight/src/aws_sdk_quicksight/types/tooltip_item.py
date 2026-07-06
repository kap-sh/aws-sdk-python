"""Generated from Smithy shape ``com.amazonaws.quicksight#TooltipItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_tooltip_item
    import aws_sdk_quicksight.types.field_tooltip_item


class TooltipItem(TypedDict, closed=True):
    field_tooltip_item: NotRequired[
        "aws_sdk_quicksight.types.field_tooltip_item.FieldTooltipItem"
    ]
    """<p>The tooltip item for the fields.</p>"""
    column_tooltip_item: NotRequired[
        "aws_sdk_quicksight.types.column_tooltip_item.ColumnTooltipItem"
    ]
    """<p>The tooltip item for the columns that are not part of a field well.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TooltipItem) -> dict:
    out: dict = {}
    if "field_tooltip_item" in value:
        import aws_sdk_quicksight.types.field_tooltip_item

        out["FieldTooltipItem"] = (
            aws_sdk_quicksight.types.field_tooltip_item.serialize_json(
                value["field_tooltip_item"]
            )
        )
    if "column_tooltip_item" in value:
        import aws_sdk_quicksight.types.column_tooltip_item

        out["ColumnTooltipItem"] = (
            aws_sdk_quicksight.types.column_tooltip_item.serialize_json(
                value["column_tooltip_item"]
            )
        )
    return out


def deserialize_json(data: dict) -> TooltipItem:
    out: TooltipItem = {}  # type: ignore[typeddict-item]
    if "FieldTooltipItem" in data:
        import aws_sdk_quicksight.types.field_tooltip_item

        out["field_tooltip_item"] = (
            aws_sdk_quicksight.types.field_tooltip_item.deserialize_json(
                data["FieldTooltipItem"]
            )
        )
    if "ColumnTooltipItem" in data:
        import aws_sdk_quicksight.types.column_tooltip_item

        out["column_tooltip_item"] = (
            aws_sdk_quicksight.types.column_tooltip_item.deserialize_json(
                data["ColumnTooltipItem"]
            )
        )
    return out
