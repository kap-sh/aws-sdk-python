"""Generated from Smithy shape ``com.amazonaws.iot#CreateProvisioningClaimResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iot.types.certificate_id
    import aws_sdk_iot.types.certificate_pem
    import aws_sdk_iot.types.date_type
    import aws_sdk_iot.types.key_pair


class CreateProvisioningClaimResponse(TypedDict, closed=True):
    certificate_id: NotRequired["aws_sdk_iot.types.certificate_id.CertificateId"]
    """<p>The ID of the certificate.</p>"""
    certificate_pem: NotRequired["aws_sdk_iot.types.certificate_pem.CertificatePem"]
    """<p>The provisioning claim certificate.</p>"""
    key_pair: NotRequired["aws_sdk_iot.types.key_pair.KeyPair"]
    """<p>The provisioning claim key pair.</p>"""
    expiration: NotRequired["aws_sdk_iot.types.date_type.DateType"]
    """<p>The provisioning claim expiration time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateProvisioningClaimResponse) -> dict:
    out: dict = {}
    if "certificate_id" in value:
        out["certificateId"] = value["certificate_id"]
    if "certificate_pem" in value:
        out["certificatePem"] = value["certificate_pem"]
    if "key_pair" in value:
        import aws_sdk_iot.types.key_pair

        out["keyPair"] = aws_sdk_iot.types.key_pair.serialize_json(value["key_pair"])
    if "expiration" in value:
        import aws_sdk_iot.types.date_type

        out["expiration"] = aws_sdk_iot.types.date_type.serialize_json(
            value["expiration"]
        )
    return out


def deserialize_json(data: dict) -> CreateProvisioningClaimResponse:
    out: CreateProvisioningClaimResponse = {}  # type: ignore[typeddict-item]
    if "certificateId" in data:
        out["certificate_id"] = data["certificateId"]
    if "certificatePem" in data:
        out["certificate_pem"] = data["certificatePem"]
    if "keyPair" in data:
        import aws_sdk_iot.types.key_pair

        out["key_pair"] = aws_sdk_iot.types.key_pair.deserialize_json(data["keyPair"])
    if "expiration" in data:
        import aws_sdk_iot.types.date_type

        out["expiration"] = aws_sdk_iot.types.date_type.deserialize_json(
            data["expiration"]
        )
    return out
