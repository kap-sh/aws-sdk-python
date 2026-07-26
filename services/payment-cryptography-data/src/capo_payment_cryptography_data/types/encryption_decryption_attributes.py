"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#EncryptionDecryptionAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.asymmetric_encryption_attributes
    import capo_payment_cryptography_data.types.dukpt_encryption_attributes
    import capo_payment_cryptography_data.types.emv_encryption_attributes
    import capo_payment_cryptography_data.types.symmetric_encryption_attributes


class _EncryptionDecryptionAttributes_Symmetric(TypedDict, closed=True):
    Symmetric: "capo_payment_cryptography_data.types.symmetric_encryption_attributes.SymmetricEncryptionAttributes"


class _EncryptionDecryptionAttributes_Asymmetric(TypedDict, closed=True):
    Asymmetric: "capo_payment_cryptography_data.types.asymmetric_encryption_attributes.AsymmetricEncryptionAttributes"


class _EncryptionDecryptionAttributes_Dukpt(TypedDict, closed=True):
    Dukpt: "capo_payment_cryptography_data.types.dukpt_encryption_attributes.DukptEncryptionAttributes"


class _EncryptionDecryptionAttributes_Emv(TypedDict, closed=True):
    Emv: "capo_payment_cryptography_data.types.emv_encryption_attributes.EmvEncryptionAttributes"


EncryptionDecryptionAttributes: TypeAlias = (
    _EncryptionDecryptionAttributes_Symmetric
    | _EncryptionDecryptionAttributes_Asymmetric
    | _EncryptionDecryptionAttributes_Dukpt
    | _EncryptionDecryptionAttributes_Emv
)


# --- restJson1 ser/de ---
def serialize_json(value: EncryptionDecryptionAttributes) -> dict:
    if "Symmetric" in value:
        import capo_payment_cryptography_data.types.symmetric_encryption_attributes

        return {
            "Symmetric": capo_payment_cryptography_data.types.symmetric_encryption_attributes.serialize_json(
                value["Symmetric"]
            )
        }
    elif "Asymmetric" in value:
        import capo_payment_cryptography_data.types.asymmetric_encryption_attributes

        return {
            "Asymmetric": capo_payment_cryptography_data.types.asymmetric_encryption_attributes.serialize_json(
                value["Asymmetric"]
            )
        }
    elif "Dukpt" in value:
        import capo_payment_cryptography_data.types.dukpt_encryption_attributes

        return {
            "Dukpt": capo_payment_cryptography_data.types.dukpt_encryption_attributes.serialize_json(
                value["Dukpt"]
            )
        }
    elif "Emv" in value:
        import capo_payment_cryptography_data.types.emv_encryption_attributes

        return {
            "Emv": capo_payment_cryptography_data.types.emv_encryption_attributes.serialize_json(
                value["Emv"]
            )
        }
    else:
        raise SerializationError("EncryptionDecryptionAttributes: no variant present")


def deserialize_json(data: dict) -> EncryptionDecryptionAttributes:
    if "Symmetric" in data:
        import capo_payment_cryptography_data.types.symmetric_encryption_attributes

        return {
            "Symmetric": capo_payment_cryptography_data.types.symmetric_encryption_attributes.deserialize_json(
                data["Symmetric"]
            )
        }
    elif "Asymmetric" in data:
        import capo_payment_cryptography_data.types.asymmetric_encryption_attributes

        return {
            "Asymmetric": capo_payment_cryptography_data.types.asymmetric_encryption_attributes.deserialize_json(
                data["Asymmetric"]
            )
        }
    elif "Dukpt" in data:
        import capo_payment_cryptography_data.types.dukpt_encryption_attributes

        return {
            "Dukpt": capo_payment_cryptography_data.types.dukpt_encryption_attributes.deserialize_json(
                data["Dukpt"]
            )
        }
    elif "Emv" in data:
        import capo_payment_cryptography_data.types.emv_encryption_attributes

        return {
            "Emv": capo_payment_cryptography_data.types.emv_encryption_attributes.deserialize_json(
                data["Emv"]
            )
        }
    else:
        raise DeserializationError(
            "EncryptionDecryptionAttributes: no recognized variant key"
        )
