"""Generated from Smithy shape ``com.amazonaws.costoptimizationhub#MetricsByTime``."""

from typing import TypedDict

from typing_extensions import NotRequired


class MetricsByTime(TypedDict):
    score: NotRequired["float"]
    """<p>The efficiency score for this time period. The score represents a measure of how effectively the cloud resources are being optimized, with higher scores indicating better optimization performance.</p>"""
    savings: NotRequired["float"]
    """<p>The estimated savings amount for this time period, representing the potential cost reduction achieved through optimization recommendations.</p>"""
    spend: NotRequired["float"]
    """<p>The total spending amount for this time period.</p>"""
    timestamp: NotRequired["str"]
    """<p>The timestamp for this data point. The format depends on the granularity: YYYY-MM-DD for daily metrics, or YYYY-MM for monthly metrics.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MetricsByTime) -> dict:
    out: dict = {}
    if "score" in value:
        out["score"] = value["score"]
    if "savings" in value:
        out["savings"] = value["savings"]
    if "spend" in value:
        out["spend"] = value["spend"]
    if "timestamp" in value:
        out["timestamp"] = value["timestamp"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MetricsByTime:
    out: MetricsByTime = {}  # type: ignore[typeddict-item]
    if "score" in data:
        out["score"] = data["score"]
    if "savings" in data:
        out["savings"] = data["savings"]
    if "spend" in data:
        out["spend"] = data["spend"]
    if "timestamp" in data:
        out["timestamp"] = data["timestamp"]
    return out
