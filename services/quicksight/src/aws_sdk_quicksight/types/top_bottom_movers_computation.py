"""Generated from Smithy shape ``com.amazonaws.quicksight#TopBottomMoversComputation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field
    import aws_sdk_quicksight.types.measure_field
    import aws_sdk_quicksight.types.short_restrictive_resource_id
    import aws_sdk_quicksight.types.string
    import aws_sdk_quicksight.types.top_bottom_computation_type
    import aws_sdk_quicksight.types.top_bottom_movers_computation_mover_size
    import aws_sdk_quicksight.types.top_bottom_sort_order


class TopBottomMoversComputation(TypedDict, closed=True):
    computation_id: "aws_sdk_quicksight.types.short_restrictive_resource_id.ShortRestrictiveResourceId"
    """<p>The ID for a computation.</p>"""
    name: NotRequired["aws_sdk_quicksight.types.string.String"]
    """<p>The name of a computation.</p>"""
    time: NotRequired["aws_sdk_quicksight.types.dimension_field.DimensionField"]
    """<p>The time field that is used in a computation.</p>"""
    category: NotRequired["aws_sdk_quicksight.types.dimension_field.DimensionField"]
    """<p>The category field that is used in a computation.</p>"""
    value: NotRequired["aws_sdk_quicksight.types.measure_field.MeasureField"]
    """<p>The value field that is used in a computation.</p>"""
    mover_size: NotRequired[
        "aws_sdk_quicksight.types.top_bottom_movers_computation_mover_size.TopBottomMoversComputationMoverSize"
    ]
    """<p>The mover size setup of the top and bottom movers computation.</p>"""
    sort_order: NotRequired[
        "aws_sdk_quicksight.types.top_bottom_sort_order.TopBottomSortOrder"
    ]
    """<p>The sort order setup of the top and bottom movers computation.</p>"""
    type: (
        "aws_sdk_quicksight.types.top_bottom_computation_type.TopBottomComputationType"
    )
    """<p>The computation type. Choose from the following options:</p> <ul> <li> <p>TOP: Top movers computation.</p> </li> <li> <p>BOTTOM: Bottom movers computation.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: TopBottomMoversComputation) -> dict:
    out: dict = {}
    out["ComputationId"] = value["computation_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "time" in value:
        import aws_sdk_quicksight.types.dimension_field

        out["Time"] = aws_sdk_quicksight.types.dimension_field.serialize_json(
            value["time"]
        )
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
    if "mover_size" in value:
        out["MoverSize"] = value["mover_size"]
    if "sort_order" in value:
        import aws_sdk_quicksight.types.top_bottom_sort_order

        out["SortOrder"] = (
            aws_sdk_quicksight.types.top_bottom_sort_order.serialize_json(
                value["sort_order"]
            )
        )
    import aws_sdk_quicksight.types.top_bottom_computation_type

    out["Type"] = aws_sdk_quicksight.types.top_bottom_computation_type.serialize_json(
        value["type"]
    )
    return out


def deserialize_json(data: dict) -> TopBottomMoversComputation:
    out: TopBottomMoversComputation = {}  # type: ignore[typeddict-item]
    if "ComputationId" in data:
        out["computation_id"] = data["ComputationId"]
    else:
        raise DeserializationError("TopBottomMoversComputation.computation_id required")
    if "Name" in data:
        out["name"] = data["Name"]
    if "Time" in data:
        import aws_sdk_quicksight.types.dimension_field

        out["time"] = aws_sdk_quicksight.types.dimension_field.deserialize_json(
            data["Time"]
        )
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
    if "MoverSize" in data:
        out["mover_size"] = data["MoverSize"]
    if "SortOrder" in data:
        import aws_sdk_quicksight.types.top_bottom_sort_order

        out["sort_order"] = (
            aws_sdk_quicksight.types.top_bottom_sort_order.deserialize_json(
                data["SortOrder"]
            )
        )
    if "Type" in data:
        import aws_sdk_quicksight.types.top_bottom_computation_type

        out["type"] = (
            aws_sdk_quicksight.types.top_bottom_computation_type.deserialize_json(
                data["Type"]
            )
        )
    else:
        raise DeserializationError("TopBottomMoversComputation.type required")
    return out
