"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#RootCertificatePublicKey``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.certificate_type
    import aws_sdk_payment_cryptography.types.key_attributes


class RootCertificatePublicKey(TypedDict, closed=True):
    key_attributes: "aws_sdk_payment_cryptography.types.key_attributes.KeyAttributes"
    """<p>The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the root public key is imported.</p>"""
    public_key_certificate: (
        "aws_sdk_payment_cryptography.types.certificate_type.CertificateType"
    )
    """<p>Parameter information for root public key certificate import.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RootCertificatePublicKey) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography.types.key_attributes

    out["KeyAttributes"] = (
        aws_sdk_payment_cryptography.types.key_attributes.serialize_aws_json_1_0(
            value["key_attributes"]
        )
    )
    out["PublicKeyCertificate"] = value["public_key_certificate"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RootCertificatePublicKey:
    out: RootCertificatePublicKey = {}  # type: ignore[typeddict-item]
    if "KeyAttributes" in data:
        import aws_sdk_payment_cryptography.types.key_attributes

        out["key_attributes"] = (
            aws_sdk_payment_cryptography.types.key_attributes.deserialize_aws_json_1_0(
                data["KeyAttributes"]
            )
        )
    else:
        raise DeserializationError("RootCertificatePublicKey.key_attributes required")
    if "PublicKeyCertificate" in data:
        out["public_key_certificate"] = data["PublicKeyCertificate"]
    else:
        raise DeserializationError(
            "RootCertificatePublicKey.public_key_certificate required"
        )
    return out
