"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixBoundary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix_boundary_geometry
    import aws_sdk_geo_routes.types.sensitive_boolean


class RouteMatrixBoundary(TypedDict):
    geometry: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_boundary_geometry.RouteMatrixBoundaryGeometry"
    ]
    """<p>Geometry of the area to be avoided.</p>"""
    unbounded: NotRequired[
        "aws_sdk_geo_routes.types.sensitive_boolean.SensitiveBoolean"
    ]
    """<p>No restrictions in terms of a routing boundary, and is typically used for longer routes.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixBoundary) -> dict:
    out: dict = {}
    if "geometry" in value:
        import aws_sdk_geo_routes.types.route_matrix_boundary_geometry

        out["Geometry"] = (
            aws_sdk_geo_routes.types.route_matrix_boundary_geometry.serialize_json(
                value["geometry"]
            )
        )
    if "unbounded" in value:
        out["Unbounded"] = value["unbounded"]
    return out


def deserialize_json(data: dict) -> RouteMatrixBoundary:
    out: RouteMatrixBoundary = {}  # type: ignore[typeddict-item]
    if "Geometry" in data:
        import aws_sdk_geo_routes.types.route_matrix_boundary_geometry

        out["geometry"] = (
            aws_sdk_geo_routes.types.route_matrix_boundary_geometry.deserialize_json(
                data["Geometry"]
            )
        )
    if "Unbounded" in data:
        out["unbounded"] = data["Unbounded"]
    return out
