"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixAvoidanceArea``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_avoidance_area_geometry


class RouteMatrixAvoidanceArea(TypedDict, closed=True):
    geometry: "aws_sdk_geo_routes.types.route_matrix_avoidance_area_geometry.RouteMatrixAvoidanceAreaGeometry"
    """<p>Geometry of the area to be avoided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixAvoidanceArea) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.route_matrix_avoidance_area_geometry

    out["Geometry"] = (
        aws_sdk_geo_routes.types.route_matrix_avoidance_area_geometry.serialize_json(
            value["geometry"]
        )
    )
    return out


def deserialize_json(data: dict) -> RouteMatrixAvoidanceArea:
    out: RouteMatrixAvoidanceArea = {}  # type: ignore[typeddict-item]
    if "Geometry" in data:
        import aws_sdk_geo_routes.types.route_matrix_avoidance_area_geometry

        out["geometry"] = (
            aws_sdk_geo_routes.types.route_matrix_avoidance_area_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    else:
        raise DeserializationError("RouteMatrixAvoidanceArea.geometry required")
    return out
