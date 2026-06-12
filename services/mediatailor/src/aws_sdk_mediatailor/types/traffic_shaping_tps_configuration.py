"""Generated from Smithy shape ``com.amazonaws.mediatailor#TrafficShapingTpsConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mediatailor.types.__integer


class TrafficShapingTpsConfiguration(TypedDict):
    peak_tps: NotRequired["aws_sdk_mediatailor.types.__integer.__integer"]
    """<p>The maximum number of transactions per second (TPS) that your ad decision server (ADS) can handle. MediaTailor uses this value along with concurrent users and headroom multiplier to calculate optimal traffic distribution and prevent ADS overload.</p>"""
    peak_concurrent_users: NotRequired["aws_sdk_mediatailor.types.__integer.__integer"]
    """<p>The expected peak number of concurrent viewers for your content. MediaTailor uses this value along with peak TPS to determine how to distribute prefetch requests across the available capacity without exceeding your ADS limits.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TrafficShapingTpsConfiguration) -> dict:
    out: dict = {}
    if "peak_tps" in value:
        out["PeakTps"] = value["peak_tps"]
    if "peak_concurrent_users" in value:
        out["PeakConcurrentUsers"] = value["peak_concurrent_users"]
    return out


def deserialize_json(data: dict) -> TrafficShapingTpsConfiguration:
    out: TrafficShapingTpsConfiguration = {}  # type: ignore[typeddict-item]
    if "PeakTps" in data:
        out["peak_tps"] = data["PeakTps"]
    if "PeakConcurrentUsers" in data:
        out["peak_concurrent_users"] = data["PeakConcurrentUsers"]
    return out
