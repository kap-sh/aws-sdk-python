"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineShapeGeometryList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.isoline_shape_geometry

IsolineShapeGeometryList: TypeAlias = list[
    "aws_sdk_geo_routes.types.isoline_shape_geometry.IsolineShapeGeometry"
]


# --- restJson1 ser/de ---
def serialize_json(value: IsolineShapeGeometryList) -> list:
    import aws_sdk_geo_routes.types.isoline_shape_geometry

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.isoline_shape_geometry.serialize_json(item))
    return out


def deserialize_json(data: list) -> IsolineShapeGeometryList:
    import aws_sdk_geo_routes.types.isoline_shape_geometry

    out: IsolineShapeGeometryList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.isoline_shape_geometry.deserialize_json(item)
        )
    return out
