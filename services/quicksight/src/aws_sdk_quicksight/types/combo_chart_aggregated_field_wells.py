"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list


class ComboChartAggregatedFieldWells(TypedDict):
    category: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The aggregated category field wells of a combo chart.</p>"""
    bar_values: NotRequired[
        "aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"
    ]
    """<p>The aggregated <code>BarValues</code> field well of a combo chart.</p>"""
    colors: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The aggregated colors field well of a combo chart.</p>"""
    line_values: NotRequired[
        "aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"
    ]
    """<p>The aggregated <code>LineValues</code> field well of a combo chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Category"] = aws_sdk_quicksight.types.dimension_field_list.serialize_json(
            value["category"]
        )
    if "bar_values" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["BarValues"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["bar_values"]
        )
    if "colors" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Colors"] = aws_sdk_quicksight.types.dimension_field_list.serialize_json(
            value["colors"]
        )
    if "line_values" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["LineValues"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["line_values"]
        )
    return out


def deserialize_json(data: dict) -> ComboChartAggregatedFieldWells:
    out: ComboChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["category"] = (
            aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
                data["Category"]
            )
        )
    if "BarValues" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["bar_values"] = (
            aws_sdk_quicksight.types.measure_field_list.deserialize_json(
                data["BarValues"]
            )
        )
    if "Colors" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["colors"] = aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
            data["Colors"]
        )
    if "LineValues" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["line_values"] = (
            aws_sdk_quicksight.types.measure_field_list.deserialize_json(
                data["LineValues"]
            )
        )
    return out
