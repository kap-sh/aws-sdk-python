"""Generated from Smithy shape ``com.amazonaws.georoutes#RouteMatrixEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.route_matrix_error_code


class RouteMatrixEntry(TypedDict, closed=True):
    distance: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The total distance of travel for the route.</p>"""
    duration: "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    """<p>The expected duration of travel for the route.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    error: NotRequired[
        "aws_sdk_geo_routes.types.route_matrix_error_code.RouteMatrixErrorCode"
    ]
    """<p>Error code that occurred during calculation of the route.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RouteMatrixEntry) -> dict:
    out: dict = {}
    out["Distance"] = value.get("distance", 0)
    out["Duration"] = value.get("duration", 0)
    if "error" in value:
        import aws_sdk_geo_routes.types.route_matrix_error_code

        out["Error"] = aws_sdk_geo_routes.types.route_matrix_error_code.serialize_json(
            value["error"]
        )
    return out


def deserialize_json(data: dict) -> RouteMatrixEntry:
    out: RouteMatrixEntry = {}  # type: ignore[typeddict-item]
    if "Distance" in data:
        out["distance"] = data["Distance"]
    else:
        out["distance"] = 0
    if "Duration" in data:
        out["duration"] = data["Duration"]
    else:
        out["duration"] = 0
    if "Error" in data:
        import aws_sdk_geo_routes.types.route_matrix_error_code

        out["error"] = (
            aws_sdk_geo_routes.types.route_matrix_error_code.deserialize_json(
                data["Error"]
            )
        )
    return out
