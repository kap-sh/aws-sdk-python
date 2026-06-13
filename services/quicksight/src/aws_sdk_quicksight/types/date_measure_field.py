"""Generated from Smithy shape ``com.amazonaws.quicksight#DateMeasureField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.date_aggregation_function
    import aws_sdk_quicksight.types.date_time_format_configuration
    import aws_sdk_quicksight.types.field_id


class DateMeasureField(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>DateMeasureField</code>.</p>"""
    aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.date_aggregation_function.DateAggregationFunction"
    ]
    """<p>The aggregation function of the measure field.</p>"""
    format_configuration: NotRequired[
        "aws_sdk_quicksight.types.date_time_format_configuration.DateTimeFormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DateMeasureField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "aggregation_function" in value:
        import aws_sdk_quicksight.types.date_aggregation_function

        out["AggregationFunction"] = (
            aws_sdk_quicksight.types.date_aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    if "format_configuration" in value:
        import aws_sdk_quicksight.types.date_time_format_configuration

        out["FormatConfiguration"] = (
            aws_sdk_quicksight.types.date_time_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> DateMeasureField:
    out: DateMeasureField = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("DateMeasureField.field_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("DateMeasureField.column required")
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.date_aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.date_aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    if "FormatConfiguration" in data:
        import aws_sdk_quicksight.types.date_time_format_configuration

        out["format_configuration"] = (
            aws_sdk_quicksight.types.date_time_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out
