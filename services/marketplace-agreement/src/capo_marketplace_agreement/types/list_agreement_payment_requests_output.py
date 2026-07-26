"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementPaymentRequestsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.next_token
    import capo_marketplace_agreement.types.payment_request_summary_list


class ListAgreementPaymentRequestsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""
    items: "capo_marketplace_agreement.types.payment_request_summary_list.PaymentRequestSummaryList"
    """<p>An array of <code>PaymentRequestSummary</code> objects containing summary information about each payment request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementPaymentRequestsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_marketplace_agreement.types.payment_request_summary_list

    out["items"] = (
        capo_marketplace_agreement.types.payment_request_summary_list.serialize_aws_json_1_0(
            value["items"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementPaymentRequestsOutput:
    out: ListAgreementPaymentRequestsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import capo_marketplace_agreement.types.payment_request_summary_list

        out["items"] = (
            capo_marketplace_agreement.types.payment_request_summary_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    else:
        raise DeserializationError("ListAgreementPaymentRequestsOutput.items required")
    return out
