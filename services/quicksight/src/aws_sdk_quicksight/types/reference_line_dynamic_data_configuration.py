"""Generated from Smithy shape ``com.amazonaws.quicksight#ReferenceLineDynamicDataConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_function
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.numerical_aggregation_function


class ReferenceLineDynamicDataConfiguration(TypedDict):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that the dynamic data targets.</p>"""
    measure_aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function that is used in the dynamic data.</p>"""
    calculation: "aws_sdk_quicksight.types.numerical_aggregation_function.NumericalAggregationFunction"
    """<p>The calculation that is used in the dynamic data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReferenceLineDynamicDataConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    if "measure_aggregation_function" in value:
        import aws_sdk_quicksight.types.aggregation_function

        out["MeasureAggregationFunction"] = (
            aws_sdk_quicksight.types.aggregation_function.serialize_json(
                value["measure_aggregation_function"]
            )
        )
    import aws_sdk_quicksight.types.numerical_aggregation_function

    out["Calculation"] = (
        aws_sdk_quicksight.types.numerical_aggregation_function.serialize_json(
            value["calculation"]
        )
    )
    return out


def deserialize_json(data: dict) -> ReferenceLineDynamicDataConfiguration:
    out: ReferenceLineDynamicDataConfiguration = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError(
            "ReferenceLineDynamicDataConfiguration.column required"
        )
    if "MeasureAggregationFunction" in data:
        import aws_sdk_quicksight.types.aggregation_function

        out["measure_aggregation_function"] = (
            aws_sdk_quicksight.types.aggregation_function.deserialize_json(
                data["MeasureAggregationFunction"]
            )
        )
    if "Calculation" in data:
        import aws_sdk_quicksight.types.numerical_aggregation_function

        out["calculation"] = (
            aws_sdk_quicksight.types.numerical_aggregation_function.deserialize_json(
                data["Calculation"]
            )
        )
    else:
        raise DeserializationError(
            "ReferenceLineDynamicDataConfiguration.calculation required"
        )
    return out
