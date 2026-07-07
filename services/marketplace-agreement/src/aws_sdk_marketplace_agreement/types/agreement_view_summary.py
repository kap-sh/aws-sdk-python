"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementViewSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.acceptor
    import aws_sdk_marketplace_agreement.types.agreement_status
    import aws_sdk_marketplace_agreement.types.agreement_type
    import aws_sdk_marketplace_agreement.types.entitlement_list
    import aws_sdk_marketplace_agreement.types.proposal_summary
    import aws_sdk_marketplace_agreement.types.proposer
    import aws_sdk_marketplace_agreement.types.resource_id
    import aws_sdk_marketplace_agreement.types.timestamp


class AgreementViewSummary(TypedDict, closed=True):
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the agreement.</p>"""
    acceptance_time: NotRequired[
        "aws_sdk_marketplace_agreement.types.timestamp.Timestamp"
    ]
    """<p>The date and time that the agreement was accepted.</p>"""
    start_time: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement starts.</p>"""
    end_time: NotRequired["aws_sdk_marketplace_agreement.types.timestamp.Timestamp"]
    """<p>The date and time when the agreement ends. The field is <code>null</code> for pay-as-you-go agreements, which don’t have end dates.</p>"""
    agreement_type: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_type.AgreementType"
    ]
    """<p>The type of agreement.</p>"""
    acceptor: NotRequired["aws_sdk_marketplace_agreement.types.acceptor.Acceptor"]
    """<p>Details of the party accepting the agreement terms. This is commonly the buyer for <code>PurchaseAgreement.</code> </p>"""
    proposer: NotRequired["aws_sdk_marketplace_agreement.types.proposer.Proposer"]
    """<p>Details of the party proposing the agreement terms, most commonly the seller for <code>PurchaseAgreement</code>.</p>"""
    proposal_summary: NotRequired[
        "aws_sdk_marketplace_agreement.types.proposal_summary.ProposalSummary"
    ]
    """<p>A summary of the proposal</p>"""
    status: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_status.AgreementStatus"
    ]
    """<p>The current status of the agreement. </p>"""
    entitlements: NotRequired[
        "aws_sdk_marketplace_agreement.types.entitlement_list.EntitlementList"
    ]
    """<p>A list of entitlements associated with the agreement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementViewSummary) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    if "acceptance_time" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["acceptanceTime"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["acceptance_time"]
            )
        )
    if "start_time" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["startTime"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["start_time"]
            )
        )
    if "end_time" in value:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["endTime"] = (
            aws_sdk_marketplace_agreement.types.timestamp.serialize_aws_json_1_0(
                value["end_time"]
            )
        )
    if "agreement_type" in value:
        out["agreementType"] = value["agreement_type"]
    if "acceptor" in value:
        import aws_sdk_marketplace_agreement.types.acceptor

        out["acceptor"] = (
            aws_sdk_marketplace_agreement.types.acceptor.serialize_aws_json_1_0(
                value["acceptor"]
            )
        )
    if "proposer" in value:
        import aws_sdk_marketplace_agreement.types.proposer

        out["proposer"] = (
            aws_sdk_marketplace_agreement.types.proposer.serialize_aws_json_1_0(
                value["proposer"]
            )
        )
    if "proposal_summary" in value:
        import aws_sdk_marketplace_agreement.types.proposal_summary

        out["proposalSummary"] = (
            aws_sdk_marketplace_agreement.types.proposal_summary.serialize_aws_json_1_0(
                value["proposal_summary"]
            )
        )
    if "status" in value:
        import aws_sdk_marketplace_agreement.types.agreement_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.agreement_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "entitlements" in value:
        import aws_sdk_marketplace_agreement.types.entitlement_list

        out["entitlements"] = (
            aws_sdk_marketplace_agreement.types.entitlement_list.serialize_aws_json_1_0(
                value["entitlements"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementViewSummary:
    out: AgreementViewSummary = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    if "acceptanceTime" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["acceptance_time"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["acceptanceTime"]
            )
        )
    if "startTime" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["start_time"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["startTime"]
            )
        )
    if "endTime" in data:
        import aws_sdk_marketplace_agreement.types.timestamp

        out["end_time"] = (
            aws_sdk_marketplace_agreement.types.timestamp.deserialize_aws_json_1_0(
                data["endTime"]
            )
        )
    if "agreementType" in data:
        out["agreement_type"] = data["agreementType"]
    if "acceptor" in data:
        import aws_sdk_marketplace_agreement.types.acceptor

        out["acceptor"] = (
            aws_sdk_marketplace_agreement.types.acceptor.deserialize_aws_json_1_0(
                data["acceptor"]
            )
        )
    if "proposer" in data:
        import aws_sdk_marketplace_agreement.types.proposer

        out["proposer"] = (
            aws_sdk_marketplace_agreement.types.proposer.deserialize_aws_json_1_0(
                data["proposer"]
            )
        )
    if "proposalSummary" in data:
        import aws_sdk_marketplace_agreement.types.proposal_summary

        out["proposal_summary"] = (
            aws_sdk_marketplace_agreement.types.proposal_summary.deserialize_aws_json_1_0(
                data["proposalSummary"]
            )
        )
    if "status" in data:
        import aws_sdk_marketplace_agreement.types.agreement_status

        out["status"] = (
            aws_sdk_marketplace_agreement.types.agreement_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "entitlements" in data:
        import aws_sdk_marketplace_agreement.types.entitlement_list

        out["entitlements"] = (
            aws_sdk_marketplace_agreement.types.entitlement_list.deserialize_aws_json_1_0(
                data["entitlements"]
            )
        )
    return out
