"""Generated from Smithy shape ``com.amazonaws.quicksight#CategoricalMeasureField``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.categorical_aggregation_function
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.field_id
    import aws_sdk_quicksight.types.string_format_configuration


class CategoricalMeasureField(TypedDict):
    field_id: "aws_sdk_quicksight.types.field_id.FieldId"
    """<p>The custom field ID.</p>"""
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that is used in the <code>CategoricalMeasureField</code>.</p>"""
    aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.categorical_aggregation_function.CategoricalAggregationFunction"
    ]
    """<p>The aggregation function of the measure field.</p>"""
    format_configuration: NotRequired[
        "aws_sdk_quicksight.types.string_format_configuration.StringFormatConfiguration"
    ]
    """<p>The format configuration of the field.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CategoricalMeasureField) -> dict:
    out: dict = {}
    out["FieldId"] = value["field_id"]
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "aggregation_function" in value:
        import aws_sdk_quicksight.types.categorical_aggregation_function

        out["AggregationFunction"] = (
            aws_sdk_quicksight.types.categorical_aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    if "format_configuration" in value:
        import aws_sdk_quicksight.types.string_format_configuration

        out["FormatConfiguration"] = (
            aws_sdk_quicksight.types.string_format_configuration.serialize_json(
                value["format_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> CategoricalMeasureField:
    out: CategoricalMeasureField = {}  # type: ignore[typeddict-item]
    if "FieldId" in data:
        out["field_id"] = data["FieldId"]
    else:
        raise DeserializationError("CategoricalMeasureField.field_id required")
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("CategoricalMeasureField.column required")
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.categorical_aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.categorical_aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    if "FormatConfiguration" in data:
        import aws_sdk_quicksight.types.string_format_configuration

        out["format_configuration"] = (
            aws_sdk_quicksight.types.string_format_configuration.deserialize_json(
                data["FormatConfiguration"]
            )
        )
    return out
