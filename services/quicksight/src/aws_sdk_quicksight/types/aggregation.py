"""Generated from Smithy shape ``com.amazonaws.quicksight#Aggregation``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_id
    import aws_sdk_quicksight.types.column_name
    import aws_sdk_quicksight.types.data_prep_aggregation_function


class Aggregation(TypedDict):
    aggregation_function: "aws_sdk_quicksight.types.data_prep_aggregation_function.DataPrepAggregationFunction"
    """<p>The aggregation function to apply, such as <code>SUM</code>, <code>COUNT</code>, <code>AVERAGE</code>, <code>MIN</code>, <code>MAX</code> </p>"""
    new_column_name: "aws_sdk_quicksight.types.column_name.ColumnName"
    """<p>The name for the new column that will contain the aggregated values.</p>"""
    new_column_id: "aws_sdk_quicksight.types.column_id.ColumnId"
    """<p>A unique identifier for the new column that will contain the aggregated values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Aggregation) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.data_prep_aggregation_function

    out["AggregationFunction"] = (
        aws_sdk_quicksight.types.data_prep_aggregation_function.serialize_json(
            value["aggregation_function"]
        )
    )
    out["NewColumnName"] = value["new_column_name"]
    out["NewColumnId"] = value["new_column_id"]
    return out


def deserialize_json(data: dict) -> Aggregation:
    out: Aggregation = {}  # type: ignore[typeddict-item]
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.data_prep_aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.data_prep_aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    else:
        raise DeserializationError("Aggregation.aggregation_function required")
    if "NewColumnName" in data:
        out["new_column_name"] = data["NewColumnName"]
    else:
        raise DeserializationError("Aggregation.new_column_name required")
    if "NewColumnId" in data:
        out["new_column_id"] = data["NewColumnId"]
    else:
        raise DeserializationError("Aggregation.new_column_id required")
    return out
