"""Generated from Smithy shape ``com.amazonaws.codegurusecurity#FindingMetricsValuePerSeverity``."""

from typing import TypedDict

from typing_extensions import NotRequired


class FindingMetricsValuePerSeverity(TypedDict):
    info: NotRequired["float"]
    """<p>A numeric value corresponding to an informational finding.</p>"""
    low: NotRequired["float"]
    """<p>A numeric value corresponding to a low severity finding.</p>"""
    medium: NotRequired["float"]
    """<p>A numeric value corresponding to a medium severity finding.</p>"""
    high: NotRequired["float"]
    """<p>A numeric value corresponding to a high severity finding.</p>"""
    critical: NotRequired["float"]
    """<p>A numeric value corresponding to a critical finding.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FindingMetricsValuePerSeverity) -> dict:
    out: dict = {}
    if "info" in value:
        out["info"] = value["info"]
    if "low" in value:
        out["low"] = value["low"]
    if "medium" in value:
        out["medium"] = value["medium"]
    if "high" in value:
        out["high"] = value["high"]
    if "critical" in value:
        out["critical"] = value["critical"]
    return out


def deserialize_json(data: dict) -> FindingMetricsValuePerSeverity:
    out: FindingMetricsValuePerSeverity = {}  # type: ignore[typeddict-item]
    if "info" in data:
        out["info"] = data["info"]
    if "low" in data:
        out["low"] = data["low"]
    if "medium" in data:
        out["medium"] = data["medium"]
    if "high" in data:
        out["high"] = data["high"]
    if "critical" in data:
        out["critical"] = data["critical"]
    return out
