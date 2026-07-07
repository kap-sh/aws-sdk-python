"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateAs2805KekValidationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.as2805_kek_validation_type
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.random_key_send_variant_mask


class GenerateAs2805KekValidationInput(TypedDict, closed=True):
    key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of sending KEK that Amazon Web Services Payment Cryptography uses for node-to-node initialization</p>"""
    kek_validation_type: "aws_sdk_payment_cryptography_data.types.as2805_kek_validation_type.As2805KekValidationType"
    """<p>Defines whether to generate a KEK validation request or KEK validation response for node-to-node initialization.</p>"""
    random_key_send_variant_mask: "aws_sdk_payment_cryptography_data.types.random_key_send_variant_mask.RandomKeySendVariantMask"
    """<p>The key variant to use for generating a random key for KEK validation during node-to-node initialization.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateAs2805KekValidationInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    import aws_sdk_payment_cryptography_data.types.as2805_kek_validation_type

    out["KekValidationType"] = (
        aws_sdk_payment_cryptography_data.types.as2805_kek_validation_type.serialize_json(
            value["kek_validation_type"]
        )
    )
    import aws_sdk_payment_cryptography_data.types.random_key_send_variant_mask

    out["RandomKeySendVariantMask"] = (
        aws_sdk_payment_cryptography_data.types.random_key_send_variant_mask.serialize_json(
            value["random_key_send_variant_mask"]
        )
    )
    return out


def deserialize_json(data: dict) -> GenerateAs2805KekValidationInput:
    out: GenerateAs2805KekValidationInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError(
            "GenerateAs2805KekValidationInput.key_identifier required"
        )
    if "KekValidationType" in data:
        import aws_sdk_payment_cryptography_data.types.as2805_kek_validation_type

        out["kek_validation_type"] = (
            aws_sdk_payment_cryptography_data.types.as2805_kek_validation_type.deserialize_json(
                data["KekValidationType"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateAs2805KekValidationInput.kek_validation_type required"
        )
    if "RandomKeySendVariantMask" in data:
        import aws_sdk_payment_cryptography_data.types.random_key_send_variant_mask

        out["random_key_send_variant_mask"] = (
            aws_sdk_payment_cryptography_data.types.random_key_send_variant_mask.deserialize_json(
                data["RandomKeySendVariantMask"]
            )
        )
    else:
        raise DeserializationError(
            "GenerateAs2805KekValidationInput.random_key_send_variant_mask required"
        )
    return out
