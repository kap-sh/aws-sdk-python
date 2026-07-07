"""Generated from Smithy shape ``com.amazonaws.georoutes#CalculateRouteMatrixResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.route_matrix
    import aws_sdk_geo_routes.types.route_matrix_boundary


class CalculateRouteMatrixResponse(TypedDict, closed=True):
    error_count: "int"
    """<p>The count of error results in the route matrix. If this number is 0, all routes were calculated successfully.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p>"""
    route_matrix: "aws_sdk_geo_routes.types.route_matrix.RouteMatrix"
    """<p>The calculated route matrix containing the results for all pairs of Origins to Destination positions. Each row corresponds to one entry in Origins. Each entry in the row corresponds to the route from that entry in Origins to an entry in Destination positions.</p>"""
    routing_boundary: (
        "aws_sdk_geo_routes.types.route_matrix_boundary.RouteMatrixBoundary"
    )
    """<p>Boundary within which the matrix is to be calculated. All data, origins and destinations outside the boundary are considered invalid.</p> <note> <p>When <code>AutoCircle</code> is set in the request, the response routing boundary will return <code>Circle</code> derived from the <code>AutoCircle</code> settings.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteMatrixResponse) -> dict:
    out: dict = {}
    out["ErrorCount"] = value["error_count"]
    import aws_sdk_geo_routes.types.route_matrix

    out["RouteMatrix"] = aws_sdk_geo_routes.types.route_matrix.serialize_json(
        value["route_matrix"]
    )
    import aws_sdk_geo_routes.types.route_matrix_boundary

    out["RoutingBoundary"] = (
        aws_sdk_geo_routes.types.route_matrix_boundary.serialize_json(
            value["routing_boundary"]
        )
    )
    return out


def deserialize_json(data: dict) -> CalculateRouteMatrixResponse:
    out: CalculateRouteMatrixResponse = {}  # type: ignore[typeddict-item]
    if "ErrorCount" in data:
        out["error_count"] = data["ErrorCount"]
    else:
        raise DeserializationError("CalculateRouteMatrixResponse.error_count required")
    if "RouteMatrix" in data:
        import aws_sdk_geo_routes.types.route_matrix

        out["route_matrix"] = aws_sdk_geo_routes.types.route_matrix.deserialize_json(
            data["RouteMatrix"]
        )
    else:
        raise DeserializationError("CalculateRouteMatrixResponse.route_matrix required")
    if "RoutingBoundary" in data:
        import aws_sdk_geo_routes.types.route_matrix_boundary

        out["routing_boundary"] = (
            aws_sdk_geo_routes.types.route_matrix_boundary.deserialize_json(
                data["RoutingBoundary"]
            )
        )
    else:
        raise DeserializationError(
            "CalculateRouteMatrixResponse.routing_boundary required"
        )
    return out
