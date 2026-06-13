"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationSortConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_function
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.sort_direction


class AggregationSortConfiguration(TypedDict):
    column: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    """<p>The column that determines the sort order of aggregated values.</p>"""
    sort_direction: "aws_sdk_quicksight.types.sort_direction.SortDirection"
    """<p>The sort direction of values.</p> <ul> <li> <p> <code>ASC</code>: Sort in ascending order.</p> </li> <li> <p> <code>DESC</code>: Sort in descending order.</p> </li> </ul>"""
    aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The function that aggregates the values in <code>Column</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationSortConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["Column"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["column"]
    )
    import aws_sdk_quicksight.types.sort_direction

    out["SortDirection"] = aws_sdk_quicksight.types.sort_direction.serialize_json(
        value["sort_direction"]
    )
    if "aggregation_function" in value:
        import aws_sdk_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            aws_sdk_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> AggregationSortConfiguration:
    out: AggregationSortConfiguration = {}  # type: ignore[typeddict-item]
    if "Column" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["column"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["Column"]
        )
    else:
        raise DeserializationError("AggregationSortConfiguration.column required")
    if "SortDirection" in data:
        import aws_sdk_quicksight.types.sort_direction

        out["sort_direction"] = (
            aws_sdk_quicksight.types.sort_direction.deserialize_json(
                data["SortDirection"]
            )
        )
    else:
        raise DeserializationError(
            "AggregationSortConfiguration.sort_direction required"
        )
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    return out
