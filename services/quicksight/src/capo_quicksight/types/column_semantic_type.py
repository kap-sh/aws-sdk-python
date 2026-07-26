"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSemanticType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.geo_spatial_data_role


class ColumnSemanticType(TypedDict, closed=True):
    geographical_role: NotRequired[
        "capo_quicksight.types.geo_spatial_data_role.GeoSpatialDataRole"
    ]
    """<p>The geographical role of the column in the new data preparation experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSemanticType) -> dict:
    out: dict = {}
    if "geographical_role" in value:
        import capo_quicksight.types.geo_spatial_data_role

        out["GeographicalRole"] = (
            capo_quicksight.types.geo_spatial_data_role.serialize_json(
                value["geographical_role"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnSemanticType:
    out: ColumnSemanticType = {}  # type: ignore[typeddict-item]
    if "GeographicalRole" in data:
        import capo_quicksight.types.geo_spatial_data_role

        out["geographical_role"] = (
            capo_quicksight.types.geo_spatial_data_role.deserialize_json(
                data["GeographicalRole"]
            )
        )
    return out
