"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapTracePointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.road_snap_trace_point

RoadSnapTracePointList: TypeAlias = list[
    "aws_sdk_geo_routes.types.road_snap_trace_point.RoadSnapTracePoint"
]


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapTracePointList) -> list:
    import aws_sdk_geo_routes.types.road_snap_trace_point

    out: list = []
    for item in value:
        out.append(aws_sdk_geo_routes.types.road_snap_trace_point.serialize_json(item))
    return out


def deserialize_json(data: list) -> RoadSnapTracePointList:
    import aws_sdk_geo_routes.types.road_snap_trace_point

    out: RoadSnapTracePointList = []
    for item in data:
        out.append(
            aws_sdk_geo_routes.types.road_snap_trace_point.deserialize_json(item)
        )
    return out
