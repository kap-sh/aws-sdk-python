"""Generated from Smithy shape ``com.amazonaws.billing#GetBillingViewRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_arn


class GetBillingViewRequest(TypedDict, closed=True):
    arn: "aws_sdk_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingViewRequest) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingViewRequest:
    out: GetBillingViewRequest = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetBillingViewRequest.arn required")
    return out
