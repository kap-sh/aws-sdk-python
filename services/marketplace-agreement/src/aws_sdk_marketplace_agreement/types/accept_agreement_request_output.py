"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AcceptAgreementRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.resource_id


class AcceptAgreementRequestOutput(TypedDict):
    agreement_id: NotRequired[
        "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The unique identifier of the agreement created or modified by accepting the agreement request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AcceptAgreementRequestOutput) -> dict:
    out: dict = {}
    if "agreement_id" in value:
        out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AcceptAgreementRequestOutput:
    out: AcceptAgreementRequestOutput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    return out
