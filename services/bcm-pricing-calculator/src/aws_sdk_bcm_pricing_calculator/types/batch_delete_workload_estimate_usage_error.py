"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteWorkloadEstimateUsageError``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_update_usage_error_code

class BatchDeleteWorkloadEstimateUsageError(TypedDict):
    id: NotRequired["aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"]
    """<p> The ID of the error. </p>"""
    error_message: NotRequired["str"]
    """<p> The message that describes the error. </p>"""
    error_code: NotRequired["aws_sdk_bcm_pricing_calculator.types.workload_estimate_update_usage_error_code.WorkloadEstimateUpdateUsageErrorCode"]
    """<p> The code associated with the error. </p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteWorkloadEstimateUsageError) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    if "error_code" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_update_usage_error_code
        out["errorCode"] = aws_sdk_bcm_pricing_calculator.types.workload_estimate_update_usage_error_code.serialize_aws_json_1_0(value["error_code"])
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchDeleteWorkloadEstimateUsageError:
    out: BatchDeleteWorkloadEstimateUsageError = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "errorMessage" in data:
        out["error_message"] = data["errorMessage"]
    if "errorCode" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_update_usage_error_code
        out["error_code"] = aws_sdk_bcm_pricing_calculator.types.workload_estimate_update_usage_error_code.deserialize_aws_json_1_0(data["errorCode"])
    return out