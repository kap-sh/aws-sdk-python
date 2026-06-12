"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SymmetricEncryptionAttributes``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.encryption_mode
    import aws_sdk_payment_cryptography_data.types.initialization_vector_type
    import aws_sdk_payment_cryptography_data.types.padding_type


class SymmetricEncryptionAttributes(TypedDict):
    mode: "aws_sdk_payment_cryptography_data.types.encryption_mode.EncryptionMode"
    """<p>The block cipher method to use for encryption.</p>"""
    initialization_vector: NotRequired[
        "aws_sdk_payment_cryptography_data.types.initialization_vector_type.InitializationVectorType"
    ]
    """<p>An input used to provide the intial state. If no value is provided, Amazon Web Services Payment Cryptography defaults it to zero.</p>"""
    padding_type: NotRequired[
        "aws_sdk_payment_cryptography_data.types.padding_type.PaddingType"
    ]
    """<p>The padding to be included with the data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SymmetricEncryptionAttributes) -> dict:
    out: dict = {}
    import aws_sdk_payment_cryptography_data.types.encryption_mode

    out["Mode"] = (
        aws_sdk_payment_cryptography_data.types.encryption_mode.serialize_json(
            value["mode"]
        )
    )
    if "initialization_vector" in value:
        out["InitializationVector"] = value["initialization_vector"]
    if "padding_type" in value:
        import aws_sdk_payment_cryptography_data.types.padding_type

        out["PaddingType"] = (
            aws_sdk_payment_cryptography_data.types.padding_type.serialize_json(
                value["padding_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> SymmetricEncryptionAttributes:
    out: SymmetricEncryptionAttributes = {}  # type: ignore[typeddict-item]
    if "Mode" in data:
        import aws_sdk_payment_cryptography_data.types.encryption_mode

        out["mode"] = (
            aws_sdk_payment_cryptography_data.types.encryption_mode.deserialize_json(
                data["Mode"]
            )
        )
    else:
        raise DeserializationError("SymmetricEncryptionAttributes.mode required")
    if "InitializationVector" in data:
        out["initialization_vector"] = data["InitializationVector"]
    if "PaddingType" in data:
        import aws_sdk_payment_cryptography_data.types.padding_type

        out["padding_type"] = (
            aws_sdk_payment_cryptography_data.types.padding_type.deserialize_json(
                data["PaddingType"]
            )
        )
    return out
