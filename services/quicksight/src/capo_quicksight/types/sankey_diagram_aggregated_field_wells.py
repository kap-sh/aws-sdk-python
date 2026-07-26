"""Generated from Smithy shape ``com.amazonaws.quicksight#SankeyDiagramAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class SankeyDiagramAggregatedFieldWells(TypedDict, closed=True):
    source: NotRequired["capo_quicksight.types.dimension_field_list.DimensionFieldList"]
    """<p>The source field wells of a sankey diagram.</p>"""
    destination: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The destination field wells of a sankey diagram.</p>"""
    weight: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The weight field wells of a sankey diagram.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SankeyDiagramAggregatedFieldWells) -> dict:
    out: dict = {}
    if "source" in value:
        import capo_quicksight.types.dimension_field_list

        out["Source"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["source"]
        )
    if "destination" in value:
        import capo_quicksight.types.dimension_field_list

        out["Destination"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["destination"]
        )
    if "weight" in value:
        import capo_quicksight.types.measure_field_list

        out["Weight"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["weight"]
        )
    return out


def deserialize_json(data: dict) -> SankeyDiagramAggregatedFieldWells:
    out: SankeyDiagramAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Source" in data:
        import capo_quicksight.types.dimension_field_list

        out["source"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Source"]
        )
    if "Destination" in data:
        import capo_quicksight.types.dimension_field_list

        out["destination"] = (
            capo_quicksight.types.dimension_field_list.deserialize_json(
                data["Destination"]
            )
        )
    if "Weight" in data:
        import capo_quicksight.types.measure_field_list

        out["weight"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Weight"]
        )
    return out
