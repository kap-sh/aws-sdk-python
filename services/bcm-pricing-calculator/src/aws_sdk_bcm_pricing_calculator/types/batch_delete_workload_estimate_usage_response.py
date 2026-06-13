"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchDeleteWorkloadEstimateUsageResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_errors


class BatchDeleteWorkloadEstimateUsageResponse(TypedDict):
    errors: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_errors.BatchDeleteWorkloadEstimateUsageErrors"
    ]
    """<p> Returns the list of errors reason and the usage item keys that cannot be deleted from the Workload estimate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchDeleteWorkloadEstimateUsageResponse) -> dict:
    out: dict = {}
    if "errors" in value:
        import aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_errors

        out["errors"] = (
            aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchDeleteWorkloadEstimateUsageResponse:
    out: BatchDeleteWorkloadEstimateUsageResponse = {}  # type: ignore[typeddict-item]
    if "errors" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_errors

        out["errors"] = (
            aws_sdk_bcm_pricing_calculator.types.batch_delete_workload_estimate_usage_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
