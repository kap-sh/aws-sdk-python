"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UpdateWorkloadEstimateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bcm_pricing_calculator.types.currency_code
    import aws_sdk_bcm_pricing_calculator.types.resource_id
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type
    import aws_sdk_bcm_pricing_calculator.types.workload_estimate_status


class UpdateWorkloadEstimateResponse(TypedDict):
    id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the updated workload estimate. </p>"""
    name: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.workload_estimate_name.WorkloadEstimateName"
    ]
    """<p> The updated name of the workload estimate. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the workload estimate was originally created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The updated expiration timestamp for the workload estimate. </p>"""
    rate_type: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.WorkloadEstimateRateType"
    ]
    """<p> The type of pricing rates used for the updated estimate. </p>"""
    rate_timestamp: NotRequired["datetime.datetime"]
    """<p> The timestamp of the pricing rates used for the updated estimate. </p>"""
    status: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.workload_estimate_status.WorkloadEstimateStatus"
    ]
    """<p> The current status of the updated workload estimate. </p>"""
    total_cost: NotRequired["float"]
    """<p> The updated total estimated cost for the workload. </p>"""
    cost_currency: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.currency_code.CurrencyCode"
    ]
    """<p> The currency of the updated estimated cost. </p>"""
    failure_message: NotRequired["str"]
    """<p> An error message if the workload estimate update failed. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateWorkloadEstimateResponse) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "created_at" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["createdAt"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_at"]
            )
        )
    if "expires_at" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expiresAt"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    if "rate_type" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rateType"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.serialize_aws_json_1_0(
                value["rate_type"]
            )
        )
    if "rate_timestamp" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["rateTimestamp"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["rate_timestamp"]
            )
        )
    if "status" in value:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "total_cost" in value:
        out["totalCost"] = value["total_cost"]
    if "cost_currency" in value:
        import aws_sdk_bcm_pricing_calculator.types.currency_code

        out["costCurrency"] = (
            aws_sdk_bcm_pricing_calculator.types.currency_code.serialize_aws_json_1_0(
                value["cost_currency"]
            )
        )
    if "failure_message" in value:
        out["failureMessage"] = value["failure_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateWorkloadEstimateResponse:
    out: UpdateWorkloadEstimateResponse = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("UpdateWorkloadEstimateResponse.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "createdAt" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["createdAt"]
            )
        )
    if "expiresAt" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expires_at"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    if "rateType" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type

        out["rate_type"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_rate_type.deserialize_aws_json_1_0(
                data["rateType"]
            )
        )
    if "rateTimestamp" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["rate_timestamp"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["rateTimestamp"]
            )
        )
    if "status" in data:
        import aws_sdk_bcm_pricing_calculator.types.workload_estimate_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.workload_estimate_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "totalCost" in data:
        out["total_cost"] = data["totalCost"]
    if "costCurrency" in data:
        import aws_sdk_bcm_pricing_calculator.types.currency_code

        out["cost_currency"] = (
            aws_sdk_bcm_pricing_calculator.types.currency_code.deserialize_aws_json_1_0(
                data["costCurrency"]
            )
        )
    if "failureMessage" in data:
        out["failure_message"] = data["failureMessage"]
    return out
