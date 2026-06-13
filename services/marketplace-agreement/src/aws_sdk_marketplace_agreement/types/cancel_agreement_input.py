"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CancelAgreementInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.resource_id


class CancelAgreementInput(TypedDict):
    agreement_id: "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CancelAgreementInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CancelAgreementInput:
    out: CancelAgreementInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError("CancelAgreementInput.agreement_id required")
    return out
