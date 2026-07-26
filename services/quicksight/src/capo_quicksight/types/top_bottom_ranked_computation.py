"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomRankedComputation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field
    import capo_quicksight.types.measure_field
    import capo_quicksight.types.short_restrictive_resource_id
    import capo_quicksight.types.string
    import capo_quicksight.types.top_bottom_computation_type
    import capo_quicksight.types.top_bottom_ranked_computation_result_size


class TopBottomRankedComputation(TypedDict, closed=True):
    computation_id: (
        "capo_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    )
    """<p>The ID for a computation.</p>"""
    name: NotRequired["capo_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    category: NotRequired["capo_quicksight.types.dimension_field.DimensionField"]
    """<p>The category field that is used in a computation.</p>"""
    value: NotRequired["capo_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    result_size: NotRequired[
        "capo_quicksight.types.top_bottom_ranked_computation_result_size.TopBottomRankedComputationResultSize"
    ]
    """<p>The result size of a top and bottom ranked computation.</p>"""
    type: "capo_quicksight.types.top_bottom_computation_type.TopBottomComputationType"
    """<p>The computation type. Choose one of the following options:</p> <ul> <li> <p>TOP: A top ranked computation.</p> </li> <li> <p>BOTTOM: A bottom ranked computation.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomRankedComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "category" in value:
        import capo_quicksight.types.dimension_field

        out["Category"] = capo_quicksight.types.dimension_field.serialize_json(
            value["category"]
        )
    if "value" in value:
        import capo_quicksight.types.measure_field

        out["Value"] = capo_quicksight.types.measure_field.serialize_json(
            value["value"]
        )
    if "result_size" in value:
        out["ResultSize"] = value["result_size"]
    import capo_quicksight.types.top_bottom_computation_type

    out["Type"] = capo_quicksight.types.top_bottom_computation_type.serialize_json(
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
        import capo_quicksight.types.dimension_field

        out["category"] = capo_quicksight.types.dimension_field.deserialize_json(
            data["Category"]
        )
    if "Value" in data:
        import capo_quicksight.types.measure_field

        out["value"] = capo_quicksight.types.measure_field.deserialize_json(
            data["Value"]
        )
    if "ResultSize" in data:
        out["result_size"] = data["ResultSize"]
    if "Type" in data:
        import capo_quicksight.types.top_bottom_computation_type

        out["type"] = (
            capo_quicksight.types.top_bottom_computation_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("TopBottomRankedComputation.type required")
    return out
