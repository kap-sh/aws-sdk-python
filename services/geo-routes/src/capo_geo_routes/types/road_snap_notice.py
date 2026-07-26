"""Generated from Smithy shape ``com.amazonaws.georoutes#RoadSnapNotice``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_geo_routes.errors import DeserializationError

if TYPE_CHECKING:
    import capo_geo_routes.types.road_snap_notice_code
    import capo_geo_routes.types.road_snap_trace_point_index_list
    import capo_geo_routes.types.sensitive_string


class RoadSnapNotice(TypedDict, closed=True):
    code: "capo_geo_routes.types.road_snap_notice_code.RoadSnapNoticeCode"
    """<p>Code corresponding to the issue.</p>"""
    title: "capo_geo_routes.types.sensitive_string.SensitiveString"
    """<p>The notice title.</p>"""
    trace_point_indexes: "capo_geo_routes.types.road_snap_trace_point_index_list.RoadSnapTracePointIndexList"
    """<p>TracePoint indices for which the provided notice code corresponds to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoadSnapNotice) -> dict:
    out: dict = {}
    import capo_geo_routes.types.road_snap_notice_code

    out["Code"] = capo_geo_routes.types.road_snap_notice_code.serialize_json(
        value["code"]
    )
    out["Title"] = value["title"]
    import capo_geo_routes.types.road_snap_trace_point_index_list

    out["TracePointIndexes"] = (
        capo_geo_routes.types.road_snap_trace_point_index_list.serialize_json(
            value["trace_point_indexes"]
        )
    )
    return out


def deserialize_json(data: dict) -> RoadSnapNotice:
    out: RoadSnapNotice = {}  # type: ignore[typeddict-item]
    if "Code" in data:
        import capo_geo_routes.types.road_snap_notice_code

        out["code"] = capo_geo_routes.types.road_snap_notice_code.deserialize_json(
            data["Code"]
        )
    else:
        raise DeserializationError("RoadSnapNotice.code required")
    if "Title" in data:
        out["title"] = data["Title"]
    else:
        raise DeserializationError("RoadSnapNotice.title required")
    if "TracePointIndexes" in data:
        import capo_geo_routes.types.road_snap_trace_point_index_list

        out["trace_point_indexes"] = (
            capo_geo_routes.types.road_snap_trace_point_index_list.deserialize_json(
                data["TracePointIndexes"]
            )
        )
    else:
        raise DeserializationError("RoadSnapNotice.trace_point_indexes required")
    return out
