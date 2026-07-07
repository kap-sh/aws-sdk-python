"""Generated from Smithy shape ``com.amazonaws.quicksight#GeoSpatialColumnGroup``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.column_group_name
    import aws_sdk_quicksight.types.column_list
    import aws_sdk_quicksight.types.geo_spatial_country_code


class GeoSpatialColumnGroup(TypedDict, closed=True):
    name: "aws_sdk_quicksight.types.column_group_name.ColumnGroupName"
    """<p>A display name for the hierarchy.</p>"""
    country_code: NotRequired[
        "aws_sdk_quicksight.types.geo_spatial_country_code.GeoSpatialCountryCode"
    ]
    """<p>Country code.</p>"""
    columns: "aws_sdk_quicksight.types.column_list.ColumnList"
    """<p>Columns in this hierarchy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GeoSpatialColumnGroup) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "country_code" in value:
        import aws_sdk_quicksight.types.geo_spatial_country_code

        out["CountryCode"] = (
            aws_sdk_quicksight.types.geo_spatial_country_code.serialize_json(
                value["country_code"]
            )
        )
    import aws_sdk_quicksight.types.column_list

    out["Columns"] = aws_sdk_quicksight.types.column_list.serialize_json(
        value["columns"]
    )
    return out


def deserialize_json(data: dict) -> GeoSpatialColumnGroup:
    out: GeoSpatialColumnGroup = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("GeoSpatialColumnGroup.name required")
    if "CountryCode" in data:
        import aws_sdk_quicksight.types.geo_spatial_country_code

        out["country_code"] = (
            aws_sdk_quicksight.types.geo_spatial_country_code.deserialize_json(
                data["CountryCode"]
            )
        )
    if "Columns" in data:
        import aws_sdk_quicksight.types.column_list

        out["columns"] = aws_sdk_quicksight.types.column_list.deserialize_json(
            data["Columns"]
        )
    else:
        raise DeserializationError("GeoSpatialColumnGroup.columns required")
    return out
