"""Generated from Smithy shape ``com.amazonaws.quicksight#ScatterPlotCategoricallyAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list


class ScatterPlotCategoricallyAggregatedFieldWells(TypedDict, closed=True):
    x_axis: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The x-axis field well of a scatter plot.</p> <p>The x-axis is aggregated by category.</p>"""
    y_axis: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The y-axis field well of a scatter plot.</p> <p>The y-axis is aggregated by category.</p>"""
    category: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The category field well of a scatter plot.</p>"""
    size: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The size field well of a scatter plot.</p>"""
    label: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The label field well of a scatter plot.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScatterPlotCategoricallyAggregatedFieldWells) -> dict:
    out: dict = {}
    if "x_axis" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["XAxis"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["x_axis"]
        )
    if "y_axis" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["YAxis"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["y_axis"]
        )
    if "category" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Category"] = aws_sdk_quicksight.types.dimension_field_list.serialize_json(
            value["category"]
        )
    if "size" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["Size"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["size"]
        )
    if "label" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Label"] = aws_sdk_quicksight.types.dimension_field_list.serialize_json(
            value["label"]
        )
    return out


def deserialize_json(data: dict) -> ScatterPlotCategoricallyAggregatedFieldWells:
    out: ScatterPlotCategoricallyAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "XAxis" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["x_axis"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["XAxis"]
        )
    if "YAxis" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["y_axis"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["YAxis"]
        )
    if "Category" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["category"] = (
            aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
                data["Category"]
            )
        )
    if "Size" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["size"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["Size"]
        )
    if "Label" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["label"] = aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
            data["Label"]
        )
    return out
