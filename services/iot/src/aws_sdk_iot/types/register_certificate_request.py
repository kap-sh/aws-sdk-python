"""Generated from Smithy shape ``com.amazonaws.iot#RegisterCertificateRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_pem
    import aws_sdk_iot.types.certificate_status
    import aws_sdk_iot.types.set_as_active_flag


class RegisterCertificateRequest(TypedDict):
    certificate_pem: "aws_sdk_iot.types.certificate_pem.CertificatePem"
    """<p>The certificate data, in PEM format.</p>"""
    ca_certificate_pem: NotRequired["aws_sdk_iot.types.certificate_pem.CertificatePem"]
    """<p>The CA certificate used to sign the device certificate being registered.</p>"""
    set_as_active: NotRequired["aws_sdk_iot.types.set_as_active_flag.SetAsActiveFlag"]
    """<p>A boolean value that specifies if the certificate is set to active.</p> <p>Valid values: <code>ACTIVE | INACTIVE</code> </p>"""
    status: NotRequired["aws_sdk_iot.types.certificate_status.CertificateStatus"]
    """<p>The status of the register certificate request. Valid values that you can use include <code>ACTIVE</code>, <code>INACTIVE</code>, and <code>REVOKED</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RegisterCertificateRequest) -> dict:
    out: dict = {}
    out["certificatePem"] = value["certificate_pem"]
    if "ca_certificate_pem" in value:
        out["caCertificatePem"] = value["ca_certificate_pem"]
    if "status" in value:
        import aws_sdk_iot.types.certificate_status

        out["status"] = aws_sdk_iot.types.certificate_status.serialize_json(
            value["status"]
        )
    return out


def deserialize_json(data: dict) -> RegisterCertificateRequest:
    out: RegisterCertificateRequest = {}  # type: ignore[typeddict-item]
    if "certificatePem" in data:
        out["certificate_pem"] = data["certificatePem"]
    else:
        raise DeserializationError(
            "RegisterCertificateRequest.certificate_pem required"
        )
    if "caCertificatePem" in data:
        out["ca_certificate_pem"] = data["caCertificatePem"]
    if "status" in data:
        import aws_sdk_iot.types.certificate_status

        out["status"] = aws_sdk_iot.types.certificate_status.deserialize_json(
            data["status"]
        )
    return out
