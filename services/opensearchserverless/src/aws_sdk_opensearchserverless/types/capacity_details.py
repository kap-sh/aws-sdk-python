"""Generated from Smithy shape ``com.amazonaws.opensearchserverless#CapacityDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_opensearchserverless.types.autoscaling_status


class CapacityDetails(TypedDict, closed=True):
    capacity_in_ocu: NotRequired["float"]
    """<p>The current capacity in OpenSearch Compute Units (OCUs).</p>"""
    autoscaling_status: NotRequired[
        "aws_sdk_opensearchserverless.types.autoscaling_status.AutoscalingStatus"
    ]
    """<p>The current autoscaling status for the collection group.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CapacityDetails) -> dict:
    out: dict = {}
    if "capacity_in_ocu" in value:
        out["capacityInOcu"] = value["capacity_in_ocu"]
    if "autoscaling_status" in value:
        out["autoscalingStatus"] = value["autoscaling_status"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CapacityDetails:
    out: CapacityDetails = {}  # type: ignore[typeddict-item]
    if "capacityInOcu" in data:
        out["capacity_in_ocu"] = data["capacityInOcu"]
    if "autoscalingStatus" in data:
        out["autoscaling_status"] = data["autoscalingStatus"]
    return out
