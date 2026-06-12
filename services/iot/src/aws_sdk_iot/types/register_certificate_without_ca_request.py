"""Generated from Smithy shape ``com.amazonaws.iot#RegisterCertificateWithoutCARequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_pem
    import aws_sdk_iot.types.certificate_status


class RegisterCertificateWithoutCARequest(TypedDict):
    certificate_pem: "aws_sdk_iot.types.certificate_pem.CertificatePem"
    """<p>The certificate data, in PEM format.</p>"""
    status: NotRequired["aws_sdk_iot.types.certificate_status.CertificateStatus"]
    """<p>The status of the register certificate request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCertificateWithoutCARequest) -> dict:
    out: dict = {}
    out["certificatePem"] = value["certificate_pem"]
    if "status" in value:
        import aws_sdk_iot.types.certificate_status

        out["status"] = aws_sdk_iot.types.certificate_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> RegisterCertificateWithoutCARequest:
    out: RegisterCertificateWithoutCARequest = {}  # type: ignore[typeddict-item]
    if "certificatePem" in data:
        out["certificate_pem"] = data["certificatePem"]
    else:
        raise DeserializationError(
            "RegisterCertificateWithoutCARequest.certificate_pem required"
        )
    if "status" in data:
        import aws_sdk_iot.types.certificate_status

        out["status"] = aws_sdk_iot.types.certificate_status.deserialize_json(
            data["status"]
        )
    return out
