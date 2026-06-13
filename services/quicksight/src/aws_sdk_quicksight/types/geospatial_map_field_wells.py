"""Generated from Smithy shape ``com.amazonaws.quicksight#GeospatialMapFieldWells``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geospatial_map_aggregated_field_wells


class GeospatialMapFieldWells(TypedDict):
    geospatial_map_aggregated_field_wells: NotRequired[
        "aws_sdk_quicksight.types.geospatial_map_aggregated_field_wells.GeospatialMapAggregatedFieldWells"
    ]
    """<p>The aggregated field well for a geospatial map.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeospatialMapFieldWells) -> dict:
    out: dict = {}
    if "geospatial_map_aggregated_field_wells" in value:
        import aws_sdk_quicksight.types.geospatial_map_aggregated_field_wells

        out["GeospatialMapAggregatedFieldWells"] = (
            aws_sdk_quicksight.types.geospatial_map_aggregated_field_wells.serialize_json(
                value["geospatial_map_aggregated_field_wells"]
            )
        )
    return out


def deserialize_json(data: dict) -> GeospatialMapFieldWells:
    out: GeospatialMapFieldWells = {}  # type: ignore[typeddict-item]
    if "GeospatialMapAggregatedFieldWells" in data:
        import aws_sdk_quicksight.types.geospatial_map_aggregated_field_wells

        out["geospatial_map_aggregated_field_wells"] = (
            aws_sdk_quicksight.types.geospatial_map_aggregated_field_wells.deserialize_json(
                data["GeospatialMapAggregatedFieldWells"]
            )
        )
    return out
