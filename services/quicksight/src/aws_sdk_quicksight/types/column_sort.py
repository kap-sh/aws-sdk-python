"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSort``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.aggregation_function
    import aws_sdk_quicksight.types.column_identifier
    import aws_sdk_quicksight.types.sort_direction


class ColumnSort(TypedDict):
    sort_by: "aws_sdk_quicksight.types.column_identifier.ColumnIdentifier"
    direction: "aws_sdk_quicksight.types.sort_direction.SortDirection"
    """<p>The sort direction.</p>"""
    aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.aggregation_function.AggregationFunction"
    ]
    """<p>The aggregation function that is defined in the column sort.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSort) -> dict:
    out: dict = {}
    import aws_sdk_quicksight.types.column_identifier

    out["SortBy"] = aws_sdk_quicksight.types.column_identifier.serialize_json(
        value["sort_by"]
    )
    import aws_sdk_quicksight.types.sort_direction

    out["Direction"] = aws_sdk_quicksight.types.sort_direction.serialize_json(
        value["direction"]
    )
    if "aggregation_function" in value:
        import aws_sdk_quicksight.types.aggregation_function

        out["AggregationFunction"] = (
            aws_sdk_quicksight.types.aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnSort:
    out: ColumnSort = {}  # type: ignore[typeddict-item]
    if "SortBy" in data:
        import aws_sdk_quicksight.types.column_identifier

        out["sort_by"] = aws_sdk_quicksight.types.column_identifier.deserialize_json(
            data["SortBy"]
        )
    else:
        raise DeserializationError("ColumnSort.sort_by required")
    if "Direction" in data:
        import aws_sdk_quicksight.types.sort_direction

        out["direction"] = aws_sdk_quicksight.types.sort_direction.deserialize_json(
            data["Direction"]
        )
    else:
        raise DeserializationError("ColumnSort.direction required")
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    return out
