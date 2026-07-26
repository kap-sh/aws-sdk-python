"""Generated from Smithy shape ``com.amazonaws.iot#UpdateCertificateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_id
    import capo_iot.types.certificate_status


class UpdateCertificateRequest(TypedDict, closed=True):
    certificate_id: "capo_iot.types.certificate_id.CertificateId"
    """<p>The ID of the certificate. (The last part of the certificate ARN contains the certificate ID.)</p>"""
    new_status: "capo_iot.types.certificate_status.CertificateStatus"
    """<p>The new status.</p> <p> <b>Note:</b> Setting the status to PENDING_TRANSFER or PENDING_ACTIVATION will result in an exception being thrown. PENDING_TRANSFER and PENDING_ACTIVATION are statuses used internally by IoT. They are not intended for developer use.</p> <p> <b>Note:</b> The status value REGISTER_INACTIVE is deprecated and should not be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCertificateRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> UpdateCertificateRequest:
    out: UpdateCertificateRequest = {}  # type: ignore[typeddict-item]
    return out
