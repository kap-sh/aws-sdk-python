"""Generated from Smithy shape ``com.amazonaws.directconnect#ConfirmCustomerAgreementResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.status


class ConfirmCustomerAgreementResponse(TypedDict, closed=True):
    status: NotRequired["aws_sdk_direct_connect.types.status.Status"]
    """<p> The status of the customer agreement when the connection was created. This will be either <code>signed</code> or <code>unsigned</code>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConfirmCustomerAgreementResponse) -> dict:
    out: dict = {}
    if "status" in value:
        out["status"] = value["status"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ConfirmCustomerAgreementResponse:
    out: ConfirmCustomerAgreementResponse = {}  # type: ignore[typeddict-item]
    if "status" in data:
        out["status"] = data["status"]
    return out
