"""Generated from Smithy shape ``com.amazonaws.directconnect#CustomerAgreement``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.agreement_name
    import aws_sdk_direct_connect.types.status


class CustomerAgreement(TypedDict):
    agreement_name: NotRequired[
        "aws_sdk_direct_connect.types.agreement_name.AgreementName"
    ]
    """<p>The name of the agreement.</p>"""
    status: NotRequired["aws_sdk_direct_connect.types.status.Status"]
    """<p>The status of the customer agreement. This will be either <code>signed</code> or <code>unsigned</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerAgreement) -> dict:
    out: dict = {}
    if "agreement_name" in value:
        out["agreementName"] = value["agreement_name"]
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerAgreement:
    out: CustomerAgreement = {}  # type: ignore[typeddict-item]
    if "agreementName" in data:
        out["agreement_name"] = data["agreementName"]
    if "status" in data:
        out["status"] = data["status"]
    return out
