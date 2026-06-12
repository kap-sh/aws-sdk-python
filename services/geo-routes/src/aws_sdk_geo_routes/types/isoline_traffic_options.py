"""Generated from Smithy shape ``com.amazonaws.georoutes#IsolineTrafficOptions``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_geo_routes.types.duration_seconds
    import aws_sdk_geo_routes.types.traffic_usage


class IsolineTrafficOptions(TypedDict):
    flow_event_threshold_override: (
        "aws_sdk_geo_routes.types.duration_seconds.DurationSeconds"
    )
    """<p>The duration in seconds that real-time congestion data is considered valid before reverting to historical traffic patterns. This helps balance between using current conditions and more predictable historical data when calculating travel times.</p> <p> <b>Unit</b>: <code>seconds</code> </p>"""
    usage: NotRequired["aws_sdk_geo_routes.types.traffic_usage.TrafficUsage"]
    """<p>Controls whether traffic data is used in calculations. <code>UseTrafficData</code> considers both real-time congestion and historical patterns, while <code>IgnoreTrafficData</code> calculates routes based solely on road types and speed limits. Using traffic data provides more accurate real-world estimates but may produce different results at different times of day.</p> <p>Default value: <code>UseTrafficData</code> </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IsolineTrafficOptions) -> dict:
    out: dict = {}
    out["FlowEventThresholdOverride"] = value.get("flow_event_threshold_override", 0)
    if "usage" in value:
        import aws_sdk_geo_routes.types.traffic_usage

        out["Usage"] = aws_sdk_geo_routes.types.traffic_usage.serialize_json(
            value["usage"]
        )
    return out


def deserialize_json(data: dict) -> IsolineTrafficOptions:
    out: IsolineTrafficOptions = {}  # type: ignore[typeddict-item]
    if "FlowEventThresholdOverride" in data:
        out["flow_event_threshold_override"] = data["FlowEventThresholdOverride"]
    else:
        out["flow_event_threshold_override"] = 0
    if "Usage" in data:
        import aws_sdk_geo_routes.types.traffic_usage

        out["usage"] = aws_sdk_geo_routes.types.traffic_usage.deserialize_json(
            data["Usage"]
        )
    return out
