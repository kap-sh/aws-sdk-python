"""Generated from Smithy shape ``com.amazonaws.bcmpricingcalculator#UpdateBillEstimateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bcm_pricing_calculator.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_bcm_pricing_calculator.types.bill_estimate_name
    import aws_sdk_bcm_pricing_calculator.types.resource_id


class UpdateBillEstimateRequest(TypedDict):
    identifier: "aws_sdk_bcm_pricing_calculator.types.resource_id.ResourceId"
    """<p> The unique identifier of the bill estimate to update. </p>"""
    name: NotRequired[
        "aws_sdk_bcm_pricing_calculator.types.bill_estimate_name.BillEstimateName"
    ]
    """<p> The new name for the bill estimate. </p>"""
    expires_at: NotRequired["datetime.datetime"]
    """<p> The new expiration date for the bill estimate. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateBillEstimateRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "name" in value:
        out["name"] = value["name"]
    if "expires_at" in value:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expiresAt"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.serialize_aws_json_1_0(
                value["expires_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateBillEstimateRequest:
    out: UpdateBillEstimateRequest = {}  # type: ignore[typeddict-item]
    if "identifier" in data:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("UpdateBillEstimateRequest.identifier required")
    if "name" in data:
        out["name"] = data["name"]
    if "expiresAt" in data:
        import aws_sdk_bcm_pricing_calculator.types._prelude.timestamp

        out["expires_at"] = (
            aws_sdk_bcm_pricing_calculator.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["expiresAt"]
            )
        )
    return out
