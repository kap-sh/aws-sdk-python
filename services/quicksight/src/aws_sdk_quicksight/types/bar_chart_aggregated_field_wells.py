"""Generated from Smithy shape ``com.amazonaws.quicksight#BarChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list
    import aws_sdk_quicksight.types.small_multiples_dimension_field_list


class BarChartAggregatedFieldWells(TypedDict):
    category: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category (y-axis) field well of a bar chart.</p>"""
    values: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a bar chart. Values are aggregated by category.</p>"""
    colors: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The color (group/color) field well of a bar chart.</p>"""
    small_multiples: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_dimension_field_list.SmallMultiplesDimensionFieldList"
    ]
    """<p>The small multiples field well of a bar chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BarChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Category"] = aws_sdk_quicksight.types.dimension_field_list.serialize_json(
            value["category"]
        )
    if "values" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["Values"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "colors" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Colors"] = aws_sdk_quicksight.types.dimension_field_list.serialize_json(
            value["colors"]
        )
    if "small_multiples" in value:
        import aws_sdk_quicksight.types.small_multiples_dimension_field_list

        out["SmallMultiples"] = (
            aws_sdk_quicksight.types.small_multiples_dimension_field_list.serialize_json(
                value["small_multiples"]
            )
        )
    return out


def deserialize_json(data: dict) -> BarChartAggregatedFieldWells:
    out: BarChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["category"] = (
            aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
                data["Category"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["values"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if "Colors" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["colors"] = aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
            data["Colors"]
        )
    if "SmallMultiples" in data:
        import aws_sdk_quicksight.types.small_multiples_dimension_field_list

        out["small_multiples"] = (
            aws_sdk_quicksight.types.small_multiples_dimension_field_list.deserialize_json(
                data["SmallMultiples"]
            )
        )
    return out
