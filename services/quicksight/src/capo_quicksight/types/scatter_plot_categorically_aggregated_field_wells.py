"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotCategoricallyAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class ScatterPlotCategoricallyAggregatedFieldWells(TypedDict, closed=True):
    x_axis: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The x-axis field well of a scatter plot.</p> <p>The x-axis is aggregated by category.</p>"""
    y_axis: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The y-axis field well of a scatter plot.</p> <p>The y-axis is aggregated by category.</p>"""
    category: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category field well of a scatter plot.</p>"""
    size: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The size field well of a scatter plot.</p>"""
    label: NotRequired["capo_quicksight.types.dimension_field_list.DimensionFieldList"]
    """<p>The label field well of a scatter plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotCategoricallyAggregatedFieldWells) -> dict:
    out: dict = {}
    if "x_axis" in value:
        import capo_quicksight.types.measure_field_list

        out["XAxis"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["x_axis"]
        )
    if "y_axis" in value:
        import capo_quicksight.types.measure_field_list

        out["YAxis"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["y_axis"]
        )
    if "category" in value:
        import capo_quicksight.types.dimension_field_list

        out["Category"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["category"]
        )
    if "size" in value:
        import capo_quicksight.types.measure_field_list

        out["Size"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["size"]
        )
    if "label" in value:
        import capo_quicksight.types.dimension_field_list

        out["Label"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["label"]
        )
    return out


def deserialize_json(data: dict) -> ScatterPlotCategoricallyAggregatedFieldWells:
    out: ScatterPlotCategoricallyAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "XAxis" in data:
        import capo_quicksight.types.measure_field_list

        out["x_axis"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["XAxis"]
        )
    if "YAxis" in data:
        import capo_quicksight.types.measure_field_list

        out["y_axis"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["YAxis"]
        )
    if "Category" in data:
        import capo_quicksight.types.dimension_field_list

        out["category"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Category"]
        )
    if "Size" in data:
        import capo_quicksight.types.measure_field_list

        out["size"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Size"]
        )
    if "Label" in data:
        import capo_quicksight.types.dimension_field_list

        out["label"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Label"]
        )
    return out
