"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#PerformanceTarget``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_redshift_serverless.types.performance_target_status


class PerformanceTarget(TypedDict):
    status: NotRequired[
        "aws_sdk_redshift_serverless.types.performance_target_status.PerformanceTargetStatus"
    ]
    """<p>Whether the price performance target is enabled for the workgroup.</p>"""
    level: NotRequired["int"]
    """<p>The target price performance level for the workgroup. Valid values include 1, 25, 50, 75, and 100. These correspond to the price performance levels LOW_COST, ECONOMICAL, BALANCED, RESOURCEFUL, and HIGH_PERFORMANCE.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PerformanceTarget) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    if "level" in value:
        out["level"] = value["level"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PerformanceTarget:
    out: PerformanceTarget = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    if "level" in data:
        out["level"] = data["level"]
    return out
