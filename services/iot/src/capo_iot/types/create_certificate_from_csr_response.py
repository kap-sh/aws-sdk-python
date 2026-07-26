"""Generated from Smithy shape ``com.amazonaws.iot#CreateCertificateFromCsrResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_arn
    import capo_iot.types.certificate_id
    import capo_iot.types.certificate_pem


class CreateCertificateFromCsrResponse(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_iot.types.certificate_arn.CertificateArn"]
    """<p>The Amazon Resource Name (ARN) of the certificate. You can use the ARN as a principal for policy operations.</p>"""
    certificate_id: NotRequired["capo_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the certificate. Certificate management operations only take a certificateId.</p>"""
    certificate_pem: NotRequired["capo_iot.types.certificate_pem.CertificatePem"]
    """<p>The certificate data, in PEM format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCertificateFromCsrResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "certificate_pem" in value:
        out["certificatePem"] = value["certificate_pem"]
    return out


def deserialize_json(data: dict) -> CreateCertificateFromCsrResponse:
    out: CreateCertificateFromCsrResponse = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    if "certificatePem" in data:
        out["certificate_pem"] = data["certificatePem"]
    return out
