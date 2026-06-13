"""Generated from Smithy shape ``com.amazonaws.internetmonitor#RoundTripTime``."""

from typing import TypedDict

from typing_extensions import NotRequired


class RoundTripTime(TypedDict):
    p50: NotRequired["float"]
    """<p>RTT at the 50th percentile (p50).</p>"""
    p90: NotRequired["float"]
    """<p>RTT at the 90th percentile (p90). </p>"""
    p95: NotRequired["float"]
    """<p>RTT at the 95th percentile (p95). </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RoundTripTime) -> dict:
    out: dict = {}
    if "p50" in value:
        out["P50"] = value["p50"]
    if "p90" in value:
        out["P90"] = value["p90"]
    if "p95" in value:
        out["P95"] = value["p95"]
    return out


def deserialize_json(data: dict) -> RoundTripTime:
    out: RoundTripTime = {}  # type: ignore[typeddict-item]
    if "P50" in data:
        out["p50"] = data["P50"]
    if "P90" in data:
        out["p90"] = data["P90"]
    if "P95" in data:
        out["p95"] = data["P95"]
    return out
