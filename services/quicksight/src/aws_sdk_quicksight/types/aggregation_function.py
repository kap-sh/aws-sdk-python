"""Generated from Smithy shape ``com.amazonaws.quicksight#AggregationFunction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.attribute_aggregation_function
    import aws_sdk_quicksight.types.categorical_aggregation_function
    import aws_sdk_quicksight.types.date_aggregation_function
    import aws_sdk_quicksight.types.numerical_aggregation_function


class AggregationFunction(TypedDict):
    numerical_aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.numerical_aggregation_function.NumericalAggregationFunction"
    ]
    """<p>Aggregation for numerical values.</p>"""
    categorical_aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.categorical_aggregation_function.CategoricalAggregationFunction"
    ]
    """<p>Aggregation for categorical values.</p> <ul> <li> <p> <code>COUNT</code>: Aggregate by the total number of values, including duplicates.</p> </li> <li> <p> <code>DISTINCT_COUNT</code>: Aggregate by the total number of distinct values.</p> </li> </ul>"""
    date_aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.date_aggregation_function.DateAggregationFunction"
    ]
    """<p>Aggregation for date values.</p> <ul> <li> <p> <code>COUNT</code>: Aggregate by the total number of values, including duplicates.</p> </li> <li> <p> <code>DISTINCT_COUNT</code>: Aggregate by the total number of distinct values.</p> </li> <li> <p> <code>MIN</code>: Select the smallest date value.</p> </li> <li> <p> <code>MAX</code>: Select the largest date value.</p> </li> </ul>"""
    attribute_aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.attribute_aggregation_function.AttributeAggregationFunction"
    ]
    """<p>Aggregation for attributes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AggregationFunction) -> dict:
    out: dict = {}
    if "numerical_aggregation_function" in value:
        import aws_sdk_quicksight.types.numerical_aggregation_function

        out["NumericalAggregationFunction"] = (
            aws_sdk_quicksight.types.numerical_aggregation_function.serialize_json(
                value["numerical_aggregation_function"]
            )
        )
    if "categorical_aggregation_function" in value:
        import aws_sdk_quicksight.types.categorical_aggregation_function

        out["CategoricalAggregationFunction"] = (
            aws_sdk_quicksight.types.categorical_aggregation_function.serialize_json(
                value["categorical_aggregation_function"]
            )
        )
    if "date_aggregation_function" in value:
        import aws_sdk_quicksight.types.date_aggregation_function

        out["DateAggregationFunction"] = (
            aws_sdk_quicksight.types.date_aggregation_function.serialize_json(
                value["date_aggregation_function"]
            )
        )
    if "attribute_aggregation_function" in value:
        import aws_sdk_quicksight.types.attribute_aggregation_function

        out["AttributeAggregationFunction"] = (
            aws_sdk_quicksight.types.attribute_aggregation_function.serialize_json(
                value["attribute_aggregation_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> AggregationFunction:
    out: AggregationFunction = {}  # type: ignore[typeddict-item]
    if "NumericalAggregationFunction" in data:
        import aws_sdk_quicksight.types.numerical_aggregation_function

        out["numerical_aggregation_function"] = (
            aws_sdk_quicksight.types.numerical_aggregation_function.deserialize_json(
                data["NumericalAggregationFunction"]
            )
        )
    if "CategoricalAggregationFunction" in data:
        import aws_sdk_quicksight.types.categorical_aggregation_function

        out["categorical_aggregation_function"] = (
            aws_sdk_quicksight.types.categorical_aggregation_function.deserialize_json(
                data["CategoricalAggregationFunction"]
            )
        )
    if "DateAggregationFunction" in data:
        import aws_sdk_quicksight.types.date_aggregation_function

        out["date_aggregation_function"] = (
            aws_sdk_quicksight.types.date_aggregation_function.deserialize_json(
                data["DateAggregationFunction"]
            )
        )
    if "AttributeAggregationFunction" in data:
        import aws_sdk_quicksight.types.attribute_aggregation_function

        out["attribute_aggregation_function"] = (
            aws_sdk_quicksight.types.attribute_aggregation_function.deserialize_json(
                data["AttributeAggregationFunction"]
            )
        )
    return out
