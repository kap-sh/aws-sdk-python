"""Generated from Smithy shape ``com.amazonaws.quicksight#DataFieldBarSeriesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.bar_chart_series_settings
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.sensitive_string


class DataFieldBarSeriesItem(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>Field ID of the field that you are setting the series configuration for.</p>"""
    field_value: NotRequired[
        "aws_sdk_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>Field value of the field that you are setting the series configuration for.</p>"""
    settings: NotRequired[
        "aws_sdk_quicksight.types.bar_chart_series_settings.BarChartSeriesSettings"
    ]
    """<p>Options that determine the presentation of bar series associated to the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataFieldBarSeriesItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    if "settings" in value:
        import aws_sdk_quicksight.types.bar_chart_series_settings

        out["Settings"] = (
            aws_sdk_quicksight.types.bar_chart_series_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataFieldBarSeriesItem:
    out: DataFieldBarSeriesItem = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("DataFieldBarSeriesItem.field_id required")
    if "FieldValue" in data:
        out["field_value"] = data["FieldValue"]
    if "Settings" in data:
        import aws_sdk_quicksight.types.bar_chart_series_settings

        out["settings"] = (
            aws_sdk_quicksight.types.bar_chart_series_settings.deserialize_json(
                data["Settings"]
            )
        )
    return out
