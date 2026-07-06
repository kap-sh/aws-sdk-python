"""Generated from Smithy shape ``com.amazonaws.quicksight#ColumnSemanticType``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.geo_spatial_data_role


class ColumnSemanticType(TypedDict, closed=True):
    geographical_role: NotRequired[
        "aws_sdk_quicksight.types.geo_spatial_data_role.GeoSpatialDataRole"
    ]
    """<p>The geographical role of the column in the new data preparation experience.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ColumnSemanticType) -> dict:
    out: dict = {}
    if "geographical_role" in value:
        import aws_sdk_quicksight.types.geo_spatial_data_role

        out["GeographicalRole"] = (
            aws_sdk_quicksight.types.geo_spatial_data_role.serialize_json(
                value["geographical_role"]
            )
        )
    return out


def deserialize_json(data: dict) -> ColumnSemanticType:
    out: ColumnSemanticType = {}  # type: ignore[typeddict-item]
    if "GeographicalRole" in data:
        import aws_sdk_quicksight.types.geo_spatial_data_role

        out["geographical_role"] = (
            aws_sdk_quicksight.types.geo_spatial_data_role.deserialize_json(
                data["GeographicalRole"]
            )
        )
    return out
