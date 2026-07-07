"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#BillEstimateSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_status
    import aws_sdk_bcm_pricing_calculator.types.bill_interval
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class BillEstimateSummary(TypedDict, closed=True):
    id: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill estimate. </p>"""
    name: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
    ]
    """<p> The name of the bill estimate. </p>"""
    status: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_estimate_status.BillEstimateStatus"
    ]
    """<p> The current status of the bill estimate. </p>"""
    bill_interval: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_interval.BillInterval"
    ]
    """<p> The time period covered by the bill estimate. </p>"""
    created_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill estimate was created. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The timestamp when the bill estimate will expire. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BillEstimateSummary) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    if "status" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "bill_interval" in value:
        import aws_sdk_bcm_pricing_calculator.types.bill_interval

        out["billInterval"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_interval.serialize_aws_json_1_0(
                value["bill_interval"]
            )
        )
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
    return out


def deserialize_aws_json_1_0(data: dict) -> BillEstimateSummary:
    out: BillEstimateSummary = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("BillEstimateSummary.id required")
    if "name" in data:
        out["name"] = data["name"]
    if "status" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_estimate_status

        out["status"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_estimate_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "billInterval" in data:
        import aws_sdk_bcm_pricing_calculator.types.bill_interval

        out["bill_interval"] = (
            aws_sdk_bcm_pricing_calculator.types.bill_interval.deserialize_aws_json_1_0(
                data["billInterval"]
            )
        )
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
    return out
