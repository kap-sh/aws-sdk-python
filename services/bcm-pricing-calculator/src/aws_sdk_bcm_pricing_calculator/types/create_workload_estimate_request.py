"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CreateWorkloadEstimateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bcm_pricing_calculator.types.client_token
    import aws_sdk_bcm_pricing_calculator.types.tags
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type


class CreateWorkloadEstimateRequest(TypedDict):
    name: "aws_sdk_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
    """<p> A descriptive name for the workload estimate. </p>"""
    client_token: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.client_token.ClientToken"
    ]
    """<p> A unique, case-sensitive identifier to ensure idempotency of the request. </p>"""
    rate_type: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"
    ]
    """<p> The type of pricing rates to use for the estimate. </p>"""
    tags: NotRequired["aws_sdk_bcm_pricing_calculator.types.tags.Tags"]
    """<p> The tags to apply to the workload estimate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkloadEstimateRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "rate_type" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rateType"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.serialize_aws_json_1_0(
                value["rate_type"]
            )
        )
    if "tags" in value:
        import aws_sdk_bcm_pricing_calculator.types.tags

        out["tags"] = aws_sdk_bcm_pricing_calculator.types.tags.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkloadEstimateRequest:
    out: CreateWorkloadEstimateRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateWorkloadEstimateRequest.name required")
    if "rateType" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rate_type"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.deserialize_aws_json_1_0(
                data["rateType"]
            )
        )
    if "tags" in data:
        import aws_sdk_bcm_pricing_calculator.types.tags

        out["tags"] = (
            aws_sdk_bcm_pricing_calculator.types.tags.deserialize_aws_json_1_0(
                data["tags"]
            )
        )
    return out
