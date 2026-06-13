"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnGroup``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geo_spatial_column_group


class ColumnGroup(TypedDict):
    geo_spatial_column_group: NotRequired[
        "aws_sdk_quicksight.types.geo_spatial_column_group.GeoSpatialColumnGroup"
    ]
    """<p>Geospatial column group that denotes a hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnGroup) -> dict:
    out: dict = {}
    if "geo_spatial_column_group" in value:
        import aws_sdk_quicksight.types.geo_spatial_column_group

        out["GeoSpatialColumnGroup"] = (
            aws_sdk_quicksight.types.geo_spatial_column_group.serialize_json(
                value["geo_spatial_column_group"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnGroup:
    out: ColumnGroup = {}  # type: ignore[typeddict-item]
    if "GeoSpatialColumnGroup" in data:
        import aws_sdk_quicksight.types.geo_spatial_column_group

        out["geo_spatial_column_group"] = (
            aws_sdk_quicksight.types.geo_spatial_column_group.deserialize_json(
                data["GeoSpatialColumnGroup"]
            )
        )
    return out
