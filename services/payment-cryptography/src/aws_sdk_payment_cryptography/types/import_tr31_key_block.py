"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#ImportTr31KeyBlock``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography.types.tr31_wrapped_key_block


class ImportTr31KeyBlock(TypedDict):
    wrapping_key_identifier: "aws_sdk_payment_cryptography.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>KeyARN</code> of the key that will decrypt or unwrap a TR-31 key block during import.</p>"""
    wrapped_key_block: (
        "aws_sdk_payment_cryptography.types.tr31_wrapped_key_block.Tr31WrappedKeyBlock"
    )
    """<p>The TR-31 wrapped key block to import.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ImportTr31KeyBlock) -> dict:
    out: dict = {}
    out["WrappingKeyIdentifier"] = value["wrapping_key_identifier"]
    out["WrappedKeyBlock"] = value["wrapped_key_block"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ImportTr31KeyBlock:
    out: ImportTr31KeyBlock = {}  # type: ignore[typeddict-item]
    if "WrappingKeyIdentifier" in data:
        out["wrapping_key_identifier"] = data["WrappingKeyIdentifier"]
    else:
        raise DeserializationError(
            "ImportTr31KeyBlock.wrapping_key_identifier required"
        )
    if "WrappedKeyBlock" in data:
        out["wrapped_key_block"] = data["WrappedKeyBlock"]
    else:
        raise DeserializationError("ImportTr31KeyBlock.wrapped_key_block required")
    return out
