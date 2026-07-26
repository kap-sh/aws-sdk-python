"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ScoringComponentResiliencyScore``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehub.types.double
    import capo_resiliencehub.types.long


class ScoringComponentResiliencyScore(TypedDict, closed=True):
    score: "capo_resiliencehub.types.double.Double"
    """<p>Resiliency score points given for the scoring component. The score is always less than or equal to the <code>possibleScore</code>.</p>"""
    possible_score: "capo_resiliencehub.types.double.Double"
    """<p>Maximum possible score that can be obtained for the scoring component. </p> <p>For example, if the <code>possibleScore</code> is 20 points, it indicates the maximum possible score you can achieve for the scoring component when you run a new assessment after implementing all the Resilience Hub recommendations.</p>"""
    outstanding_count: "capo_resiliencehub.types.long.Long"
    """<p>Number of recommendations that must be implemented to obtain the maximum possible score for the scoring component. For SOPs, alarms, and tests, these are the number of recommendations that must be implemented. For compliance, these are the number of Application Components that have breached the resiliency policy.</p> <p>For example, if the <code>outstandingCount</code> for Alarms coverage scoring component is 5, it indicates that 5 Amazon CloudWatch alarms need to be implemented to achieve the maximum possible score.</p>"""
    excluded_count: "capo_resiliencehub.types.long.Long"
    """<p>Number of recommendations that were excluded from the assessment.</p> <p>For example, if the <code>excludedCount</code> for Alarms coverage scoring component is 7, it indicates that 7 Amazon CloudWatch alarms are excluded from the assessment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScoringComponentResiliencyScore) -> dict:
    out: dict = {}
    out["score"] = value.get("score", 0)
    out["possibleScore"] = value.get("possible_score", 0)
    out["outstandingCount"] = value.get("outstanding_count", 0)
    out["excludedCount"] = value.get("excluded_count", 0)
    return out


def deserialize_json(data: dict) -> ScoringComponentResiliencyScore:
    out: ScoringComponentResiliencyScore = {}  # type: ignore[typeddict-item]
    if "score" in data:
        out["score"] = data["score"]
    else:
        out["score"] = 0
    if "possibleScore" in data:
        out["possible_score"] = data["possibleScore"]
    else:
        out["possible_score"] = 0
    if "outstandingCount" in data:
        out["outstanding_count"] = data["outstandingCount"]
    else:
        out["outstanding_count"] = 0
    if "excludedCount" in data:
        out["excluded_count"] = data["excludedCount"]
    else:
        out["excluded_count"] = 0
    return out
