"""Generated from Smithy shape ``com.amazonaws.billing#DisassociateSourceViewsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn


class DisassociateSourceViewsResponse(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The ARN of the billing view that the source views were disassociated from. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateSourceViewsResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateSourceViewsResponse:
    out: DisassociateSourceViewsResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("DisassociateSourceViewsResponse.arn required")
    return out
