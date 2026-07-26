"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#CreateWorkloadEstimateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_bcm_pricing_calculator.types.currency_code
    import capo_bcm_pricing_calculator.types.resource_id
    import capo_bcm_pricing_calculator.types.workload_estimate_name
    import capo_bcm_pricing_calculator.types.workload_estimate_rate_type
    import capo_bcm_pricing_calculator.types.workload_estimate_status


class CreateWorkloadEstimateResponse(TypedDict, closed=True):
    id: "capo_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier for the created workload estimate. </p>"""
    name: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
    ]
    """<p> The name of the created workload estimate. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the workload estimate was created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the workload estimate will expire. </p>"""
    rate_type: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"
    ]
    """<p> The type of pricing rates used for the estimate. </p>"""
    rate_timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp of the pricing rates used for the estimate. </p>"""
    status: NotRequired[
        "capo_bcm_pricing_calculator.types.workload_estimate_status.WorkloadEstimateStatus"
    ]
    """<p> The current status of the workload estimate. </p>"""
    total_cost: NotRequired["float"]
    """<p> The total estimated cost for the workload. </p>"""
    cost_currency: NotRequired[
        "capo_bcm_pricing_calculator.types.currency_code.CurrencyCode"
    ]
    """<p> The currency of the estimated cost. </p>"""
    failure_message: NotRequired["str"]
    """<p> An error message if the workload estimate creation failed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateWorkloadEstimateResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "created_at" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["createdAt"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "expires_at" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["expiresAt"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    if "rate_type" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rateType"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_rate_type.serialize_aws_json_1_0(
                value["rate_type"]
            )
        )
    if "rate_timestamp" in value:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["rateTimestamp"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["rate_timestamp"]
            )
        )
    if "status" in value:
        import capo_bcm_pricing_calculator.types.workload_estimate_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "total_cost" in value:
        out["totalCost"] = value["total_cost"]
    if "cost_currency" in value:
        import capo_bcm_pricing_calculator.types.currency_code

        out["costCurrency"] = (
            capo_bcm_pricing_calculator.types.currency_code.serialize_aws_json_1_0(
                value["cost_currency"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateWorkloadEstimateResponse:
    out: CreateWorkloadEstimateResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateWorkloadEstimateResponse.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "createdAt" in data:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["created_at"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "expiresAt" in data:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["expires_at"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    if "rateType" in data:
        import capo_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rate_type"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_rate_type.deserialize_aws_json_1_0(
                data["rateType"]
            )
        )
    if "rateTimestamp" in data:
        import capo_bcm_pricing_calculator.types._prelude.timestamp

        out["rate_timestamp"] = (
            capo_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["rateTimestamp"]
            )
        )
    if "status" in data:
        import capo_bcm_pricing_calculator.types.workload_estimate_status

        out["status"] = (
            capo_bcm_pricing_calculator.types.workload_estimate_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "totalCost" in data:
        out["total_cost"] = data["totalCost"]
    if "costCurrency" in data:
        import capo_bcm_pricing_calculator.types.currency_code

        out["cost_currency"] = (
            capo_bcm_pricing_calculator.types.currency_code.deserialize_aws_json_1_0(
                data["costCurrency"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
