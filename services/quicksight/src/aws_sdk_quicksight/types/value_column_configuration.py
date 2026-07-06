"""Generated from Smithy shape ``com.amazonaws.quicksight#ValueColumnConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.data_prep_aggregation_function


class ValueColumnConfiguration(TypedDict, closed=True):
    aggregation_function: NotRequired[
        "aws_sdk_quicksight.types.data_prep_aggregation_function.DataPrepAggregationFunction"
    ]
    """<p>The aggregation function to apply when multiple values map to the same pivoted cell.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ValueColumnConfiguration) -> dict:
    out: dict = {}
    if "aggregation_function" in value:
        import aws_sdk_quicksight.types.data_prep_aggregation_function

        out["AggregationFunction"] = (
            aws_sdk_quicksight.types.data_prep_aggregation_function.serialize_json(
                value["aggregation_function"]
            )
        )
    return out


def deserialize_json(data: dict) -> ValueColumnConfiguration:
    out: ValueColumnConfiguration = {}  # type: ignore[typeddict-item]
    if "AggregationFunction" in data:
        import aws_sdk_quicksight.types.data_prep_aggregation_function

        out["aggregation_function"] = (
            aws_sdk_quicksight.types.data_prep_aggregation_function.deserialize_json(
                data["AggregationFunction"]
            )
        )
    return out
