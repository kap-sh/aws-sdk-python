"""Generated from Smithy shape ``com.amazonaws.billing#AssociateSourceViewsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.billing_view_arn


class AssociateSourceViewsResponse(TypedDict, closed=True):
    arn: "capo_billing.types.billing_view_arn.BillingViewArn"
    """<p> The ARN of the billing view that the source views were associated with. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateSourceViewsResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateSourceViewsResponse:
    out: AssociateSourceViewsResponse = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("AssociateSourceViewsResponse.arn required")
    return out
