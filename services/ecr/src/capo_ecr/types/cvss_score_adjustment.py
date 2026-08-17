"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScoreAdjustment``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ecr.types.metric
    import capo_ecr.types.reason


class CvssScoreAdjustment(TypedDict, closed=True):
    metric: NotRequired["capo_ecr.types.metric.Metric"]
    """<p>The metric used to adjust the CVSS score.</p>"""
    reason: NotRequired["capo_ecr.types.reason.Reason"]
    """<p>The reason the CVSS score has been adjustment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CvssScoreAdjustment) -> dict:
    out: dict = {}
    if "metric" in value:
        out["metric"] = value["metric"]
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CvssScoreAdjustment:
    out: CvssScoreAdjustment = {}  # type: ignore[typeddict-item]
    if data.get("metric") is not None:
        out["metric"] = data["metric"]
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    return out
