"""Generated from Smithy shape ``com.amazonaws.quicksight#BarSeriesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_field_bar_series_item
    import aws_sdk_quicksight.types.field_bar_series_item


class BarSeriesItem(TypedDict, closed=True):
    field_bar_series_item: NotRequired[
        "aws_sdk_quicksight.types.field_bar_series_item.FieldBarSeriesItem"
    ]
    """<p>The field series item configuration of a <code>BarChartVisual</code>.</p>"""
    data_field_bar_series_item: NotRequired[
        "aws_sdk_quicksight.types.data_field_bar_series_item.DataFieldBarSeriesItem"
    ]
    """<p>The data field series item configuration of a <code>BarChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarSeriesItem) -> dict:
    out: dict = {}
    if "field_bar_series_item" in value:
        import aws_sdk_quicksight.types.field_bar_series_item

        out["FieldBarSeriesItem"] = (
            aws_sdk_quicksight.types.field_bar_series_item.serialize_json(
                value["field_bar_series_item"]
            )
        )
    if "data_field_bar_series_item" in value:
        import aws_sdk_quicksight.types.data_field_bar_series_item

        out["DataFieldBarSeriesItem"] = (
            aws_sdk_quicksight.types.data_field_bar_series_item.serialize_json(
                value["data_field_bar_series_item"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarSeriesItem:
    out: BarSeriesItem = {}  # type: ignore[typeddict-item]
    if "FieldBarSeriesItem" in data:
        import aws_sdk_quicksight.types.field_bar_series_item

        out["field_bar_series_item"] = (
            aws_sdk_quicksight.types.field_bar_series_item.deserialize_json(
                data["FieldBarSeriesItem"]
            )
        )
    if "DataFieldBarSeriesItem" in data:
        import aws_sdk_quicksight.types.data_field_bar_series_item

        out["data_field_bar_series_item"] = (
            aws_sdk_quicksight.types.data_field_bar_series_item.deserialize_json(
                data["DataFieldBarSeriesItem"]
            )
        )
    return out
