"""Generated from Smithy shape ``com.amazonaws.quicksight#DataFieldSeriesItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.axis_binding
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.line_chart_series_settings
    import aws_sdk_quicksight.types.sensitive_string


class DataFieldSeriesItem(TypedDict, closed=True):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The field ID of the field that you are setting the axis binding to.</p>"""
    field_value: NotRequired[
        "aws_sdk_quicksight.types.sensitive_string.SensitiveString"
    ]
    """<p>The field value of the field that you are setting the axis binding to.</p>"""
    axis_binding: "aws_sdk_quicksight.types.axis_binding.AxisBinding"
    """<p>The axis that you are binding the field to.</p>"""
    settings: NotRequired[
        "aws_sdk_quicksight.types.line_chart_series_settings.LineChartSeriesSettings"
    ]
    """<p>The options that determine the presentation of line series associated to the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataFieldSeriesItem) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    if "field_value" in value:
        out["FieldValue"] = value["field_value"]
    import aws_sdk_quicksight.types.axis_binding

    out["AxisBinding"] = aws_sdk_quicksight.types.axis_binding.serialize_json(
        value["axis_binding"]
    )
    if "settings" in value:
        import aws_sdk_quicksight.types.line_chart_series_settings

        out["Settings"] = (
            aws_sdk_quicksight.types.line_chart_series_settings.serialize_json(
                value["settings"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataFieldSeriesItem:
    out: DataFieldSeriesItem = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("DataFieldSeriesItem.field_id required")
    if "FieldValue" in data:
        out["field_value"] = data["FieldValue"]
    if "AxisBinding" in data:
        import aws_sdk_quicksight.types.axis_binding

        out["axis_binding"] = aws_sdk_quicksight.types.axis_binding.deserialize_json(
            data["AxisBinding"]
        )
    else:
        raise DeserializationError("DataFieldSeriesItem.axis_binding required")
    if "Settings" in data:
        import aws_sdk_quicksight.types.line_chart_series_settings

        out["settings"] = (
            aws_sdk_quicksight.types.line_chart_series_settings.deserialize_json(
                data["Settings"]
            )
        )
    return out
