"""Generated from Smithy shape ``com.amazonaws.quicksight#DataPrepAggregationFunction``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_prep_list_aggregation_function
    import aws_sdk_quicksight.types.data_prep_simple_aggregation_function


class DataPrepAggregationFunction(TypedDict, closed=True):
    simple_aggregation: NotRequired[
        "aws_sdk_quicksight.types.data_prep_simple_aggregation_function.DataPrepSimpleAggregationFunction"
    ]
    """<p>A simple aggregation function such as <code>SUM</code>, <code>COUNT</code>, <code>AVERAGE</code>, <code>MIN</code>, <code>MAX</code>, <code>MEDIAN</code>, <code>VARIANCE</code>, or <code>STANDARD_DEVIATION</code>.</p>"""
    list_aggregation: NotRequired[
        "aws_sdk_quicksight.types.data_prep_list_aggregation_function.DataPrepListAggregationFunction"
    ]
    """<p>A list aggregation function that concatenates values from multiple rows into a single delimited string.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrepAggregationFunction) -> dict:
    out: dict = {}
    if "simple_aggregation" in value:
        import aws_sdk_quicksight.types.data_prep_simple_aggregation_function

        out["SimpleAggregation"] = (
            aws_sdk_quicksight.types.data_prep_simple_aggregation_function.serialize_json(
                value["simple_aggregation"]
            )
        )
    if "list_aggregation" in value:
        import aws_sdk_quicksight.types.data_prep_list_aggregation_function

        out["ListAggregation"] = (
            aws_sdk_quicksight.types.data_prep_list_aggregation_function.serialize_json(
                value["list_aggregation"]
            )
        )
    return out


def deserialize_json(data: dict) -> DataPrepAggregationFunction:
    out: DataPrepAggregationFunction = {}  # type: ignore[typeddict-item]
    if "SimpleAggregation" in data:
        import aws_sdk_quicksight.types.data_prep_simple_aggregation_function

        out["simple_aggregation"] = (
            aws_sdk_quicksight.types.data_prep_simple_aggregation_function.deserialize_json(
                data["SimpleAggregation"]
            )
        )
    if "ListAggregation" in data:
        import aws_sdk_quicksight.types.data_prep_list_aggregation_function

        out["list_aggregation"] = (
            aws_sdk_quicksight.types.data_prep_list_aggregation_function.deserialize_json(
                data["ListAggregation"]
            )
        )
    return out
