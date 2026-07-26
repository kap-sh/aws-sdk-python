"""Generated from Smithy shape ``com.amazonaws.iot#TransferCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.aws_account_id
    import capo_iot.types.certificate_id
    import capo_iot.types.message


class TransferCertificateRequest(TypedDict, closed=True):
    certificate_id: "capo_iot.types.certificate_id.CertificateId"
    """<p>The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)</p>"""
    target_aws_account: "capo_iot.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account.</p>"""
    transfer_message: NotRequired["capo_iot.types.message.Message"]
    """<p>The transfer message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TransferCertificateRequest) -> dict:
    out: dict = {}
    if "transfer_message" in value:
        out["transferMessage"] = value["transfer_message"]
    return out


def deserialize_json(data: dict) -> TransferCertificateRequest:
    out: TransferCertificateRequest = {}  # type: ignore[typeddict-item]
    if "transferMessage" in data:
        out["transfer_message"] = data["transferMessage"]
    return out
