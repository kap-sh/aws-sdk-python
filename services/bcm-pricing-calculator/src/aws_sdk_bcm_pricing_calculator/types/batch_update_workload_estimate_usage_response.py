"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchUpdateWorkloadEstimateUsageResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_errors
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_items

class BatchUpdateWorkloadEstimateUsageResponse(TypedDict):
    items: NotRequired["aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_items.WorkloadEstimateUsageItems"]
    """<p> Returns the list of successful usage line items that were updated for a Workload estimate. </p>"""
    errors: NotRequired["aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_errors.BatchUpdateWorkloadEstimateUsageErrors"]
    """<p> Returns the list of error reasons and usage line item IDs that could not be updated for the Workload estimate. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchUpdateWorkloadEstimateUsageResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_items
        out["items"] = aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_items.serialize_aws_json_1_0(value["items"])
    if "errors" in value:
        import aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_errors
        out["errors"] = aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_errors.serialize_aws_json_1_0(value["errors"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchUpdateWorkloadEstimateUsageResponse:
    out: BatchUpdateWorkloadEstimateUsageResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_items
        out["items"] = aws_sdk_bcm_pricing_calculator.types.workload_estimate_usage_items.deserialize_aws_json_1_0(data["items"])
    if "errors" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_errors
        out["errors"] = aws_sdk_bcm_pricing_calculator.types.batch_update_workload_estimate_usage_errors.deserialize_aws_json_1_0(data["errors"])
    return out