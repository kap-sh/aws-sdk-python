"""Generated from Smithy shape ``com.amazonaws.outposts#GetOutpostBillingInformationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_outposts.types.payment_option
    import capo_outposts.types.payment_term
    import capo_outposts.types.string
    import capo_outposts.types.subscription_list
    import capo_outposts.types.token


class GetOutpostBillingInformationOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_outposts.types.token.Token"]
    subscriptions: NotRequired["capo_outposts.types.subscription_list.SubscriptionList"]
    """<p>The subscription details for the specified Outpost.</p>"""
    contract_end_date: NotRequired["capo_outposts.types.string.String"]
    """<p>The date the current contract term ends for the specified Outpost. You must start the renewal or decommission process at least 5 business days before the current term for your Amazon Web Services Outposts ends. Failing to complete these steps at least 5 business days before the current term ends might result in unanticipated charges.</p>"""
    payment_term: NotRequired["capo_outposts.types.payment_term.PaymentTerm"]
    """<p>The payment term.</p>"""
    payment_option: NotRequired["capo_outposts.types.payment_option.PaymentOption"]
    """<p>The payment option.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetOutpostBillingInformationOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "subscriptions" in value:
        import capo_outposts.types.subscription_list

        out["Subscriptions"] = capo_outposts.types.subscription_list.serialize_json(
            value["subscriptions"]
        )
    if "contract_end_date" in value:
        out["ContractEndDate"] = value["contract_end_date"]
    if "payment_term" in value:
        import capo_outposts.types.payment_term

        out["PaymentTerm"] = capo_outposts.types.payment_term.serialize_json(
            value["payment_term"]
        )
    if "payment_option" in value:
        import capo_outposts.types.payment_option

        out["PaymentOption"] = capo_outposts.types.payment_option.serialize_json(
            value["payment_option"]
        )
    return out


def deserialize_json(data: dict) -> GetOutpostBillingInformationOutput:
    out: GetOutpostBillingInformationOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "Subscriptions" in data:
        import capo_outposts.types.subscription_list

        out["subscriptions"] = capo_outposts.types.subscription_list.deserialize_json(
            data["Subscriptions"]
        )
    if "ContractEndDate" in data:
        out["contract_end_date"] = data["ContractEndDate"]
    if "PaymentTerm" in data:
        import capo_outposts.types.payment_term

        out["payment_term"] = capo_outposts.types.payment_term.deserialize_json(
            data["PaymentTerm"]
        )
    if "PaymentOption" in data:
        import capo_outposts.types.payment_option

        out["payment_option"] = capo_outposts.types.payment_option.deserialize_json(
            data["PaymentOption"]
        )
    return out
