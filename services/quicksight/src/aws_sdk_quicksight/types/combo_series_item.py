"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboSeriesItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_field_combo_series_item
    import aws_sdk_quicksight.types.field_combo_series_item


class ComboSeriesItem(TypedDict):
    field_combo_series_item: NotRequired[
        "aws_sdk_quicksight.types.field_combo_series_item.FieldComboSeriesItem"
    ]
    """<p>The field series item configuration of a <code>ComboChartVisual</code>.</p>"""
    data_field_combo_series_item: NotRequired[
        "aws_sdk_quicksight.types.data_field_combo_series_item.DataFieldComboSeriesItem"
    ]
    """<p>The data field series item configuration of a <code>ComboChartVisual</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboSeriesItem) -> dict:
    out: dict = {}
    if "field_combo_series_item" in value:
        import aws_sdk_quicksight.types.field_combo_series_item

        out["FieldComboSeriesItem"] = (
            aws_sdk_quicksight.types.field_combo_series_item.serialize_json(
                value["field_combo_series_item"]
            )
        )
    if "data_field_combo_series_item" in value:
        import aws_sdk_quicksight.types.data_field_combo_series_item

        out["DataFieldComboSeriesItem"] = (
            aws_sdk_quicksight.types.data_field_combo_series_item.serialize_json(
                value["data_field_combo_series_item"]
            )
        )
    return out


def deserialize_json(data: dict) -> ComboSeriesItem:
    out: ComboSeriesItem = {}  # type: ignore[typeddict-item]
    if "FieldComboSeriesItem" in data:
        import aws_sdk_quicksight.types.field_combo_series_item

        out["field_combo_series_item"] = (
            aws_sdk_quicksight.types.field_combo_series_item.deserialize_json(
                data["FieldComboSeriesItem"]
            )
        )
    if "DataFieldComboSeriesItem" in data:
        import aws_sdk_quicksight.types.data_field_combo_series_item

        out["data_field_combo_series_item"] = (
            aws_sdk_quicksight.types.data_field_combo_series_item.deserialize_json(
                data["DataFieldComboSeriesItem"]
            )
        )
    return out
