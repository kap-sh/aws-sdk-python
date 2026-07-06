"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportKeyCryptogram``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.certificate_type
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography.types.wrapping_key_spec


class ExportKeyCryptogram(TypedDict, closed=True):
    certificate_authority_public_key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>KeyARN</code> of the certificate chain that signs the wrapping key certificate during RSA wrap and unwrap key export.</p>"""
    wrapping_key_certificate: (
        "aws_sdk_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>The wrapping key certificate in PEM format (base64 encoded). Amazon Web Services Payment Cryptography uses this certificate to wrap the key under export.</p>"""
    wrapping_spec: NotRequired[
        "aws_sdk_payment_cryptography.types.wrapping_key_spec.WrappingKeySpec"
    ]
    """<p>The wrapping spec for the key under export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportKeyCryptogram) -> dict:
    out: dict = {}
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["WrappingKeyCertificate"] = value["wrapping_key_certificate"]
    if "wrapping_spec" in value:
        out["WrappingSpec"] = value["wrapping_spec"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportKeyCryptogram:
    out: ExportKeyCryptogram = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityPublicKeyIdentifier" in data:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "ExportKeyCryptogram.certificate_authority_public_key_identifier required"
        )
    if "WrappingKeyCertificate" in data:
        out["wrapping_key_certificate"] = data["WrappingKeyCertificate"]
    else:
        raise DeserializationError(
            "ExportKeyCryptogram.wrapping_key_certificate required"
        )
    if "WrappingSpec" in data:
        out["wrapping_spec"] = data["WrappingSpec"]
    return out
