"""Generated from Smithy shape ``com.amazonaws.quicksight#FieldBarSeriesItem``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.bar_chart_series_settings
    import aws_sdk_quicksight.types.field_id


class FieldBarSeriesItem(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>Field ID of the field for which you are setting the series configuration.</p>"""
    settings: NotRequired[
        "aws_sdk_quicksight.types.bar_chart_series_settings.BarChartSeriesSettings"
    ]
    """<p>Options that determine the presentation of bar series associated to the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FieldBarSeriesItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "settings" in value:
        import aws_sdk_quicksight.types.bar_chart_series_settings

        out["Settings"] = (
            aws_sdk_quicksight.types.bar_chart_series_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> FieldBarSeriesItem:
    out: FieldBarSeriesItem = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("FieldBarSeriesItem.field_id required")
    if "Settings" in data:
        import aws_sdk_quicksight.types.bar_chart_series_settings

        out["settings"] = (
            aws_sdk_quicksight.types.bar_chart_series_settings.deserialize_json(
                data["Settings"]
            )
        )
    return out
