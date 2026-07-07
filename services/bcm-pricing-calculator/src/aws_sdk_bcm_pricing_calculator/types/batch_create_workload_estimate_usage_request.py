"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BatchCreateWorkloadEstimateUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries
    import aws_sdk_bcm_pricing_calculator.types.client_token
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class BatchCreateWorkloadEstimateUsageRequest(TypedDict, closed=True):
    workload_estimate_id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The ID of the Workload estimate for which you want to create the modeled usage. </p>"""
    usage: "aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries.BatchCreateWorkloadEstimateUsageEntries"
    """<p> List of usage that you want to model in the Workload estimate. </p>"""
    client_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BatchCreateWorkloadEstimateUsageRequest) -> dict:
    out: dict = {}
    out["workloadEstimateId"] = value["workload_estimate_id"]
    import aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries

    out["usage"] = (
        aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries.serialize_aws_json_1_0(
            value["usage"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> BatchCreateWorkloadEstimateUsageRequest:
    out: BatchCreateWorkloadEstimateUsageRequest = {}  # type: ignore[typeddict-item]
    if "workloadEstimateId" in data:
        out["workload_estimate_id"] = data["workloadEstimateId"]
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageRequest.workload_estimate_id required"
        )
    if "usage" in data:
        import aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries

        out["usage"] = (
            aws_sdk_bcm_pricing_calculator.types.batch_create_workload_estimate_usage_entries.deserialize_aws_json_1_0(
                data["usage"]
            )
        )
    else:
        raise DeserializationError(
            "BatchCreateWorkloadEstimateUsageRequest.usage required"
        )
    return out
