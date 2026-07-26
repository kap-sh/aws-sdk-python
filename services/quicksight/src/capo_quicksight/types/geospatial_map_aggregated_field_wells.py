"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapAggregatedFieldWells``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.dimension_field_list
    import capo_quicksight.types.measure_field_list


class GeospatialMapAggregatedFieldWells(TypedDict, closed=True):
    geospatial: NotRequired[
        "capo_quicksight.types.dimension_field_list.DimensionFieldList"
    ]
    """<p>The geospatial field wells of a geospatial map. Values are grouped by geospatial fields.</p>"""
    values: NotRequired["capo_quicksight.types.measure_field_list.MeasureFieldList"]
    """<p>The size field wells of a geospatial map. Values are aggregated based on geospatial fields.</p>"""
    colors: NotRequired["capo_quicksight.types.dimension_field_list.DimensionFieldList"]
    """<p>The color field wells of a geospatial map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapAggregatedFieldWells) -> dict:
    out: dict = {}
    if "geospatial" in value:
        import capo_quicksight.types.dimension_field_list

        out["Geospatial"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["geospatial"]
        )
    if "values" in value:
        import capo_quicksight.types.measure_field_list

        out["Values"] = capo_quicksight.types.measure_field_list.serialize_json(
            value["values"]
        )
    if "colors" in value:
        import capo_quicksight.types.dimension_field_list

        out["Colors"] = capo_quicksight.types.dimension_field_list.serialize_json(
            value["colors"]
        )
    return out


def deserialize_json(data: dict) -> GeospatialMapAggregatedFieldWells:
    out: GeospatialMapAggregatedFieldWells = {}  # type: ignore[typeddict-item]
    if "Geospatial" in data:
        import capo_quicksight.types.dimension_field_list

        out["geospatial"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Geospatial"]
        )
    if "Values" in data:
        import capo_quicksight.types.measure_field_list

        out["values"] = capo_quicksight.types.measure_field_list.deserialize_json(
            data["Values"]
        )
    if "Colors" in data:
        import capo_quicksight.types.dimension_field_list

        out["colors"] = capo_quicksight.types.dimension_field_list.deserialize_json(
            data["Colors"]
        )
    return out
