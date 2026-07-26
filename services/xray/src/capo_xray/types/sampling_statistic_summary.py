"""Generated from Smithy shape ``com.amazonaws.xray#SamplingStatisticSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_xray.types.integer
    import capo_xray.types.string
    import capo_xray.types.timestamp


class SamplingStatisticSummary(TypedDict, closed=True):
    rule_name: NotRequired["capo_xray.types.string.String"]
    """<p>The name of the sampling rule.</p>"""
    timestamp: NotRequired["capo_xray.types.timestamp.Timestamp"]
    """<p>The start time of the reporting window.</p>"""
    request_count: "capo_xray.types.integer.Integer"
    """<p>The number of requests that matched the rule.</p>"""
    borrow_count: "capo_xray.types.integer.Integer"
    """<p>The number of requests recorded with borrowed reservoir quota.</p>"""
    sampled_count: "capo_xray.types.integer.Integer"
    """<p>The number of requests recorded.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamplingStatisticSummary) -> dict:
    out: dict = {}
    if "rule_name" in value:
        out["RuleName"] = value["rule_name"]
    if "timestamp" in value:
        import capo_xray.types.timestamp

        out["Timestamp"] = capo_xray.types.timestamp.serialize_json(value["timestamp"])
    out["RequestCount"] = value.get("request_count", 0)
    out["BorrowCount"] = value.get("borrow_count", 0)
    out["SampledCount"] = value.get("sampled_count", 0)
    return out


def deserialize_json(data: dict) -> SamplingStatisticSummary:
    out: SamplingStatisticSummary = {}  # type: ignore[typeddict-item]
    if "RuleName" in data:
        out["rule_name"] = data["RuleName"]
    if "Timestamp" in data:
        import capo_xray.types.timestamp

        out["timestamp"] = capo_xray.types.timestamp.deserialize_json(data["Timestamp"])
    if "RequestCount" in data:
        out["request_count"] = data["RequestCount"]
    else:
        out["request_count"] = 0
    if "BorrowCount" in data:
        out["borrow_count"] = data["BorrowCount"]
    else:
        out["borrow_count"] = 0
    if "SampledCount" in data:
        out["sampled_count"] = data["SampledCount"]
    else:
        out["sampled_count"] = 0
    return out
