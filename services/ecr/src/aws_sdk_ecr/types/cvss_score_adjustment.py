"""Generated from Smithy shape ``com.amazonaws.ecr#CvssScoreAdjustment``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ecr.types.metric
    import aws_sdk_ecr.types.reason


class CvssScoreAdjustment(TypedDict):
    metric: NotRequired["aws_sdk_ecr.types.metric.Metric"]
    """<p>The metric used to adjust the CVSS score.</p>"""
    reason: NotRequired["aws_sdk_ecr.types.reason.Reason"]
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
    if "metric" in data:
        out["metric"] = data["metric"]
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
