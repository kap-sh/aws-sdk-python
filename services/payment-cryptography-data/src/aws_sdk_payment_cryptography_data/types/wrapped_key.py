"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#WrappedKey``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.key_check_value_algorithm
    import aws_sdk_payment_cryptography_data.types.wrapped_key_material


class WrappedKey(TypedDict, closed=True):
    wrapped_key_material: "aws_sdk_payment_cryptography_data.types.wrapped_key_material.WrappedKeyMaterial"
    """<p>Parameter information of a WrappedKeyBlock for encryption key exchange.</p>"""
    key_check_value_algorithm: NotRequired[
        "aws_sdk_payment_cryptography_data.types.key_check_value_algorithm.KeyCheckValueAlgorithm"
    ]
    """<p>The algorithm that Amazon Web Services Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity.</p> <p>For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WrappedKey) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.wrapped_key_material

    out["WrappedKeyMaterial"] = (
        aws_sdk_payment_cryptography_data.types.wrapped_key_material.serialize_json(
            value["wrapped_key_material"]
        )
    )
    if "key_check_value_algorithm" in value:
        out["KeyCheckValueAlgorithm"] = value["key_check_value_algorithm"]
    return out


def deserialize_json(data: dict) -> WrappedKey:
    out: WrappedKey = {}  # type: ignore[typeddict-item]
    if "WrappedKeyMaterial" in data:
        import aws_sdk_payment_cryptography_data.types.wrapped_key_material

        out["wrapped_key_material"] = (
            aws_sdk_payment_cryptography_data.types.wrapped_key_material.deserialize_json(
                data["WrappedKeyMaterial"]
            )
        )
    else:
        raise DeserializationError("WrappedKey.wrapped_key_material required")
    if "KeyCheckValueAlgorithm" in data:
        out["key_check_value_algorithm"] = data["KeyCheckValueAlgorithm"]
    return out
