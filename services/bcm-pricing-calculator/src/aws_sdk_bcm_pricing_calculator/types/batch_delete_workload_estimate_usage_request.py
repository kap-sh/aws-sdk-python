"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteWorkloadEstimateUsageRequest``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_bcm_pricing_calculator.errors import DeserializationError
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries
    import aws_sdk_bcm_pricing_calculator.types.resource_id

class BatchDeleteWorkloadEstimateUsageRequest(TypedDict):
    workload_estimate_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Workload estimate for which you want to delete the modeled usage. </p>"""
    ids: "aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries.BatchDeleteWorkloadEstimateUsageEntries"
    """<p> List of usage that you want to delete from the Workload estimate. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteWorkloadEstimateUsageRequest) -> dict:
    out: dict = {}
    out["workloadEstimateId"] = value["workload_estimate_id"]
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries
    out["ids"] = aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries.serialize_aws_json_1_0(value["ids"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchDeleteWorkloadEstimateUsageRequest:
    out: BatchDeleteWorkloadEstimateUsageRequest = {}  # type: ignore[typeddict-item]
    if "workloadEstimateId" in data:
        out["workload_estimate_id"] = data["workloadEstimateId"]
    else:
        raise DeserializationError("BatchDeleteWorkloadEstimateUsageRequest.workload_estimate_id required")
    if "ids" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries
        out["ids"] = aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_entries.deserialize_aws_json_1_0(data["ids"])
    else:
        raise DeserializationError("BatchDeleteWorkloadEstimateUsageRequest.ids required")
    return out