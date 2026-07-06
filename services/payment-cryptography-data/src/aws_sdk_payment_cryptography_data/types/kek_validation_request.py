"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#KekValidationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.random_key_max_length
    import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm


class KekValidationRequest(TypedDict, closed=True):
    derive_key_algorithm: "aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.SymmetricKeyAlgorithm"
    """<p>The key derivation algorithm to use for generating a KEK validation request.</p>"""
    random_key_max_length: NotRequired[
        "aws_sdk_payment_cryptography_data.types.random_key_max_length.RandomKeyMaxLength"
    ]
    """<p>The maximum length of the random key to generate for a KEK validation request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KekValidationRequest) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm

    out["DeriveKeyAlgorithm"] = (
        aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.serialize_json(
            value["derive_key_algorithm"]
        )
    )
    if "random_key_max_length" in value:
        import aws_sdk_payment_cryptography_data.types.random_key_max_length

        out["RandomKeyMaxLength"] = (
            aws_sdk_payment_cryptography_data.types.random_key_max_length.serialize_json(
                value["random_key_max_length"]
            )
        )
    return out


def deserialize_json(data: dict) -> KekValidationRequest:
    out: KekValidationRequest = {}  # type: ignore[typeddict-item]
    if "DeriveKeyAlgorithm" in data:
        import aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm

        out["derive_key_algorithm"] = (
            aws_sdk_payment_cryptography_data.types.symmetric_key_algorithm.deserialize_json(
                data["DeriveKeyAlgorithm"]
            )
        )
    else:
        raise DeserializationError("KekValidationRequest.derive_key_algorithm required")
    if "RandomKeyMaxLength" in data:
        import aws_sdk_payment_cryptography_data.types.random_key_max_length

        out["random_key_max_length"] = (
            aws_sdk_payment_cryptography_data.types.random_key_max_length.deserialize_json(
                data["RandomKeyMaxLength"]
            )
        )
    return out
