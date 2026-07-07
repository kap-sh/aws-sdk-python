"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#KeyAttributes``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_algorithm
    import aws_sdk_payment_cryptography.types.key_class
    import aws_sdk_payment_cryptography.types.key_modes_of_use
    import aws_sdk_payment_cryptography.types.key_usage


class KeyAttributes(TypedDict, closed=True):
    key_usage: "aws_sdk_payment_cryptography.types.key_usage.KeyUsage"
    """<p>The cryptographic usage of an Amazon Web Services Payment Cryptography key as deﬁned in section A.5.2 of the TR-31 spec.</p>"""
    key_class: "aws_sdk_payment_cryptography.types.key_class.KeyClass"
    """<p>The type of Amazon Web Services Payment Cryptography key to create, which determines the classiﬁcation of the cryptographic method and whether Amazon Web Services Payment Cryptography key contains a symmetric key or an asymmetric key pair.</p>"""
    key_algorithm: "aws_sdk_payment_cryptography.types.key_algorithm.KeyAlgorithm"
    """<p>The key algorithm to be use during creation of an Amazon Web Services Payment Cryptography key.</p> <p>For symmetric keys, Amazon Web Services Payment Cryptography supports <code>AES</code> and <code>TDES</code> algorithms. For asymmetric keys, Amazon Web Services Payment Cryptography supports <code>RSA</code> and <code>ECC_NIST</code> algorithms.</p>"""
    key_modes_of_use: (
        "aws_sdk_payment_cryptography.types.key_modes_of_use.KeyModesOfUse"
    )
    """<p>The list of cryptographic operations that you can perform using the key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyAttributes) -> dict:
    out: dict = {}
    out["KeyUsage"] = value["key_usage"]
    out["KeyClass"] = value["key_class"]
    out["KeyAlgorithm"] = value["key_algorithm"]
    import aws_sdk_payment_cryptography.types.key_modes_of_use

    out["KeyModesOfUse"] = (
        aws_sdk_payment_cryptography.types.key_modes_of_use.serialize_aws_json_1_0(
            value["key_modes_of_use"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> KeyAttributes:
    out: KeyAttributes = {}  # type: ignore[typeddict-item]
    if "KeyUsage" in data:
        out["key_usage"] = data["KeyUsage"]
    else:
        raise DeserializationError("KeyAttributes.key_usage required")
    if "KeyClass" in data:
        out["key_class"] = data["KeyClass"]
    else:
        raise DeserializationError("KeyAttributes.key_class required")
    if "KeyAlgorithm" in data:
        out["key_algorithm"] = data["KeyAlgorithm"]
    else:
        raise DeserializationError("KeyAttributes.key_algorithm required")
    if "KeyModesOfUse" in data:
        import aws_sdk_payment_cryptography.types.key_modes_of_use

        out["key_modes_of_use"] = (
            aws_sdk_payment_cryptography.types.key_modes_of_use.deserialize_aws_json_1_0(
                data["KeyModesOfUse"]
            )
        )
    else:
        raise DeserializationError("KeyAttributes.key_modes_of_use required")
    return out
