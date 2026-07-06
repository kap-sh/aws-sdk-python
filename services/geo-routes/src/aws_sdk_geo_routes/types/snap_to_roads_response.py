"""Generated from Smithy shape ``com.amazonaws.georoutes#SnapToRoadsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.geometry_format
    import aws_sdk_geo_routes.types.road_snap_notice_list
    import aws_sdk_geo_routes.types.road_snap_snapped_geometry
    import aws_sdk_geo_routes.types.road_snap_snapped_trace_point_list


class SnapToRoadsResponse(TypedDict, closed=True):
    notices: "aws_sdk_geo_routes.types.road_snap_notice_list.RoadSnapNoticeList"
    """<p>Notices are additional information returned that indicate issues that occurred during route calculation.</p>"""
    pricing_bucket: "str"
    """<p>The pricing bucket for which the query is charged at.</p>"""
    snapped_geometry: NotRequired[
        "aws_sdk_geo_routes.types.road_snap_snapped_geometry.RoadSnapSnappedGeometry"
    ]
    """<p>The interpolated geometry for the snapped route onto the road network.</p>"""
    snapped_geometry_format: "aws_sdk_geo_routes.types.geometry_format.GeometryFormat"
    """<p>Specifies the format of the geometry returned for each leg of the route.</p>"""
    snapped_trace_points: "aws_sdk_geo_routes.types.road_snap_snapped_trace_point_list.RoadSnapSnappedTracePointList"
    """<p>The trace points snapped onto the road network. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SnapToRoadsResponse) -> dict:
    out: dict = {}
    import aws_sdk_geo_routes.types.road_snap_notice_list

    out["Notices"] = aws_sdk_geo_routes.types.road_snap_notice_list.serialize_json(
        value["notices"]
    )
    if "snapped_geometry" in value:
        import aws_sdk_geo_routes.types.road_snap_snapped_geometry

        out["SnappedGeometry"] = (
            aws_sdk_geo_routes.types.road_snap_snapped_geometry.serialize_json(
                value["snapped_geometry"]
            )
        )
    import aws_sdk_geo_routes.types.geometry_format

    out["SnappedGeometryFormat"] = (
        aws_sdk_geo_routes.types.geometry_format.serialize_json(
            value["snapped_geometry_format"]
        )
    )
    import aws_sdk_geo_routes.types.road_snap_snapped_trace_point_list

    out["SnappedTracePoints"] = (
        aws_sdk_geo_routes.types.road_snap_snapped_trace_point_list.serialize_json(
            value["snapped_trace_points"]
        )
    )
    return out


def deserialize_json(data: dict) -> SnapToRoadsResponse:
    out: SnapToRoadsResponse = {}  # type: ignore[typeddict-item]
    if "Notices" in data:
        import aws_sdk_geo_routes.types.road_snap_notice_list

        out["notices"] = (
            aws_sdk_geo_routes.types.road_snap_notice_list.deserialize_json(
                data["Notices"]
            )
        )
    else:
        raise DeserializationError("SnapToRoadsResponse.notices required")
    if "SnappedGeometry" in data:
        import aws_sdk_geo_routes.types.road_snap_snapped_geometry

        out["snapped_geometry"] = (
            aws_sdk_geo_routes.types.road_snap_snapped_geometry.deserialize_json(
                data["SnappedGeometry"]
            )
        )
    if "SnappedGeometryFormat" in data:
        import aws_sdk_geo_routes.types.geometry_format

        out["snapped_geometry_format"] = (
            aws_sdk_geo_routes.types.geometry_format.deserialize_json(
                data["SnappedGeometryFormat"]
            )
        )
    else:
        raise DeserializationError(
            "SnapToRoadsResponse.snapped_geometry_format required"
        )
    if "SnappedTracePoints" in data:
        import aws_sdk_geo_routes.types.road_snap_snapped_trace_point_list

        out["snapped_trace_points"] = (
            aws_sdk_geo_routes.types.road_snap_snapped_trace_point_list.deserialize_json(
                data["SnappedTracePoints"]
            )
        )
    else:
        raise DeserializationError("SnapToRoadsResponse.snapped_trace_points required")
    return out
