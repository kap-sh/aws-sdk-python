"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineAvoidanceArea``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.isoline_avoidance_area_geometry
    import aws_sdk_geo_routes.types.isoline_avoidance_area_geometry_list

IsolineAvoidanceArea = TypedDict(
    "IsolineAvoidanceArea",
    {
        "except": NotRequired[
            "aws_sdk_geo_routes.types.isoline_avoidance_area_geometry_list.IsolineAvoidanceAreaGeometryList"
        ],
        "geometry": "aws_sdk_geo_routes.types.isoline_avoidance_area_geometry.IsolineAvoidanceAreaGeometry",
    },
)


# --- restJson1 ser/de ---
def serialize_json(value: IsolineAvoidanceArea) -> dict:
    out: dict = {}
    if "except" in value:
        import aws_sdk_geo_routes.types.isoline_avoidance_area_geometry_list

        out["Except"] = (
            aws_sdk_geo_routes.types.isoline_avoidance_area_geometry_list.serialize_json(
                value["except"]
            )
        )
    import aws_sdk_geo_routes.types.isoline_avoidance_area_geometry

    out["Geometry"] = (
        aws_sdk_geo_routes.types.isoline_avoidance_area_geometry.serialize_json(
            value["geometry"]
        )
    )
    return out


def deserialize_json(data: dict) -> IsolineAvoidanceArea:
    out: IsolineAvoidanceArea = {}  # type: ignore[typeddict-item]
    if "Except" in data:
        import aws_sdk_geo_routes.types.isoline_avoidance_area_geometry_list

        out["except"] = (
            aws_sdk_geo_routes.types.isoline_avoidance_area_geometry_list.deserialize_json(
                data["Except"]
            )
        )
    if "Geometry" in data:
        import aws_sdk_geo_routes.types.isoline_avoidance_area_geometry

        out["geometry"] = (
            aws_sdk_geo_routes.types.isoline_avoidance_area_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    else:
        raise DeserializationError("IsolineAvoidanceArea.geometry required")
    return out
