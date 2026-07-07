"""Generated from Smithy shape ``com.amazonaws.georoutes#WaypointOptimizationOptimizedWaypoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.cluster_index
    import aws_sdk_geo_routes.types.position
    import aws_sdk_geo_routes.types.timestamp_with_timezone_offset
    import aws_sdk_geo_routes.types.waypoint_id


class WaypointOptimizationOptimizedWaypoint(TypedDict, closed=True):
    arrival_time: NotRequired[
        "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    ]
    """<p>Estimated time of arrival at the destination.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    cluster_index: NotRequired["aws_sdk_geo_routes.types.cluster_index.ClusterIndex"]
    """<p>Index of the cluster the waypoint is associated with. The index is included in the response only if clustering was performed while processing the request.</p>"""
    departure_time: "aws_sdk_geo_routes.types.timestamp_with_timezone_offset.TimestampWithTimezoneOffset"
    """<p>Estimated time of departure from the origin.</p> <p>Time format:<code>YYYY-MM-DDThh:mm:ss.sssZ | YYYY-MM-DDThh:mm:ss.sss+hh:mm</code> </p> <p>Examples:</p> <p> <code>2020-04-22T17:57:24Z</code> </p> <p> <code>2020-04-22T17:57:24+02:00</code> </p>"""
    id: "aws_sdk_geo_routes.types.waypoint_id.WaypointId"
    """<p>The waypoint Id.</p>"""
    position: "aws_sdk_geo_routes.types.position.Position"
    """<p>Position in World Geodetic System (WGS 84) format: [longitude, latitude].</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WaypointOptimizationOptimizedWaypoint) -> dict:
    out: dict = {}
    if "arrival_time" in value:
        out["ArrivalTime"] = value["arrival_time"]
    if "cluster_index" in value:
        out["ClusterIndex"] = value["cluster_index"]
    out["DepartureTime"] = value["departure_time"]
    out["Id"] = value["id"]
    import aws_sdk_geo_routes.types.position

    out["Position"] = aws_sdk_geo_routes.types.position.serialize_json(
        value["position"]
    )
    return out


def deserialize_json(data: dict) -> WaypointOptimizationOptimizedWaypoint:
    out: WaypointOptimizationOptimizedWaypoint = {}  # type: ignore[typeddict-item]
    if "ArrivalTime" in data:
        out["arrival_time"] = data["ArrivalTime"]
    if "ClusterIndex" in data:
        out["cluster_index"] = data["ClusterIndex"]
    if "DepartureTime" in data:
        out["departure_time"] = data["DepartureTime"]
    else:
        raise DeserializationError(
            "WaypointOptimizationOptimizedWaypoint.departure_time required"
        )
    if "Id" in data:
        out["id"] = data["Id"]
    else:
        raise DeserializationError("WaypointOptimizationOptimizedWaypoint.id required")
    if "Position" in data:
        import aws_sdk_geo_routes.types.position

        out["position"] = aws_sdk_geo_routes.types.position.deserialize_json(
            data["Position"]
        )
    else:
        raise DeserializationError(
            "WaypointOptimizationOptimizedWaypoint.position required"
        )
    return out
