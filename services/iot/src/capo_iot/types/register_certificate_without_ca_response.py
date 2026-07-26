"""Generated from Smithy shape ``com.amazonaws.iot#RegisterCertificateWithoutCAResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.certificate_arn
    import capo_iot.types.certificate_id


class RegisterCertificateWithoutCAResponse(TypedDict, closed=True):
    certificate_arn: NotRequired["capo_iot.types.certificate_arn.CertificateArn"]
    """<p>The Amazon Resource Name (ARN) of the registered certificate.</p>"""
    certificate_id: NotRequired["capo_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the registered certificate. (The last part of the certificate ARN contains the certificate ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCertificateWithoutCAResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    return out


def deserialize_json(data: dict) -> RegisterCertificateWithoutCAResponse:
    out: RegisterCertificateWithoutCAResponse = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    return out
