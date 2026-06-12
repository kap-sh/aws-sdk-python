"""Generated from Smithy shape ``com.amazonaws.location#CalculateRouteMatrixResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_location.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_location.types.calculate_route_matrix_summary
    import aws_sdk_location.types.position_list
    import aws_sdk_location.types.route_matrix

class CalculateRouteMatrixResponse(TypedDict):
    route_matrix: "aws_sdk_location.types.route_matrix.RouteMatrix"
    """<p>The calculated route matrix containing the results for all pairs of <code>DeparturePositions</code> to <code>DestinationPositions</code>. Each row corresponds to one entry in <code>DeparturePositions</code>. Each entry in the row corresponds to the route from that entry in <code>DeparturePositions</code> to an entry in <code>DestinationPositions</code>. </p>"""
    snapped_departure_positions: NotRequired["aws_sdk_location.types.position_list.PositionList"]
    """<p>For routes calculated using an Esri route calculator resource, departure positions are snapped to the closest road. For Esri route calculator resources, this returns the list of departure/origin positions used for calculation of the <code>RouteMatrix</code>.</p>"""
    snapped_destination_positions: NotRequired["aws_sdk_location.types.position_list.PositionList"]
    """<p>The list of destination positions for the route matrix used for calculation of the <code>RouteMatrix</code>.</p>"""
    summary: "aws_sdk_location.types.calculate_route_matrix_summary.CalculateRouteMatrixSummary"
    """<p>Contains information about the route matrix, <code>DataSource</code>, <code>DistanceUnit</code>, <code>RouteCount</code> and <code>ErrorCount</code>.</p>"""

# --- restJson1 ser/de ---
def serialize_json(value: CalculateRouteMatrixResponse) -> dict:
    out: dict = {}
    import aws_sdk_location.types.route_matrix
    out["RouteMatrix"] = aws_sdk_location.types.route_matrix.serialize_json(value["route_matrix"])
    if "snapped_departure_positions" in value:
        import aws_sdk_location.types.position_list
        out["SnappedDeparturePositions"] = aws_sdk_location.types.position_list.serialize_json(value["snapped_departure_positions"])
    if "snapped_destination_positions" in value:
        import aws_sdk_location.types.position_list
        out["SnappedDestinationPositions"] = aws_sdk_location.types.position_list.serialize_json(value["snapped_destination_positions"])
    import aws_sdk_location.types.calculate_route_matrix_summary
    out["Summary"] = aws_sdk_location.types.calculate_route_matrix_summary.serialize_json(value["summary"])
    return out


def deserialize_json(data: dict) -> CalculateRouteMatrixResponse:
    out: CalculateRouteMatrixResponse = {}  # type: ignore[typeddict-item]
    if "RouteMatrix" in data:
        import aws_sdk_location.types.route_matrix
        out["route_matrix"] = aws_sdk_location.types.route_matrix.deserialize_json(data["RouteMatrix"])
    else:
        raise DeserializationError("CalculateRouteMatrixResponse.route_matrix required")
    if "SnappedDeparturePositions" in data:
        import aws_sdk_location.types.position_list
        out["snapped_departure_positions"] = aws_sdk_location.types.position_list.deserialize_json(data["SnappedDeparturePositions"])
    if "SnappedDestinationPositions" in data:
        import aws_sdk_location.types.position_list
        out["snapped_destination_positions"] = aws_sdk_location.types.position_list.deserialize_json(data["SnappedDestinationPositions"])
    if "Summary" in data:
        import aws_sdk_location.types.calculate_route_matrix_summary
        out["summary"] = aws_sdk_location.types.calculate_route_matrix_summary.deserialize_json(data["Summary"])
    else:
        raise DeserializationError("CalculateRouteMatrixResponse.summary required")
    return out