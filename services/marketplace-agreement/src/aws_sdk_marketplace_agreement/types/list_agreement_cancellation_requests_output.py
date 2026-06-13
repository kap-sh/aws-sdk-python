"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#ListAgreementCancellationRequestsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_summary_list
    import aws_sdk_marketplace_agreement.types.next_token


class ListAgreementCancellationRequestsOutput(TypedDict):
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""
    items: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_cancellation_request_summary_list.AgreementCancellationRequestSummaryList"
    ]
    """<p>An array of <code>AgreementCancellationRequestSummary</code> objects containing summary information about each cancellation request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListAgreementCancellationRequestsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "items" in value:
        import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_summary_list

        out["items"] = (
            aws_sdk_marketplace_agreement.types.agreement_cancellation_request_summary_list.serialize_aws_json_1_0(
                value["items"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListAgreementCancellationRequestsOutput:
    out: ListAgreementCancellationRequestsOutput = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "items" in data:
        import aws_sdk_marketplace_agreement.types.agreement_cancellation_request_summary_list

        out["items"] = (
            aws_sdk_marketplace_agreement.types.agreement_cancellation_request_summary_list.deserialize_aws_json_1_0(
                data["items"]
            )
        )
    return out
