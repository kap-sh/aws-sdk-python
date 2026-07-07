"""Generated from Smithy shape ``com.amazonaws.quicksight#TotalAggregationFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.simple_total_aggregation_function


class TotalAggregationFunction(TypedDict, closed=True):
    simple_total_aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.simple_total_aggregation_function.SimpleTotalAggregationFunction"
    ]
    """<p>A built in aggregation function for total values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TotalAggregationFunction) -> dict:
    out: dict = {}
    if "simple_total_aggregation_function" in value:
        import aws_sdk_quicksight.types.simple_total_aggregation_function

        out["SimpleTotalAggregationFunction"] = (
            aws_sdk_quicksight.types.simple_total_aggregation_function.serialize_json(
                value["simple_total_aggregation_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> TotalAggregationFunction:
    out: TotalAggregationFunction = {}  # type: ignore[typeddict-item]
    if "SimpleTotalAggregationFunction" in data:
        import aws_sdk_quicksight.types.simple_total_aggregation_function

        out["simple_total_aggregation_function"] = (
            aws_sdk_quicksight.types.simple_total_aggregation_function.deserialize_json(
                data["SimpleTotalAggregationFunction"]
            )
        )
    return out
