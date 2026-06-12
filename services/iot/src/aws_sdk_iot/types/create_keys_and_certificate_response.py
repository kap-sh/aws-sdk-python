"""Generated from Smithy shape ``com.amazonaws.iot#CreateKeysAndCertificateResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_arn
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.certificate_pem
    import aws_sdk_iot.types.key_pair


class CreateKeysAndCertificateResponse(TypedDict):
    certificate_arn: NotRequired["aws_sdk_iot.types.certificate_arn.CertificateArn"]
    """<p>The ARN of the certificate.</p>"""
    certificate_id: NotRequired["aws_sdk_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the certificate. IoT issues a default subject name for the certificate (for example, IoT Certificate).</p>"""
    certificate_pem: NotRequired["aws_sdk_iot.types.certificate_pem.CertificatePem"]
    """<p>The certificate data, in PEM format.</p>"""
    key_pair: NotRequired["aws_sdk_iot.types.key_pair.KeyPair"]
    """<p>The generated key pair.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateKeysAndCertificateResponse) -> dict:
    out: dict = {}
    if "certificate_arn" in value:
        out["certificateArn"] = value["certificate_arn"]
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "certificate_pem" in value:
        out["certificatePem"] = value["certificate_pem"]
    if "key_pair" in value:
        import aws_sdk_iot.types.key_pair

        out["keyPair"] = aws_sdk_iot.types.key_pair.serialize_json(value["key_pair"])
    return out


def deserialize_json(data: dict) -> CreateKeysAndCertificateResponse:
    out: CreateKeysAndCertificateResponse = {}  # type: ignore[typeddict-item]
    if "certificateArn" in data:
        out["certificate_arn"] = data["certificateArn"]
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    if "certificatePem" in data:
        out["certificate_pem"] = data["certificatePem"]
    if "keyPair" in data:
        import aws_sdk_iot.types.key_pair

        out["key_pair"] = aws_sdk_iot.types.key_pair.deserialize_json(data["keyPair"])
    return out
