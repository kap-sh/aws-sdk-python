"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#ItemSource``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sagemaker_geospatial.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_sagemaker_geospatial.types.assets_map
    import aws_sdk_sagemaker_geospatial.types.geometry
    import aws_sdk_sagemaker_geospatial.types.properties


class ItemSource(TypedDict):
    id: "str"
    """<p>A unique Id for the source item.</p>"""
    geometry: "aws_sdk_sagemaker_geospatial.types.geometry.Geometry"
    """<p>The item Geometry in GeoJson format.</p>"""
    assets: NotRequired["aws_sdk_sagemaker_geospatial.types.assets_map.AssetsMap"]
    """<p>This is a dictionary of Asset Objects data associated with the Item that can be downloaded or streamed, each with a unique key.</p>"""
    date_time: "datetime.datetime"
    """<p>The searchable date and time of the item, in UTC.</p>"""
    properties: NotRequired["aws_sdk_sagemaker_geospatial.types.properties.Properties"]
    """<p>This field contains additional properties of the item.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ItemSource) -> dict:
    out: dict = {}
    out["Id"] = value["id"]
    import aws_sdk_sagemaker_geospatial.types.geometry

    out["Geometry"] = aws_sdk_sagemaker_geospatial.types.geometry.serialize_json(
        value["geometry"]
    )
    if "assets" in value:
        import aws_sdk_sagemaker_geospatial.types.assets_map

        out["Assets"] = aws_sdk_sagemaker_geospatial.types.assets_map.serialize_json(
            value["assets"]
        )
    import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

    out["DateTime"] = (
        aws_sdk_sagemaker_geospatial.types._prelude.timestamp.serialize_json(
            value["date_time"]
        )
    )
    if "properties" in value:
        import aws_sdk_sagemaker_geospatial.types.properties

        out["Properties"] = (
            aws_sdk_sagemaker_geospatial.types.properties.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ItemSource:
    out: ItemSource = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("ItemSource.id required")
    if "Geometry" in data:
        import aws_sdk_sagemaker_geospatial.types.geometry

        out["geometry"] = aws_sdk_sagemaker_geospatial.types.geometry.deserialize_json(
            data["Geometry"]
        )
    else:
        raise DeserializationError("ItemSource.geometry required")
    if "Assets" in data:
        import aws_sdk_sagemaker_geospatial.types.assets_map

        out["assets"] = aws_sdk_sagemaker_geospatial.types.assets_map.deserialize_json(
            data["Assets"]
        )
    if "DateTime" in data:
        import aws_sdk_sagemaker_geospatial.types._prelude.timestamp

        out["date_time"] = (
            aws_sdk_sagemaker_geospatial.types._prelude.timestamp.deserialize_json(
                data["DateTime"]
            )
        )
    else:
        raise DeserializationError("ItemSource.date_time required")
    if "Properties" in data:
        import aws_sdk_sagemaker_geospatial.types.properties

        out["properties"] = (
            aws_sdk_sagemaker_geospatial.types.properties.deserialize_json(
                data["Properties"]
            )
        )
    return out
