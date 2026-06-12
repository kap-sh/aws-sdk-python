"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#ReEncryptionAttributes``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.dukpt_encryption_attributes
    import aws_sdk_payment_cryptography_data.types.symmetric_encryption_attributes


class _ReEncryptionAttributes_Symmetric(TypedDict):
    Symmetric: "aws_sdk_payment_cryptography_data.types.symmetric_encryption_attributes.SymmetricEncryptionAttributes"


class _ReEncryptionAttributes_Dukpt(TypedDict):
    Dukpt: "aws_sdk_payment_cryptography_data.types.dukpt_encryption_attributes.DukptEncryptionAttributes"


ReEncryptionAttributes: TypeAlias = (
    _ReEncryptionAttributes_Symmetric | _ReEncryptionAttributes_Dukpt
)


# --- restJson1 ser/de ---
def serialize_json(value: ReEncryptionAttributes) -> dict:
    if "Symmetric" in value:
        import aws_sdk_payment_cryptography_data.types.symmetric_encryption_attributes

        return {
            "Symmetric": aws_sdk_payment_cryptography_data.types.symmetric_encryption_attributes.serialize_json(
                value["Symmetric"]
            )
        }
    elif "Dukpt" in value:
        import aws_sdk_payment_cryptography_data.types.dukpt_encryption_attributes

        return {
            "Dukpt": aws_sdk_payment_cryptography_data.types.dukpt_encryption_attributes.serialize_json(
                value["Dukpt"]
            )
        }
    else:
        raise SerializationError("ReEncryptionAttributes: no variant present")


def deserialize_json(data: dict) -> ReEncryptionAttributes:
    if "Symmetric" in data:
        import aws_sdk_payment_cryptography_data.types.symmetric_encryption_attributes

        return {
            "Symmetric": aws_sdk_payment_cryptography_data.types.symmetric_encryption_attributes.deserialize_json(
                data["Symmetric"]
            )
        }
    elif "Dukpt" in data:
        import aws_sdk_payment_cryptography_data.types.dukpt_encryption_attributes

        return {
            "Dukpt": aws_sdk_payment_cryptography_data.types.dukpt_encryption_attributes.deserialize_json(
                data["Dukpt"]
            )
        }
    else:
        raise DeserializationError("ReEncryptionAttributes: no recognized variant key")
