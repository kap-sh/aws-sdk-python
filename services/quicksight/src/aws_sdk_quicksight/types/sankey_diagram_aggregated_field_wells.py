"""Generated from Smithy shape ``com.amazonaws.quicksight#SankeyDiagramAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.dimension_field_list
    import aws_sdk_quicksight.types.measure_field_list


class SankeyDiagramAggregatedFieldWells(TypedDict, closed=True):
    source: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The source field wells of a sankey diagram.</p>"""
    destination: NotRequired[
        "aws_sdk_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The destination field wells of a sankey diagram.</p>"""
    weight: NotRequired["aws_sdk_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The weight field wells of a sankey diagram.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SankeyDiagramAggregatedFieldWells) -> dict:
    out: dict = {}
    if "source" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Source"] = aws_sdk_quicksight.types.dimension_field_list.serialize_json(
            value["source"]
        )
    if "destination" in value:
        import aws_sdk_quicksight.types.dimension_field_list

        out["Destination"] = (
            aws_sdk_quicksight.types.dimension_field_list.serialize_json(
                value["destination"]
            )
        )
    if "weight" in value:
        import aws_sdk_quicksight.types.measure_field_list

        out["Weight"] = aws_sdk_quicksight.types.measure_field_list.serialize_json(
            value["weight"]
        )
    return out


def deserialize_json(data: dict) -> SankeyDiagramAggregatedFieldWells:
    out: SankeyDiagramAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["source"] = aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
            data["Source"]
        )
    if "Destination" in data:
        import aws_sdk_quicksight.types.dimension_field_list

        out["destination"] = (
            aws_sdk_quicksight.types.dimension_field_list.deserialize_json(
                data["Destination"]
            )
        )
    if "Weight" in data:
        import aws_sdk_quicksight.types.measure_field_list

        out["weight"] = aws_sdk_quicksight.types.measure_field_list.deserialize_json(
            data["Weight"]
        )
    return out
