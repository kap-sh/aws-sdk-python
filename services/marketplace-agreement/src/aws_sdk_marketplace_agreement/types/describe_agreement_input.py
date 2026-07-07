"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#DescribeAgreementInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_marketplace_agreement.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_marketplace_agreement.types.resource_id


class DescribeAgreementInput(TypedDict, closed=True):
    agreement_id: "aws_sdk_marketplace_agreement.types.resource_id.ResourceId"
    """<p>The unique identifier of the agreement.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAgreementInput) -> dict:
    out: dict = {}
    out["agreementId"] = value["agreement_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAgreementInput:
    out: DescribeAgreementInput = {}  # type: ignore[typeddict-item]
    if "agreementId" in data:
        out["agreement_id"] = data["agreementId"]
    else:
        raise DeserializationError("DescribeAgreementInput.agreement_id required")
    return out
