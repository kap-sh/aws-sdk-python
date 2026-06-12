"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateWorkloadEstimateUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries
    import aws_sdk_bcm_pricing_calculator.types.resource_id

class BatchUpdateWorkloadEstimateUsageRequest(TypedDict):
    workload_estimate_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Workload estimate for which you want to modify the usage lines. </p>"""
    usage: "aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries.BatchUpdateWorkloadEstimateUsageEntries"
    """<p> List of usage line amounts and usage group that you want to update in a Workload estimate identified by the usage ID. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateWorkloadEstimateUsageRequest) -> dict:
    out: dict = {}
    out["workloadEstimateId"] = value["workload_estimate_id"]
    import aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries
    out["usage"] = aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries.serialize_aws_json_1_0(value["usage"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateWorkloadEstimateUsageRequest:
    out: BatchUpdateWorkloadEstimateUsageRequest = {}  # type: ignore[typeddict-item]
    if "workloadEstimateId" in data:
        out["workload_estimate_id"] = data["workloadEstimateId"]
    else:
        raise DeserializationError("BatchUpdateWorkloadEstimateUsageRequest.workload_estimate_id required")
    if "usage" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries
        out["usage"] = aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_entries.deserialize_aws_json_1_0(data["usage"])
    else:
        raise DeserializationError("BatchUpdateWorkloadEstimateUsageRequest.usage required")
    return out