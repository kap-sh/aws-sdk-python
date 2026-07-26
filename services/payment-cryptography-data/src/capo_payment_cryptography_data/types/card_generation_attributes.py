"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CardGenerationAttributes``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.amex_card_security_code_version1
    import capo_payment_cryptography_data.types.amex_card_security_code_version2
    import capo_payment_cryptography_data.types.card_holder_verification_value
    import capo_payment_cryptography_data.types.card_verification_value1
    import capo_payment_cryptography_data.types.card_verification_value2
    import capo_payment_cryptography_data.types.dynamic_card_verification_code
    import capo_payment_cryptography_data.types.dynamic_card_verification_value


class _CardGenerationAttributes_AmexCardSecurityCodeVersion1(TypedDict, closed=True):
    AmexCardSecurityCodeVersion1: "capo_payment_cryptography_data.types.amex_card_security_code_version1.AmexCardSecurityCodeVersion1"


class _CardGenerationAttributes_AmexCardSecurityCodeVersion2(TypedDict, closed=True):
    AmexCardSecurityCodeVersion2: "capo_payment_cryptography_data.types.amex_card_security_code_version2.AmexCardSecurityCodeVersion2"


class _CardGenerationAttributes_CardVerificationValue1(TypedDict, closed=True):
    CardVerificationValue1: "capo_payment_cryptography_data.types.card_verification_value1.CardVerificationValue1"


class _CardGenerationAttributes_CardVerificationValue2(TypedDict, closed=True):
    CardVerificationValue2: "capo_payment_cryptography_data.types.card_verification_value2.CardVerificationValue2"


class _CardGenerationAttributes_CardHolderVerificationValue(TypedDict, closed=True):
    CardHolderVerificationValue: "capo_payment_cryptography_data.types.card_holder_verification_value.CardHolderVerificationValue"


class _CardGenerationAttributes_DynamicCardVerificationCode(TypedDict, closed=True):
    DynamicCardVerificationCode: "capo_payment_cryptography_data.types.dynamic_card_verification_code.DynamicCardVerificationCode"


class _CardGenerationAttributes_DynamicCardVerificationValue(TypedDict, closed=True):
    DynamicCardVerificationValue: "capo_payment_cryptography_data.types.dynamic_card_verification_value.DynamicCardVerificationValue"


CardGenerationAttributes: TypeAlias = (
    _CardGenerationAttributes_AmexCardSecurityCodeVersion1
    | _CardGenerationAttributes_AmexCardSecurityCodeVersion2
    | _CardGenerationAttributes_CardVerificationValue1
    | _CardGenerationAttributes_CardVerificationValue2
    | _CardGenerationAttributes_CardHolderVerificationValue
    | _CardGenerationAttributes_DynamicCardVerificationCode
    | _CardGenerationAttributes_DynamicCardVerificationValue
)


# --- restJson1 ser/de ---
def serialize_json(value: CardGenerationAttributes) -> dict:
    if "AmexCardSecurityCodeVersion1" in value:
        import capo_payment_cryptography_data.types.amex_card_security_code_version1

        return {
            "AmexCardSecurityCodeVersion1": capo_payment_cryptography_data.types.amex_card_security_code_version1.serialize_json(
                value["AmexCardSecurityCodeVersion1"]
            )
        }
    elif "AmexCardSecurityCodeVersion2" in value:
        import capo_payment_cryptography_data.types.amex_card_security_code_version2

        return {
            "AmexCardSecurityCodeVersion2": capo_payment_cryptography_data.types.amex_card_security_code_version2.serialize_json(
                value["AmexCardSecurityCodeVersion2"]
            )
        }
    elif "CardVerificationValue1" in value:
        import capo_payment_cryptography_data.types.card_verification_value1

        return {
            "CardVerificationValue1": capo_payment_cryptography_data.types.card_verification_value1.serialize_json(
                value["CardVerificationValue1"]
            )
        }
    elif "CardVerificationValue2" in value:
        import capo_payment_cryptography_data.types.card_verification_value2

        return {
            "CardVerificationValue2": capo_payment_cryptography_data.types.card_verification_value2.serialize_json(
                value["CardVerificationValue2"]
            )
        }
    elif "CardHolderVerificationValue" in value:
        import capo_payment_cryptography_data.types.card_holder_verification_value

        return {
            "CardHolderVerificationValue": capo_payment_cryptography_data.types.card_holder_verification_value.serialize_json(
                value["CardHolderVerificationValue"]
            )
        }
    elif "DynamicCardVerificationCode" in value:
        import capo_payment_cryptography_data.types.dynamic_card_verification_code

        return {
            "DynamicCardVerificationCode": capo_payment_cryptography_data.types.dynamic_card_verification_code.serialize_json(
                value["DynamicCardVerificationCode"]
            )
        }
    elif "DynamicCardVerificationValue" in value:
        import capo_payment_cryptography_data.types.dynamic_card_verification_value

        return {
            "DynamicCardVerificationValue": capo_payment_cryptography_data.types.dynamic_card_verification_value.serialize_json(
                value["DynamicCardVerificationValue"]
            )
        }
    else:
        raise SerializationError("CardGenerationAttributes: no variant present")


def deserialize_json(data: dict) -> CardGenerationAttributes:
    if "AmexCardSecurityCodeVersion1" in data:
        import capo_payment_cryptography_data.types.amex_card_security_code_version1

        return {
            "AmexCardSecurityCodeVersion1": capo_payment_cryptography_data.types.amex_card_security_code_version1.deserialize_json(
                data["AmexCardSecurityCodeVersion1"]
            )
        }
    elif "AmexCardSecurityCodeVersion2" in data:
        import capo_payment_cryptography_data.types.amex_card_security_code_version2

        return {
            "AmexCardSecurityCodeVersion2": capo_payment_cryptography_data.types.amex_card_security_code_version2.deserialize_json(
                data["AmexCardSecurityCodeVersion2"]
            )
        }
    elif "CardVerificationValue1" in data:
        import capo_payment_cryptography_data.types.card_verification_value1

        return {
            "CardVerificationValue1": capo_payment_cryptography_data.types.card_verification_value1.deserialize_json(
                data["CardVerificationValue1"]
            )
        }
    elif "CardVerificationValue2" in data:
        import capo_payment_cryptography_data.types.card_verification_value2

        return {
            "CardVerificationValue2": capo_payment_cryptography_data.types.card_verification_value2.deserialize_json(
                data["CardVerificationValue2"]
            )
        }
    elif "CardHolderVerificationValue" in data:
        import capo_payment_cryptography_data.types.card_holder_verification_value

        return {
            "CardHolderVerificationValue": capo_payment_cryptography_data.types.card_holder_verification_value.deserialize_json(
                data["CardHolderVerificationValue"]
            )
        }
    elif "DynamicCardVerificationCode" in data:
        import capo_payment_cryptography_data.types.dynamic_card_verification_code

        return {
            "DynamicCardVerificationCode": capo_payment_cryptography_data.types.dynamic_card_verification_code.deserialize_json(
                data["DynamicCardVerificationCode"]
            )
        }
    elif "DynamicCardVerificationValue" in data:
        import capo_payment_cryptography_data.types.dynamic_card_verification_value

        return {
            "DynamicCardVerificationValue": capo_payment_cryptography_data.types.dynamic_card_verification_value.deserialize_json(
                data["DynamicCardVerificationValue"]
            )
        }
    else:
        raise DeserializationError(
            "CardGenerationAttributes: no recognized variant key"
        )
