"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#CardVerificationAttributes``."""

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
    import capo_payment_cryptography_data.types.discover_dynamic_card_verification_code
    import capo_payment_cryptography_data.types.dynamic_card_verification_code
    import capo_payment_cryptography_data.types.dynamic_card_verification_value


class _CardVerificationAttributes_AmexCardSecurityCodeVersion1(TypedDict, closed=True):
    AmexCardSecurityCodeVersion1: "capo_payment_cryptography_data.types.amex_card_security_code_version1.AmexCardSecurityCodeVersion1"


class _CardVerificationAttributes_AmexCardSecurityCodeVersion2(TypedDict, closed=True):
    AmexCardSecurityCodeVersion2: "capo_payment_cryptography_data.types.amex_card_security_code_version2.AmexCardSecurityCodeVersion2"


class _CardVerificationAttributes_CardVerificationValue1(TypedDict, closed=True):
    CardVerificationValue1: "capo_payment_cryptography_data.types.card_verification_value1.CardVerificationValue1"


class _CardVerificationAttributes_CardVerificationValue2(TypedDict, closed=True):
    CardVerificationValue2: "capo_payment_cryptography_data.types.card_verification_value2.CardVerificationValue2"


class _CardVerificationAttributes_CardHolderVerificationValue(TypedDict, closed=True):
    CardHolderVerificationValue: "capo_payment_cryptography_data.types.card_holder_verification_value.CardHolderVerificationValue"


class _CardVerificationAttributes_DynamicCardVerificationCode(TypedDict, closed=True):
    DynamicCardVerificationCode: "capo_payment_cryptography_data.types.dynamic_card_verification_code.DynamicCardVerificationCode"


class _CardVerificationAttributes_DynamicCardVerificationValue(TypedDict, closed=True):
    DynamicCardVerificationValue: "capo_payment_cryptography_data.types.dynamic_card_verification_value.DynamicCardVerificationValue"


class _CardVerificationAttributes_DiscoverDynamicCardVerificationCode(
    TypedDict, closed=True
):
    DiscoverDynamicCardVerificationCode: "capo_payment_cryptography_data.types.discover_dynamic_card_verification_code.DiscoverDynamicCardVerificationCode"


CardVerificationAttributes: TypeAlias = (
    _CardVerificationAttributes_AmexCardSecurityCodeVersion1
    | _CardVerificationAttributes_AmexCardSecurityCodeVersion2
    | _CardVerificationAttributes_CardVerificationValue1
    | _CardVerificationAttributes_CardVerificationValue2
    | _CardVerificationAttributes_CardHolderVerificationValue
    | _CardVerificationAttributes_DynamicCardVerificationCode
    | _CardVerificationAttributes_DynamicCardVerificationValue
    | _CardVerificationAttributes_DiscoverDynamicCardVerificationCode
)


# --- restJson1 ser/de ---
def serialize_json(value: CardVerificationAttributes) -> dict:
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
    elif "DiscoverDynamicCardVerificationCode" in value:
        import capo_payment_cryptography_data.types.discover_dynamic_card_verification_code

        return {
            "DiscoverDynamicCardVerificationCode": capo_payment_cryptography_data.types.discover_dynamic_card_verification_code.serialize_json(
                value["DiscoverDynamicCardVerificationCode"]
            )
        }
    else:
        raise SerializationError("CardVerificationAttributes: no variant present")


def deserialize_json(data: dict) -> CardVerificationAttributes:
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
    elif "DiscoverDynamicCardVerificationCode" in data:
        import capo_payment_cryptography_data.types.discover_dynamic_card_verification_code

        return {
            "DiscoverDynamicCardVerificationCode": capo_payment_cryptography_data.types.discover_dynamic_card_verification_code.deserialize_json(
                data["DiscoverDynamicCardVerificationCode"]
            )
        }
    else:
        raise DeserializationError(
            "CardVerificationAttributes: no recognized variant key"
        )
