"""Generated from Smithy shape ``com.amazonaws.billing#DeleteBillingViewResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_arn


class DeleteBillingViewResponse(TypedDict):
    arn: "aws_sdk_billing.types.billing_view_arn.BillingViewArn"
    """<p> The Amazon Resource Name (ARN) that can be used to uniquely identify the billing view. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteBillingViewResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteBillingViewResponse:
    out: DeleteBillingViewResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DeleteBillingViewResponse.arn required")
    return out
