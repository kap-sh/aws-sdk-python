"""Generated from Smithy shape ``com.amazonaws.iot#RegisterCertificateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_arn
    import aws_sdk_iot.types.certificate_id


class RegisterCertificateResponse(TypedDict, closed=True):
    certificate_arn: NotRequired["aws_sdk_iot.types.certificate_arn.CertificateArn"]
    """<p>The certificate ARN.</p>"""
    certificate_id: NotRequired["aws_sdk_iot.types.certificate_id.CertificateId"]
    """<p>The certificate identifier.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    return out


def deserialize_json(data: dict) -> RegisterCertificateResponse:
    out: RegisterCertificateResponse = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    return out
