"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostBillingInformationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_outposts.types.payment_option
    import aws_sdk_outposts.types.payment_term
    import aws_sdk_outposts.types.string
    import aws_sdk_outposts.types.subscription_list
    import aws_sdk_outposts.types.token


class GetOutpostBillingInformationOutput(TypedDict):
    next_token: NotRequired["aws_sdk_outposts.types.token.Token"]
    subscriptions: NotRequired[
        "aws_sdk_outposts.types.subscription_list.SubscriptionList"
    ]
    """<p>The subscription details for the specified Outpost.</p>"""
    contract_end_date: NotRequired["aws_sdk_outposts.types.string.String"]
    """<p>The date the current contract term ends for the specified Outpost. You must start the renewal or decommission process at least 5 business days before the current term for your Amazon Web Services Outposts ends. Failing to complete these steps at least 5 business days before the current term ends might result in unanticipated charges.</p>"""
    payment_term: NotRequired["aws_sdk_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment term.</p>"""
    payment_option: NotRequired["aws_sdk_outposts.types.payment_option.PaymentOption"]
    """<p>The payment option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostBillingInformationOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "subscriptions" in value:
        import aws_sdk_outposts.types.subscription_list

        out["Subscriptions"] = aws_sdk_outposts.types.subscription_list.serialize_json(
            value["subscriptions"]
        )
    if "contract_end_date" in value:
        out["ContractEndDate"] = value["contract_end_date"]
    if "payment_term" in value:
        import aws_sdk_outposts.types.payment_term

        out["PaymentTerm"] = aws_sdk_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    if "payment_option" in value:
        import aws_sdk_outposts.types.payment_option

        out["PaymentOption"] = aws_sdk_outposts.types.payment_option.serialize_json(
            value["payment_option"]
        )
    return out


def deserialize_json(data: dict) -> GetOutpostBillingInformationOutput:
    out: GetOutpostBillingInformationOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Subscriptions" in data:
        import aws_sdk_outposts.types.subscription_list

        out["subscriptions"] = (
            aws_sdk_outposts.types.subscription_list.deserialize_json(
                data["Subscriptions"]
            )
        )
    if "ContractEndDate" in data:
        out["contract_end_date"] = data["ContractEndDate"]
    if "PaymentTerm" in data:
        import aws_sdk_outposts.types.payment_term

        out["payment_term"] = aws_sdk_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    if "PaymentOption" in data:
        import aws_sdk_outposts.types.payment_option

        out["payment_option"] = aws_sdk_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    return out
