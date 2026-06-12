"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#IncomingDiffieHellmanTr31KeyBlock``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.certificate_type
    import aws_sdk_payment_cryptography_data.types.diffie_hellman_derivation_data
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.key_derivation_function
    import aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm
    import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm
    import aws_sdk_payment_cryptography_data.types.tr31_wrapped_key_block


class IncomingDiffieHellmanTr31KeyBlock(TypedDict):
    private_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the asymmetric ECC key pair.</p>"""
    certificate_authority_public_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyArn</code> of the certificate that signed the client's <code>PublicKeyCertificate</code>.</p>"""
    public_key_certificate: (
        "aws_sdk_payment_cryptography_data.types.certificate_type.CertificateType"
    )
    """<p>The client's public key certificate in PEM format (base64 encoded) to use for ECDH key derivation.</p>"""
    derive_key_algorithm: "aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.SymmetricKeyAlgorithm"
    """<p>The key algorithm of the derived ECDH key.</p>"""
    key_derivation_function: "aws_sdk_payment_cryptography_data.types.key_derivation_function.KeyDerivationFunction"
    """<p>The key derivation function to use for deriving a key using ECDH.</p>"""
    key_derivation_hash_algorithm: "aws_sdk_payment_cryptography_data.types.key_derivation_hash_algorithm.KeyDerivationHashAlgorithm"
    """<p>The hash type to use for deriving a key using ECDH.</p>"""
    derivation_data: "aws_sdk_payment_cryptography_data.types.diffie_hellman_derivation_data.DiffieHellmanDerivationData"
    wrapped_key_block: "aws_sdk_payment_cryptography_data.types.tr31_wrapped_key_block.Tr31WrappedKeyBlock"
    """<p>The WrappedKeyBlock containing the transaction key wrapped using an ECDH dervied key. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncomingDiffieHellmanTr31KeyBlock) -> dict:
    out: dict = {}
    out["PrivateKeyIdentifier"] = value["private_key_identifier"]
    out["CertificateAuthorityPublicKeyIdentifier"] = value[
        "certificate_authority_public_key_identifier"
    ]
    out["PublicKeyCertificate"] = value["public_key_certificate"]
    import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm

    out["DeriveKeyAlgorithm"] = (
        aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.serialize_json(
            value["derive_key_algorithm"]
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
    import aws_sdk_payment_cryptography_data.types.diffie_hellman_derivation_data

    out["DerivationData"] = (
        aws_sdk_payment_cryptography_data.types.diffie_hellman_derivation_data.serialize_json(
            value["derivation_data"]
        )
    )
    out["WrappedKeyBlock"] = value["wrapped_key_block"]
    return out


def deserialize_json(data: dict) -> IncomingDiffieHellmanTr31KeyBlock:
    out: IncomingDiffieHellmanTr31KeyBlock = {}  # type: ignore[typeddict-item]
    if "PrivateKeyIdentifier" in data:
        out["private_key_identifier"] = data["PrivateKeyIdentifier"]
    else:
        raise DeserializationError(
            "IncomingDiffieHellmanTr31KeyBlock.private_key_identifier required"
        )
    if "CertificateAuthorityPublicKeyIdentifier" in data:
        out["certificate_authority_public_key_identifier"] = data[
            "CertificateAuthorityPublicKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "IncomingDiffieHellmanTr31KeyBlock.certificate_authority_public_key_identifier required"
        )
    if "PublicKeyCertificate" in data:
        out["public_key_certificate"] = data["PublicKeyCertificate"]
    else:
        raise DeserializationError(
            "IncomingDiffieHellmanTr31KeyBlock.public_key_certificate required"
        )
    if "DeriveKeyAlgorithm" in data:
        import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm

        out["derive_key_algorithm"] = (
            aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.deserialize_json(
                data["DeriveKeyAlgorithm"]
            )
        )
    else:
        raise DeserializationError(
            "IncomingDiffieHellmanTr31KeyBlock.derive_key_algorithm required"
        )
    if "KeyDerivationFunction" in data:
        import aws_sdk_payment_cryptography_data.types.key_derivation_function

        out["key_derivation_function"] = (
            aws_sdk_payment_cryptography_data.types.key_derivation_function.deserialize_json(
                data["KeyDerivationFunction"]
            )
        )
    else:
        raise DeserializationError(
            "IncomingDiffieHellmanTr31KeyBlock.key_derivation_function required"
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
            "IncomingDiffieHellmanTr31KeyBlock.key_derivation_hash_algorithm required"
        )
    if "DerivationData" in data:
        import aws_sdk_payment_cryptography_data.types.diffie_hellman_derivation_data

        out["derivation_data"] = (
            aws_sdk_payment_cryptography_data.types.diffie_hellman_derivation_data.deserialize_json(
                data["DerivationData"]
            )
        )
    else:
        raise DeserializationError(
            "IncomingDiffieHellmanTr31KeyBlock.derivation_data required"
        )
    if "WrappedKeyBlock" in data:
        out["wrapped_key_block"] = data["WrappedKeyBlock"]
    else:
        raise DeserializationError(
            "IncomingDiffieHellmanTr31KeyBlock.wrapped_key_block required"
        )
    return out
