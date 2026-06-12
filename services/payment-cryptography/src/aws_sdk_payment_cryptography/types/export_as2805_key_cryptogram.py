"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ExportAs2805KeyCryptogram``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.as2805_key_variant
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type


class ExportAs2805KeyCryptogram(TypedDict):
    wrapping_key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    as2805_key_variant: (
        "aws_sdk_payment_cryptography.types.as2805_key_variant.As2805KeyVariant"
    )
    """<p>The cryptographic usage of the key under export.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ExportAs2805KeyCryptogram) -> dict:
    out: dict = {}
    out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    import aws_sdk_payment_cryptography.types.as2805_key_variant

    out["As2805KeyVariant"] = (
        aws_sdk_payment_cryptography.types.as2805_key_variant.serialize_aws_json_1_0(
            value["as2805_key_variant"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ExportAs2805KeyCryptogram:
    out: ExportAs2805KeyCryptogram = {}  # type: ignore[typeddict-item]
    if "WrappingKeyIdentifier" in data:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    else:
        raise DeserializationError(
            "ExportAs2805KeyCryptogram.wrapping_key_identifier required"
        )
    if "As2805KeyVariant" in data:
        import aws_sdk_payment_cryptography.types.as2805_key_variant

        out["as2805_key_variant"] = (
            aws_sdk_payment_cryptography.types.as2805_key_variant.deserialize_aws_json_1_0(
                data["As2805KeyVariant"]
            )
        )
    else:
        raise DeserializationError(
            "ExportAs2805KeyCryptogram.as2805_key_variant required"
        )
    return out
