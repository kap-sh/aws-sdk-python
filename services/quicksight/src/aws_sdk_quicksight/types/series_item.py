"""Generated from Smithy shape ``com.amazonaws.quicksight#SeriesItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_field_series_item
    import aws_sdk_quicksight.types.field_series_item


class SeriesItem(TypedDict):
    field_series_item: NotRequired[
        "aws_sdk_quicksight.types.field_series_item.FieldSeriesItem"
    ]
    """<p>The field series item configuration of a line chart.</p>"""
    data_field_series_item: NotRequired[
        "aws_sdk_quicksight.types.data_field_series_item.DataFieldSeriesItem"
    ]
    """<p>The data field series item configuration of a line chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SeriesItem) -> dict:
    out: dict = {}
    if "field_series_item" in value:
        import aws_sdk_quicksight.types.field_series_item

        out["FieldSeriesItem"] = (
            aws_sdk_quicksight.types.field_series_item.serialize_json(
                value["field_series_item"]
            )
        )
    if "data_field_series_item" in value:
        import aws_sdk_quicksight.types.data_field_series_item

        out["DataFieldSeriesItem"] = (
            aws_sdk_quicksight.types.data_field_series_item.serialize_json(
                value["data_field_series_item"]
            )
        )
    return out


def deserialize_json(data: dict) -> SeriesItem:
    out: SeriesItem = {}  # type: ignore[typeddict-item]
    if "FieldSeriesItem" in data:
        import aws_sdk_quicksight.types.field_series_item

        out["field_series_item"] = (
            aws_sdk_quicksight.types.field_series_item.deserialize_json(
                data["FieldSeriesItem"]
            )
        )
    if "DataFieldSeriesItem" in data:
        import aws_sdk_quicksight.types.data_field_series_item

        out["data_field_series_item"] = (
            aws_sdk_quicksight.types.data_field_series_item.deserialize_json(
                data["DataFieldSeriesItem"]
            )
        )
    return out
