"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CreateAgreementRequestOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.agreement_request_id
    import aws_sdk_marketplace_agreement.types.charge_summary


class CreateAgreementRequestOutput(TypedDict, closed=True):
    agreement_request_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.agreement_request_id.AgreementRequestId"
    ]
    """<p>The unique identifier of the agreement request created. Use this identifier with <code>AcceptAgreementRequest</code> to accept the agreement.</p>"""
    charge_summary: NotRequired[
        "aws_sdk_marketplace_agreement.types.charge_summary.ChargeSummary"
    ]
    """<p>Provides details of the charges associated with the agreement request. This is only applicable when a request is created for <code>PurchaseAgreement</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAgreementRequestOutput) -> dict:
    out: dict = {}
    if "agreement_request_id" in value:
        out["agreementRequestId"] = value["agreement_request_id"]
    if "charge_summary" in value:
        import aws_sdk_marketplace_agreement.types.charge_summary

        out["chargeSummary"] = (
            aws_sdk_marketplace_agreement.types.charge_summary.serialize_aws_json_1_0(
                value["charge_summary"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAgreementRequestOutput:
    out: CreateAgreementRequestOutput = {}  # type: ignore[typeddict-item]
    if "agreementRequestId" in data:
        out["agreement_request_id"] = data["agreementRequestId"]
    if "chargeSummary" in data:
        import aws_sdk_marketplace_agreement.types.charge_summary

        out["charge_summary"] = (
            aws_sdk_marketplace_agreement.types.charge_summary.deserialize_aws_json_1_0(
                data["chargeSummary"]
            )
        )
    return out
