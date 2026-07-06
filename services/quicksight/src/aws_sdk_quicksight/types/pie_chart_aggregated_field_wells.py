"""Generated from Smithy shape ``com.amazonaws.quicksight#PieChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list
    import aws_sdk_quicksight.types.small_multiples_dimension_field_list


class PieChartAggregatedFieldWells(TypedDict, closed=True):
    category: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category (group/color) field wells of a pie chart.</p>"""
    values: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a pie chart. Values are aggregated based on categories.</p>"""
    small_multiples: NotRequired[
        "aws_sdk_quicksight.types.small_multiples_dimension_field_list.SmallMultiplesDimensionFieldList"
    ]
    """<p>The small multiples field well of a pie chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PieChartAggregatedFieldWells) -> dict:
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
    if "small_multiples" in value:
        import aws_sdk_quicksight.types.small_multiples_dimension_field_list

        out["SmallMultiples"] = (
            aws_sdk_quicksight.types.small_multiples_dimension_field_list.serialize_json(
                value["small_multiples"]
            )
        )
    return out


def deserialize_json(data: dict) -> PieChartAggregatedFieldWells:
    out: PieChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
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
    if "SmallMultiples" in data:
        import aws_sdk_quicksight.types.small_multiples_dimension_field_list

        out["small_multiples"] = (
            aws_sdk_quicksight.types.small_multiples_dimension_field_list.deserialize_json(
                data["SmallMultiples"]
            )
        )
    return out
