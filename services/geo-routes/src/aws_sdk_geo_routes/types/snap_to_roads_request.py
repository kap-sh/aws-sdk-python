"""Generated from Smithy shape ``com.amazonaws.georoutes#SnapToRoadsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.api_key
    import aws_sdk_geo_routes.types.distance_meters
    import aws_sdk_geo_routes.types.geometry_format
    import aws_sdk_geo_routes.types.road_snap_trace_point_list
    import aws_sdk_geo_routes.types.road_snap_travel_mode
    import aws_sdk_geo_routes.types.road_snap_travel_mode_options


class SnapToRoadsRequest(TypedDict, closed=True):
    key: NotRequired["aws_sdk_geo_routes.types.api_key.ApiKey"]
    """<p>Optional: The API key to be used for authorization. Either an API key or valid SigV4 signature must be provided when making a request. </p>"""
    snapped_geometry_format: NotRequired[
        "aws_sdk_geo_routes.types.geometry_format.GeometryFormat"
    ]
    """<p>Chooses what the returned SnappedGeometry format should be.</p> <p>Default value: <code>FlexiblePolyline</code> </p>"""
    snap_radius: "aws_sdk_geo_routes.types.distance_meters.DistanceMeters"
    """<p>The radius around the provided tracepoint that is considered for snapping.</p> <p> <b>Unit</b>: <code>meters</code> </p> <p>Default value: <code>300</code> </p>"""
    trace_points: (
        "aws_sdk_geo_routes.types.road_snap_trace_point_list.RoadSnapTracePointList"
    )
    """<p>List of trace points to be snapped onto the road network.</p>"""
    travel_mode: NotRequired[
        "aws_sdk_geo_routes.types.road_snap_travel_mode.RoadSnapTravelMode"
    ]
    """<p>Specifies the mode of transport when calculating a route. Used in estimating the speed of travel and road compatibility.</p> <p>Default value: <code>Car</code> </p>"""
    travel_mode_options: NotRequired[
        "aws_sdk_geo_routes.types.road_snap_travel_mode_options.RoadSnapTravelModeOptions"
    ]
    """<p>Travel mode related options for the provided travel mode.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapToRoadsRequest) -> dict:
    out: dict = {}
    if "snapped_geometry_format" in value:
        import aws_sdk_geo_routes.types.geometry_format

        out["SnappedGeometryFormat"] = (
            aws_sdk_geo_routes.types.geometry_format.serialize_json(
                value["snapped_geometry_format"]
            )
        )
    out["SnapRadius"] = value.get("snap_radius", 0)
    import aws_sdk_geo_routes.types.road_snap_trace_point_list

    out["TracePoints"] = (
        aws_sdk_geo_routes.types.road_snap_trace_point_list.serialize_json(
            value["trace_points"]
        )
    )
    if "travel_mode" in value:
        import aws_sdk_geo_routes.types.road_snap_travel_mode

        out["TravelMode"] = (
            aws_sdk_geo_routes.types.road_snap_travel_mode.serialize_json(
                value["travel_mode"]
            )
        )
    if "travel_mode_options" in value:
        import aws_sdk_geo_routes.types.road_snap_travel_mode_options

        out["TravelModeOptions"] = (
            aws_sdk_geo_routes.types.road_snap_travel_mode_options.serialize_json(
                value["travel_mode_options"]
            )
        )
    return out


def deserialize_json(data: dict) -> SnapToRoadsRequest:
    out: SnapToRoadsRequest = {}  # type: ignore[typeddict-item]
    if "SnappedGeometryFormat" in data:
        import aws_sdk_geo_routes.types.geometry_format

        out["snapped_geometry_format"] = (
            aws_sdk_geo_routes.types.geometry_format.deserialize_json(
                data["SnappedGeometryFormat"]
            )
        )
    if "SnapRadius" in data:
        out["snap_radius"] = data["SnapRadius"]
    else:
        out["snap_radius"] = 0
    if "TracePoints" in data:
        import aws_sdk_geo_routes.types.road_snap_trace_point_list

        out["trace_points"] = (
            aws_sdk_geo_routes.types.road_snap_trace_point_list.deserialize_json(
                data["TracePoints"]
            )
        )
    else:
        raise DeserializationError("SnapToRoadsRequest.trace_points required")
    if "TravelMode" in data:
        import aws_sdk_geo_routes.types.road_snap_travel_mode

        out["travel_mode"] = (
            aws_sdk_geo_routes.types.road_snap_travel_mode.deserialize_json(
                data["TravelMode"]
            )
        )
    if "TravelModeOptions" in data:
        import aws_sdk_geo_routes.types.road_snap_travel_mode_options

        out["travel_mode_options"] = (
            aws_sdk_geo_routes.types.road_snap_travel_mode_options.deserialize_json(
                data["TravelModeOptions"]
            )
        )
    return out
