"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#TranslationIsoFormats``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.translation_pin_data_as2805_format0
    import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034
    import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format1


class _TranslationIsoFormats_IsoFormat0(TypedDict):
    IsoFormat0: "aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.TranslationPinDataIsoFormat034"


class _TranslationIsoFormats_IsoFormat1(TypedDict):
    IsoFormat1: "aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format1.TranslationPinDataIsoFormat1"


class _TranslationIsoFormats_IsoFormat3(TypedDict):
    IsoFormat3: "aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.TranslationPinDataIsoFormat034"


class _TranslationIsoFormats_IsoFormat4(TypedDict):
    IsoFormat4: "aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.TranslationPinDataIsoFormat034"


class _TranslationIsoFormats_As2805Format0(TypedDict):
    As2805Format0: "aws_sdk_payment_cryptography_data.types.translation_pin_data_as2805_format0.TranslationPinDataAs2805Format0"


TranslationIsoFormats: TypeAlias = (
    _TranslationIsoFormats_IsoFormat0
    | _TranslationIsoFormats_IsoFormat1
    | _TranslationIsoFormats_IsoFormat3
    | _TranslationIsoFormats_IsoFormat4
    | _TranslationIsoFormats_As2805Format0
)


# --- restJson1 ser/de ---
def serialize_json(value: TranslationIsoFormats) -> dict:
    if "IsoFormat0" in value:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat0": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.serialize_json(
                value["IsoFormat0"]
            )
        }
    elif "IsoFormat1" in value:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format1

        return {
            "IsoFormat1": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format1.serialize_json(
                value["IsoFormat1"]
            )
        }
    elif "IsoFormat3" in value:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat3": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.serialize_json(
                value["IsoFormat3"]
            )
        }
    elif "IsoFormat4" in value:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat4": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.serialize_json(
                value["IsoFormat4"]
            )
        }
    elif "As2805Format0" in value:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_as2805_format0

        return {
            "As2805Format0": aws_sdk_payment_cryptography_data.types.translation_pin_data_as2805_format0.serialize_json(
                value["As2805Format0"]
            )
        }
    else:
        raise SerializationError("TranslationIsoFormats: no variant present")


def deserialize_json(data: dict) -> TranslationIsoFormats:
    if "IsoFormat0" in data:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat0": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.deserialize_json(
                data["IsoFormat0"]
            )
        }
    elif "IsoFormat1" in data:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format1

        return {
            "IsoFormat1": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format1.deserialize_json(
                data["IsoFormat1"]
            )
        }
    elif "IsoFormat3" in data:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat3": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.deserialize_json(
                data["IsoFormat3"]
            )
        }
    elif "IsoFormat4" in data:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034

        return {
            "IsoFormat4": aws_sdk_payment_cryptography_data.types.translation_pin_data_iso_format034.deserialize_json(
                data["IsoFormat4"]
            )
        }
    elif "As2805Format0" in data:
        import aws_sdk_payment_cryptography_data.types.translation_pin_data_as2805_format0

        return {
            "As2805Format0": aws_sdk_payment_cryptography_data.types.translation_pin_data_as2805_format0.deserialize_json(
                data["As2805Format0"]
            )
        }
    else:
        raise DeserializationError("TranslationIsoFormats: no recognized variant key")
