"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateWorkloadEstimateUsageEntry``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.usage_group

class BatchUpdateWorkloadEstimateUsageEntry(TypedDict):
    id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the usage estimate to update. </p>"""
    group: NotRequired["aws_sdk_bcm_pricing_calculator.types.usage_group.UsageGroup"]
    """<p> The updated group identifier for the usage estimate. </p>"""
    amount: NotRequired["float"]
    """<p> The updated estimated usage amount. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateWorkloadEstimateUsageEntry) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "group" in value:
        out["group"] = value["group"]
    if "amount" in value:
        out["amount"] = value["amount"]
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateWorkloadEstimateUsageEntry:
    out: BatchUpdateWorkloadEstimateUsageEntry = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("BatchUpdateWorkloadEstimateUsageEntry.id required")
    if "group" in data:
        out["group"] = data["group"]
    if "amount" in data:
        out["amount"] = data["amount"]
    return out