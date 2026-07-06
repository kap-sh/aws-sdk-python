"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomRankedComputation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field
    import aws_sdk_quicksight.types.measure_field
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.top_bottom_computation_type
    import aws_sdk_quicksight.types.top_bottom_ranked_computation_result_size


class TopBottomRankedComputation(TypedDict, closed=True):
    computation_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for a computation.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    category: NotRequired["aws_sdk_quicksight.types.dimension_field.DimensionField"]
    """<p>The category field that is used in a computation.</p>"""
    value: NotRequired["aws_sdk_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    result_size: NotRequired[
        "aws_sdk_quicksight.types.top_bottom_ranked_computation_result_size.TopBottomRankedComputationResultSize"
    ]
    """<p>The result size of a top and bottom ranked computation.</p>"""
    type: (
        "aws_sdk_quicksight.types.top_bottom_computation_type.TopBottomComputationType"
    )
    """<p>The computation type. Choose one of the following options:</p> <ul> <li> <p>TOP: A top ranked computation.</p> </li> <li> <p>BOTTOM: A bottom ranked computation.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomRankedComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "category" in value:
        import aws_sdk_quicksight.types.dimension_field

        out["Category"] = aws_sdk_quicksight.types.dimension_field.serialize_json(
            value["category"]
        )
    if "value" in value:
        import aws_sdk_quicksight.types.measure_field

        out["Value"] = aws_sdk_quicksight.types.measure_field.serialize_json(
            value["value"]
        )
    if "result_size" in value:
        out["ResultSize"] = value["result_size"]
    import aws_sdk_quicksight.types.top_bottom_computation_type

    out["Type"] = aws_sdk_quicksight.types.top_bottom_computation_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> TopBottomRankedComputation:
    out: TopBottomRankedComputation = {}  # type: ignore[typeddict-item]
    if "ComputationId" in data:
        out["computation_id"] = data["ComputationId"]
    else:
        raise DeserializationError("TopBottomRankedComputation.computation_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Category" in data:
        import aws_sdk_quicksight.types.dimension_field

        out["category"] = aws_sdk_quicksight.types.dimension_field.deserialize_json(
            data["Category"]
        )
    if "Value" in data:
        import aws_sdk_quicksight.types.measure_field

        out["value"] = aws_sdk_quicksight.types.measure_field.deserialize_json(
            data["Value"]
        )
    if "ResultSize" in data:
        out["result_size"] = data["ResultSize"]
    if "Type" in data:
        import aws_sdk_quicksight.types.top_bottom_computation_type

        out["type"] = (
            aws_sdk_quicksight.types.top_bottom_computation_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("TopBottomRankedComputation.type required")
    return out
