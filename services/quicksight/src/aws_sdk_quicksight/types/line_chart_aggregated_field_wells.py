"""Generated from Smithy shape ``com.amazonaws.quicksight#LineChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list
    import aws_sdk_quicksight.types.small_multiples_dimension_field_list


class LineChartAggregatedFieldWells(TypedDict, closed=True):
    category: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category field wells of a line chart. Values are grouped by category fields.</p>"""
    values: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a line chart. Values are aggregated based on categories.</p>"""
    colors: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The color field wells of a line chart. Values are grouped by category fields.</p>"""
    small_multiples: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_dimension_field_list.SmallMultiplesDimensionFieldList"
    ]
    """<p>The small multiples field well of a line chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LineChartAggregatedFieldWells) -> dict:
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


def deserialize_json(data: dict) -> LineChartAggregatedFieldWells:
    out: LineChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
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
