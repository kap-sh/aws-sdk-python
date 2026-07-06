"""Generated from Smithy shape ``com.amazonaws.sagemakergeospatial#AreaOfInterestGeometry``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker_geospatial.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker_geospatial.types.multi_polygon_geometry_input
    import aws_sdk_sagemaker_geospatial.types.polygon_geometry_input


class _AreaOfInterestGeometry_PolygonGeometry(TypedDict, closed=True):
    PolygonGeometry: (
        "aws_sdk_sagemaker_geospatial.types.polygon_geometry_input.PolygonGeometryInput"
    )


class _AreaOfInterestGeometry_MultiPolygonGeometry(TypedDict, closed=True):
    MultiPolygonGeometry: "aws_sdk_sagemaker_geospatial.types.multi_polygon_geometry_input.MultiPolygonGeometryInput"


AreaOfInterestGeometry: TypeAlias = (
    _AreaOfInterestGeometry_PolygonGeometry
    | _AreaOfInterestGeometry_MultiPolygonGeometry
)


# --- restJson1 ser/de ---
def serialize_json(value: AreaOfInterestGeometry) -> dict:
    if "PolygonGeometry" in value:
        import aws_sdk_sagemaker_geospatial.types.polygon_geometry_input

        return {
            "PolygonGeometry": aws_sdk_sagemaker_geospatial.types.polygon_geometry_input.serialize_json(
                value["PolygonGeometry"]
            )
        }
    elif "MultiPolygonGeometry" in value:
        import aws_sdk_sagemaker_geospatial.types.multi_polygon_geometry_input

        return {
            "MultiPolygonGeometry": aws_sdk_sagemaker_geospatial.types.multi_polygon_geometry_input.serialize_json(
                value["MultiPolygonGeometry"]
            )
        }
    else:
        raise SerializationError("AreaOfInterestGeometry: no variant present")


def deserialize_json(data: dict) -> AreaOfInterestGeometry:
    if "PolygonGeometry" in data:
        import aws_sdk_sagemaker_geospatial.types.polygon_geometry_input

        return {
            "PolygonGeometry": aws_sdk_sagemaker_geospatial.types.polygon_geometry_input.deserialize_json(
                data["PolygonGeometry"]
            )
        }
    elif "MultiPolygonGeometry" in data:
        import aws_sdk_sagemaker_geospatial.types.multi_polygon_geometry_input

        return {
            "MultiPolygonGeometry": aws_sdk_sagemaker_geospatial.types.multi_polygon_geometry_input.deserialize_json(
                data["MultiPolygonGeometry"]
            )
        }
    else:
        raise DeserializationError("AreaOfInterestGeometry: no recognized variant key")
