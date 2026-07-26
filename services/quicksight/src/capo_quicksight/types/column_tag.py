"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnTag``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.column_description
    import capo_quicksight.types.geo_spatial_data_role


class ColumnTag(TypedDict, closed=True):
    column_geographic_role: NotRequired[
        "capo_quicksight.types.geo_spatial_data_role.GeoSpatialDataRole"
    ]
    """<p>A geospatial role for a column.</p>"""
    column_description: NotRequired[
        "capo_quicksight.types.column_description.ColumnDescription"
    ]
    """<p>A description for a column.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnTag) -> dict:
    out: dict = {}
    if "column_geographic_role" in value:
        import capo_quicksight.types.geo_spatial_data_role

        out["ColumnGeographicRole"] = (
            capo_quicksight.types.geo_spatial_data_role.serialize_json(
                value["column_geographic_role"]
            )
        )
    if "column_description" in value:
        import capo_quicksight.types.column_description

        out["ColumnDescription"] = (
            capo_quicksight.types.column_description.serialize_json(
                value["column_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnTag:
    out: ColumnTag = {}  # type: ignore[typeddict-item]
    if "ColumnGeographicRole" in data:
        import capo_quicksight.types.geo_spatial_data_role

        out["column_geographic_role"] = (
            capo_quicksight.types.geo_spatial_data_role.deserialize_json(
                data["ColumnGeographicRole"]
            )
        )
    if "ColumnDescription" in data:
        import capo_quicksight.types.column_description

        out["column_description"] = (
            capo_quicksight.types.column_description.deserialize_json(
                data["ColumnDescription"]
            )
        )
    return out
