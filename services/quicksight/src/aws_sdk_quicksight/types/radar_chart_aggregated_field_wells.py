"""Generated from Smithy shape ``com.amazonaws.quicksight#RadarChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.radar_chart_category_field_list
    import aws_sdk_quicksight.types.radar_chart_color_field_list
    import aws_sdk_quicksight.types.radar_chart_values_field_list


class RadarChartAggregatedFieldWells(TypedDict):
    category: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_category_field_list.RadarChartCategoryFieldList"
    ]
    """<p>The aggregated field well categories of a radar chart.</p>"""
    color: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_color_field_list.RadarChartColorFieldList"
    ]
    """<p>The color that are assigned to the aggregated field wells of a radar chart.</p>"""
    values: NotRequired[
        "aws_sdk_quicksight.types.radar_chart_values_field_list.RadarChartValuesFieldList"
    ]
    """<p>The values that are assigned to the aggregated field wells of a radar chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RadarChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import aws_sdk_quicksight.types.radar_chart_category_field_list

        out["Category"] = (
            aws_sdk_quicksight.types.radar_chart_category_field_list.serialize_json(
                value["category"]
            )
        )
    if "color" in value:
        import aws_sdk_quicksight.types.radar_chart_color_field_list

        out["Color"] = (
            aws_sdk_quicksight.types.radar_chart_color_field_list.serialize_json(
                value["color"]
            )
        )
    if "values" in value:
        import aws_sdk_quicksight.types.radar_chart_values_field_list

        out["Values"] = (
            aws_sdk_quicksight.types.radar_chart_values_field_list.serialize_json(
                value["values"]
            )
        )
    return out


def deserialize_json(data: dict) -> RadarChartAggregatedFieldWells:
    out: RadarChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import aws_sdk_quicksight.types.radar_chart_category_field_list

        out["category"] = (
            aws_sdk_quicksight.types.radar_chart_category_field_list.deserialize_json(
                data["Category"]
            )
        )
    if "Color" in data:
        import aws_sdk_quicksight.types.radar_chart_color_field_list

        out["color"] = (
            aws_sdk_quicksight.types.radar_chart_color_field_list.deserialize_json(
                data["Color"]
            )
        )
    if "Values" in data:
        import aws_sdk_quicksight.types.radar_chart_values_field_list

        out["values"] = (
            aws_sdk_quicksight.types.radar_chart_values_field_list.deserialize_json(
                data["Values"]
            )
        )
    return out
