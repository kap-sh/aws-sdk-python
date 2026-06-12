"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EcdhDerivationAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.certificate_type
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.key_derivation_function
    import aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm
    import aws_sdk_payment_cryptography_data.types.shared_information
    import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm


class EcdhDerivationAttributes(TypedDict):
    certificate_authority_public_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyArn</code> of the certificate that signed the client's <code>PublicKeyCertificate</code>.</p>"""
    public_key_certificate: (
        "aws_sdk_payment_cryptography_data.types.certificate_type.CertificateType"
    )
    """<p>The client's public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.</p>"""
    key_algorithm: "aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.SymmetricKeyAlgorithm"
    """<p>The key algorithm of the derived ECDH key.</p>"""
    key_derivation_function: "aws_sdk_payment_cryptography_data.types.key_derivation_function.KeyDerivationFunction"
    """<p>The key derivation function to use for deriving a key using ECDH.</p>"""
    key_derivation_hash_algorithm: "aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm.KeyDerivationHashAlgorithm"
    """<p>The hash type to use for deriving a key using ECDH.</p>"""
    shared_information: (
        "aws_sdk_payment_cryptography_data.types.shared_information.SharedInformation"
    )
    """<p>A byte string containing information that binds the ECDH derived key to the two parties involved or to the context of the key.</p> <p>It may include details like identities of the two parties deriving the key, context of the operation, session IDs, and optionally a nonce. It must not contain zero bytes, and re-using shared information for multiple ECDH key derivations is not recommended.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EcdhDerivationAttributes) -> dict:
    out: dict = {}
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["PublicKeyCertificate"] = value["public_key_certificate"]
    import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm

    out["KeyAlgorithm"] = (
        aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.serialize_json(
            value["key_algorithm"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.key_derivation_function

    out["KeyDerivationFunction"] = (
        aws_sdk_payment_cryptography_data.types.key_derivation_function.serialize_json(
            value["key_derivation_function"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm

    out["KeyDerivationHashAlgorithm"] = (
        aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm.serialize_json(
            value["key_derivation_hash_algorithm"]
        )
    )
    out["SharedInformation"] = value["shared_information"]
    return out


def deserialize_json(data: dict) -> EcdhDerivationAttributes:
    out: EcdhDerivationAttributes = {}  # type: ignore[typeddict-item]
    if "CertificateAuthorityPublicKeyIdentifier" in data:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "EcdhDerivationAttributes.certificate_authority_public_key_identifier required"
        )
    if "PublicKeyCertificate" in data:
        out["public_key_certificate"] = data["PublicKeyCertificate"]
    else:
        raise DeserializationError(
            "EcdhDerivationAttributes.public_key_certificate required"
        )
    if "KeyAlgorithm" in data:
        import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm

        out["key_algorithm"] = (
            aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.deserialize_json(
                data["KeyAlgorithm"]
            )
        )
    else:
        raise DeserializationError("EcdhDerivationAttributes.key_algorithm required")
    if "KeyDerivationFunction" in data:
        import aws_sdk_payment_cryptography_data.types.key_derivation_function

        out["key_derivation_function"] = (
            aws_sdk_payment_cryptography_data.types.key_derivation_function.deserialize_json(
                data["KeyDerivationFunction"]
            )
        )
    else:
        raise DeserializationError(
            "EcdhDerivationAttributes.key_derivation_function required"
        )
    if "KeyDerivationHashAlgorithm" in data:
        import aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm

        out["key_derivation_hash_algorithm"] = (
            aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm.deserialize_json(
                data["KeyDerivationHashAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "EcdhDerivationAttributes.key_derivation_hash_algorithm required"
        )
    if "SharedInformation" in data:
        out["shared_information"] = data["SharedInformation"]
    else:
        raise DeserializationError(
            "EcdhDerivationAttributes.shared_information required"
        )
    return out
