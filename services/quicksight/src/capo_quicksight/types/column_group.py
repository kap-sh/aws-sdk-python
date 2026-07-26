"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geo_spatial_column_group


class ColumnGroup(TypedDict, closed=True):
    geo_spatial_column_group: NotRequired[
        "capo_quicksight.types.geo_spatial_column_group.GeoSpatialColumnGroup"
    ]
    """<p>Geospatial column group that denotes a hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroup) -> dict:
    out: dict = {}
    if "geo_spatial_column_group" in value:
        import capo_quicksight.types.geo_spatial_column_group

        out["GeoSpatialColumnGroup"] = (
            capo_quicksight.types.geo_spatial_column_group.serialize_json(
                value["geo_spatial_column_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnGroup:
    out: ColumnGroup = {}  # type: ignore[typeddict-item]
    if "GeoSpatialColumnGroup" in data:
        import capo_quicksight.types.geo_spatial_column_group

        out["geo_spatial_column_group"] = (
            capo_quicksight.types.geo_spatial_column_group.deserialize_json(
                data["GeoSpatialColumnGroup"]
            )
        )
    return out
