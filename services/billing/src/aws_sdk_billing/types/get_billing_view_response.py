"""Generated from Smithy shape ``com.amazonaws.billing#GetBillingViewResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_billing.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_billing.types.billing_view_element


class GetBillingViewResponse(TypedDict, closed=True):
    billing_view: "aws_sdk_billing.types.billing_view_element.BillingViewElement"
    """<p>The billing view element associated with the specified ARN. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetBillingViewResponse) -> dict:
    out: dict = {}
    import aws_sdk_billing.types.billing_view_element

    out["billingView"] = (
        aws_sdk_billing.types.billing_view_element.serialize_aws_json_1_0(
            value["billing_view"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetBillingViewResponse:
    out: GetBillingViewResponse = {}  # type: ignore[typeddict-item]
    if "billingView" in data:
        import aws_sdk_billing.types.billing_view_element

        out["billing_view"] = (
            aws_sdk_billing.types.billing_view_element.deserialize_aws_json_1_0(
                data["billingView"]
            )
        )
    else:
        raise DeserializationError("GetBillingViewResponse.billing_view required")
    return out
