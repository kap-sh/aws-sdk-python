"""Generated from Smithy shape ``com.amazonaws.quicksight#ComboChartAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class ComboChartAggregatedFieldWells(TypedDict, closed=True):
    category: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The aggregated category field wells of a combo chart.</p>"""
    bar_values: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The aggregated <code>BarValues</code> field well of a combo chart.</p>"""
    colors: NotRequired["capo_quicksight.types.dimension_field_list.DimensionFieldList"]
    """<p>The aggregated colors field well of a combo chart.</p>"""
    line_values: NotRequired[
        "capo_quicksight.types.measure_field_list.MeasureFieldList"
    ]
    """<p>The aggregated <code>LineValues</code> field well of a combo chart.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComboChartAggregatedFieldWells) -> dict:
    out: dict = {}
    if "category" in value:
        import capo_quicksight.types.dimension_field_list

        out["Category"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["category"]
        )
    if "bar_values" in value:
        import capo_quicksight.types.measure_field_list

        out["BarValues"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["bar_values"]
        )
    if "colors" in value:
        import capo_quicksight.types.dimension_field_list

        out["Colors"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["colors"]
        )
    if "line_values" in value:
        import capo_quicksight.types.measure_field_list

        out["LineValues"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["line_values"]
        )
    return out


def deserialize_json(data: dict) -> ComboChartAggregatedFieldWells:
    out: ComboChartAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Category" in data:
        import capo_quicksight.types.dimension_field_list

        out["category"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Category"]
        )
    if "BarValues" in data:
        import capo_quicksight.types.measure_field_list

        out["bar_values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["BarValues"]
        )
    if "Colors" in data:
        import capo_quicksight.types.dimension_field_list

        out["colors"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Colors"]
        )
    if "LineValues" in data:
        import capo_quicksight.types.measure_field_list

        out["line_values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["LineValues"]
        )
    return out
