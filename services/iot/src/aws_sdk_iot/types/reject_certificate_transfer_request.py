"""Generated from Smithy shape ``com.amazonaws.iot#RejectCertificateTransferRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.message


class RejectCertificateTransferRequest(TypedDict, closed=True):
    certificate_id: "aws_sdk_iot.types.certificate_id.CertificateId"
    """<p>The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)</p>"""
    reject_reason: NotRequired["aws_sdk_iot.types.message.Message"]
    """<p>The reason the certificate transfer was rejected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RejectCertificateTransferRequest) -> dict:
    out: dict = {}
    if "reject_reason" in value:
        out["rejectReason"] = value["reject_reason"]
    return out


def deserialize_json(data: dict) -> RejectCertificateTransferRequest:
    out: RejectCertificateTransferRequest = {}  # type: ignore[typeddict-item]
    if "rejectReason" in data:
        out["reject_reason"] = data["rejectReason"]
    return out
