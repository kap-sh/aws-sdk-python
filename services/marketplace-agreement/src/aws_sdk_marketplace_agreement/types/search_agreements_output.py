"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#SearchAgreementsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_view_summary_list
    import aws_sdk_marketplace_agreement.types.next_token


class SearchAgreementsOutput(TypedDict, closed=True):
    agreement_view_summaries: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_view_summary_list.AgreementViewSummaryList"
    ]
    """<p>A summary of the agreement, including top-level attributes (for example, the agreement ID, proposer, and acceptor).</p>"""
    next_token: NotRequired["aws_sdk_marketplace_agreement.types.next_token.NextToken"]
    """<p>The token used for pagination. The field is <code>null</code> if there are no more results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SearchAgreementsOutput) -> dict:
    out: dict = {}
    if "agreement_view_summaries" in value:
        import aws_sdk_marketplace_agreement.types.agreement_view_summary_list

        out["agreementViewSummaries"] = (
            aws_sdk_marketplace_agreement.types.agreement_view_summary_list.serialize_aws_json_1_0(
                value["agreement_view_summaries"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SearchAgreementsOutput:
    out: SearchAgreementsOutput = {}  # type: ignore[typeddict-item]
    if "agreementViewSummaries" in data:
        import aws_sdk_marketplace_agreement.types.agreement_view_summary_list

        out["agreement_view_summaries"] = (
            aws_sdk_marketplace_agreement.types.agreement_view_summary_list.deserialize_aws_json_1_0(
                data["agreementViewSummaries"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
