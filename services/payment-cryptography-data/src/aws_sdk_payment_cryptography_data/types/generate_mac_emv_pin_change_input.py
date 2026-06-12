"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateMacEmvPinChangeInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.command_message_data_type
    import aws_sdk_payment_cryptography_data.types.derivation_method_attributes
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.pin_block_format_for_emv_pin_change
    import aws_sdk_payment_cryptography_data.types.pin_block_length_equals16


class GenerateMacEmvPinChangeInput(TypedDict):
    new_pin_pek_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the PEK protecting the incoming new encrypted PIN block.</p>"""
    new_encrypted_pin_block: "aws_sdk_payment_cryptography_data.types.pin_block_length_equals16.PinBlockLengthEquals16"
    """<p>The incoming new encrypted PIN block data for offline pin change on an EMV card.</p>"""
    pin_block_format: "aws_sdk_payment_cryptography_data.types.pin_block_format_for_emv_pin_change.PinBlockFormatForEmvPinChange"
    """<p>The PIN encoding format of the incoming new encrypted PIN block as specified in ISO 9564.</p>"""
    secure_messaging_integrity_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the issuer master key (IMK-SMI) used to authenticate the issuer script response.</p>"""
    secure_messaging_confidentiality_key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the issuer master key (IMK-SMC) used to protect the PIN block data in the issuer script response.</p>"""
    message_data: "aws_sdk_payment_cryptography_data.types.command_message_data_type.CommandMessageDataType"
    """<p>The message data is the APDU command from the card reader or terminal. The target encrypted PIN block, after translation to ISO2 format, is appended to this message data to generate an issuer script response.</p>"""
    derivation_method_attributes: "aws_sdk_payment_cryptography_data.types.derivation_method_attributes.DerivationMethodAttributes"
    """<p>The attributes and data values to derive payment card specific confidentiality and integrity keys.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMacEmvPinChangeInput) -> dict:
    out: dict = {}
    out["NewPinPekIdentifier"] = value["new_pin_pek_identifier"]
    out["NewEncryptedPinBlock"] = value["new_encrypted_pin_block"]
    import aws_sdk_payment_cryptography_data.types.pin_block_format_for_emv_pin_change

    out["PinBlockFormat"] = (
        aws_sdk_payment_cryptography_data.types.pin_block_format_for_emv_pin_change.serialize_json(
            value["pin_block_format"]
        )
    )
    out["SecureMessagingIntegrityKeyIdentifier"] = value[
        "secure_messaging_integrity_key_identifier"
    ]
    out["SecureMessagingConfidentialityKeyIdentifier"] = value[
        "secure_messaging_confidentiality_key_identifier"
    ]
    out["MessageData"] = value["message_data"]
    import aws_sdk_payment_cryptography_data.types.derivation_method_attributes

    out["DerivationMethodAttributes"] = (
        aws_sdk_payment_cryptography_data.types.derivation_method_attributes.serialize_json(
            value["derivation_method_attributes"]
        )
    )
    return out


def deserialize_json(data: dict) -> GenerateMacEmvPinChangeInput:
    out: GenerateMacEmvPinChangeInput = {}  # type: ignore[typeddict-item]
    if "NewPinPekIdentifier" in data:
        out["new_pin_pek_identifier"] = data["NewPinPekIdentifier"]
    else:
        raise DeserializationError(
            "GenerateMacEmvPinChangeInput.new_pin_pek_identifier required"
        )
    if "NewEncryptedPinBlock" in data:
        out["new_encrypted_pin_block"] = data["NewEncryptedPinBlock"]
    else:
        raise DeserializationError(
            "GenerateMacEmvPinChangeInput.new_encrypted_pin_block required"
        )
    if "PinBlockFormat" in data:
        import aws_sdk_payment_cryptography_data.types.pin_block_format_for_emv_pin_change

        out["pin_block_format"] = (
            aws_sdk_payment_cryptography_data.types.pin_block_format_for_emv_pin_change.deserialize_json(
                data["PinBlockFormat"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateMacEmvPinChangeInput.pin_block_format required"
        )
    if "SecureMessagingIntegrityKeyIdentifier" in data:
        out["secure_messaging_integrity_key_identifier"] = data[
            "SecureMessagingIntegrityKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "GenerateMacEmvPinChangeInput.secure_messaging_integrity_key_identifier required"
        )
    if "SecureMessagingConfidentialityKeyIdentifier" in data:
        out["secure_messaging_confidentiality_key_identifier"] = data[
            "SecureMessagingConfidentialityKeyIdentifier"
        ]
    else:
        raise DeserializationError(
            "GenerateMacEmvPinChangeInput.secure_messaging_confidentiality_key_identifier required"
        )
    if "MessageData" in data:
        out["message_data"] = data["MessageData"]
    else:
        raise DeserializationError("GenerateMacEmvPinChangeInput.message_data required")
    if "DerivationMethodAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.derivation_method_attributes

        out["derivation_method_attributes"] = (
            aws_sdk_payment_cryptography_data.types.derivation_method_attributes.deserialize_json(
                data["DerivationMethodAttributes"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateMacEmvPinChangeInput.derivation_method_attributes required"
        )
    return out
