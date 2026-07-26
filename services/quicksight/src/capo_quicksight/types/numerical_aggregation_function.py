"""Generated from Smithy shape ``com.amazonaws.quicksight#NumericalAggregationFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.percentile_aggregation
    import capo_quicksight.types.simple_numerical_aggregation_function


class NumericalAggregationFunction(TypedDict, closed=True):
    simple_numerical_aggregation: NotRequired[
        "capo_quicksight.types.simple_numerical_aggregation_function.SimpleNumericalAggregationFunction"
    ]
    """<p>Built-in aggregation functions for numerical values.</p> <ul> <li> <p> <code>SUM</code>: The sum of a dimension or measure. </p> </li> <li> <p> <code>AVERAGE</code>: The average of a dimension or measure.</p> </li> <li> <p> <code>MIN</code>: The minimum value of a dimension or measure.</p> </li> <li> <p> <code>MAX</code>: The maximum value of a dimension or measure.</p> </li> <li> <p> <code>COUNT</code>: The count of a dimension or measure.</p> </li> <li> <p> <code>DISTINCT_COUNT</code>: The count of distinct values in a dimension or measure.</p> </li> <li> <p> <code>VAR</code>: The variance of a dimension or measure.</p> </li> <li> <p> <code>VARP</code>: The partitioned variance of a dimension or measure.</p> </li> <li> <p> <code>STDEV</code>: The standard deviation of a dimension or measure.</p> </li> <li> <p> <code>STDEVP</code>: The partitioned standard deviation of a dimension or measure.</p> </li> <li> <p> <code>MEDIAN</code>: The median value of a dimension or measure.</p> </li> </ul>"""
    percentile_aggregation: NotRequired[
        "capo_quicksight.types.percentile_aggregation.PercentileAggregation"
    ]
    """<p>An aggregation based on the percentile of values in a dimension or measure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NumericalAggregationFunction) -> dict:
    out: dict = {}
    if "simple_numerical_aggregation" in value:
        import capo_quicksight.types.simple_numerical_aggregation_function

        out["SimpleNumericalAggregation"] = (
            capo_quicksight.types.simple_numerical_aggregation_function.serialize_json(
                value["simple_numerical_aggregation"]
            )
        )
    if "percentile_aggregation" in value:
        import capo_quicksight.types.percentile_aggregation

        out["PercentileAggregation"] = (
            capo_quicksight.types.percentile_aggregation.serialize_json(
                value["percentile_aggregation"]
            )
        )
    return out


def deserialize_json(data: dict) -> NumericalAggregationFunction:
    out: NumericalAggregationFunction = {}  # type: ignore[typeddict-item]
    if "SimpleNumericalAggregation" in data:
        import capo_quicksight.types.simple_numerical_aggregation_function

        out["simple_numerical_aggregation"] = (
            capo_quicksight.types.simple_numerical_aggregation_function.deserialize_json(
                data["SimpleNumericalAggregation"]
            )
        )
    if "PercentileAggregation" in data:
        import capo_quicksight.types.percentile_aggregation

        out["percentile_aggregation"] = (
            capo_quicksight.types.percentile_aggregation.deserialize_json(
                data["PercentileAggregation"]
            )
        )
    return out
