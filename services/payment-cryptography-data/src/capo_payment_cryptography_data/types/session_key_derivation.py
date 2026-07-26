"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#SessionKeyDerivation``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.session_key_amex
    import capo_payment_cryptography_data.types.session_key_emv2000
    import capo_payment_cryptography_data.types.session_key_emv_common
    import capo_payment_cryptography_data.types.session_key_mastercard
    import capo_payment_cryptography_data.types.session_key_visa


class _SessionKeyDerivation_EmvCommon(TypedDict, closed=True):
    EmvCommon: "capo_payment_cryptography_data.types.session_key_emv_common.SessionKeyEmvCommon"


class _SessionKeyDerivation_Mastercard(TypedDict, closed=True):
    Mastercard: "capo_payment_cryptography_data.types.session_key_mastercard.SessionKeyMastercard"


class _SessionKeyDerivation_Emv2000(TypedDict, closed=True):
    Emv2000: (
        "capo_payment_cryptography_data.types.session_key_emv2000.SessionKeyEmv2000"
    )


class _SessionKeyDerivation_Amex(TypedDict, closed=True):
    Amex: "capo_payment_cryptography_data.types.session_key_amex.SessionKeyAmex"


class _SessionKeyDerivation_Visa(TypedDict, closed=True):
    Visa: "capo_payment_cryptography_data.types.session_key_visa.SessionKeyVisa"


SessionKeyDerivation: TypeAlias = (
    _SessionKeyDerivation_EmvCommon
    | _SessionKeyDerivation_Mastercard
    | _SessionKeyDerivation_Emv2000
    | _SessionKeyDerivation_Amex
    | _SessionKeyDerivation_Visa
)


# --- restJson1 ser/de ---
def serialize_json(value: SessionKeyDerivation) -> dict:
    if "EmvCommon" in value:
        import capo_payment_cryptography_data.types.session_key_emv_common

        return {
            "EmvCommon": capo_payment_cryptography_data.types.session_key_emv_common.serialize_json(
                value["EmvCommon"]
            )
        }
    elif "Mastercard" in value:
        import capo_payment_cryptography_data.types.session_key_mastercard

        return {
            "Mastercard": capo_payment_cryptography_data.types.session_key_mastercard.serialize_json(
                value["Mastercard"]
            )
        }
    elif "Emv2000" in value:
        import capo_payment_cryptography_data.types.session_key_emv2000

        return {
            "Emv2000": capo_payment_cryptography_data.types.session_key_emv2000.serialize_json(
                value["Emv2000"]
            )
        }
    elif "Amex" in value:
        import capo_payment_cryptography_data.types.session_key_amex

        return {
            "Amex": capo_payment_cryptography_data.types.session_key_amex.serialize_json(
                value["Amex"]
            )
        }
    elif "Visa" in value:
        import capo_payment_cryptography_data.types.session_key_visa

        return {
            "Visa": capo_payment_cryptography_data.types.session_key_visa.serialize_json(
                value["Visa"]
            )
        }
    else:
        raise SerializationError("SessionKeyDerivation: no variant present")


def deserialize_json(data: dict) -> SessionKeyDerivation:
    if "EmvCommon" in data:
        import capo_payment_cryptography_data.types.session_key_emv_common

        return {
            "EmvCommon": capo_payment_cryptography_data.types.session_key_emv_common.deserialize_json(
                data["EmvCommon"]
            )
        }
    elif "Mastercard" in data:
        import capo_payment_cryptography_data.types.session_key_mastercard

        return {
            "Mastercard": capo_payment_cryptography_data.types.session_key_mastercard.deserialize_json(
                data["Mastercard"]
            )
        }
    elif "Emv2000" in data:
        import capo_payment_cryptography_data.types.session_key_emv2000

        return {
            "Emv2000": capo_payment_cryptography_data.types.session_key_emv2000.deserialize_json(
                data["Emv2000"]
            )
        }
    elif "Amex" in data:
        import capo_payment_cryptography_data.types.session_key_amex

        return {
            "Amex": capo_payment_cryptography_data.types.session_key_amex.deserialize_json(
                data["Amex"]
            )
        }
    elif "Visa" in data:
        import capo_payment_cryptography_data.types.session_key_visa

        return {
            "Visa": capo_payment_cryptography_data.types.session_key_visa.deserialize_json(
                data["Visa"]
            )
        }
    else:
        raise DeserializationError("SessionKeyDerivation: no recognized variant key")
