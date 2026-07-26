"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_errors
    import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_items


class BatchCreateWorkloadEstimateUsageResponse(TypedDict, closed=True):
    items: NotRequired[
        "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_items.BatchCreateWorkloadEstimateUsageItems"
    ]
    """<p> Returns the list of successful usage line items that were created for the Workload estimate. </p>"""
    errors: NotRequired[
        "capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_errors.BatchCreateWorkloadEstimateUsageErrors"
    ]
    """<p> Returns the list of errors reason and the usage item keys that cannot be created in the Workload estimate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_items.serialize_aws_json_1_0(
                value["items"]
            )
        )
    if "errors" in value:
        import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_errors

        out["errors"] = (
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_errors.serialize_aws_json_1_0(
                value["errors"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateWorkloadEstimateUsageResponse:
    out: BatchCreateWorkloadEstimateUsageResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_items

        out["items"] = (
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_items.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    if "errors" in data:
        import capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_errors

        out["errors"] = (
            capo_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_errors.deserialize_aws_json_1_0(
                data["errors"]
            )
        )
    return out
