"""Generated from Smithy shape ``com.amazonaws.quicksight#WaterfallChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list


class WaterfallChartAggregatedFieldWells(TypedDict, closed=True):
    categories: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category field wells of a waterfall visual.</p>"""
    values: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The value field wells of a waterfall visual.</p>"""
    breakdowns: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The breakdown field wells of a waterfall visual.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaterfallChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "categories" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Categories"] = (
            aws_sdk_quicksight.types.dimension_field_list.serialize_json(
                value["categories"]
            )
        )
    if "values" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["Values"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "breakdowns" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Breakdowns"] = (
            aws_sdk_quicksight.types.dimension_field_list.serialize_json(
                value["breakdowns"]
            )
        )
    return out


def deserialize_json(data: dict) -> WaterfallChartAggregatedFieldWells:
    out: WaterfallChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Categories" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["categories"] = (
            aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
                data["Categories"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["values"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if "Breakdowns" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["breakdowns"] = (
            aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
                data["Breakdowns"]
            )
        )
    return out
