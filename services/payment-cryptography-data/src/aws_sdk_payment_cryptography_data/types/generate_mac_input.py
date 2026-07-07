"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateMacInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.integer_range_between4_and32
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.mac_attributes
    import aws_sdk_payment_cryptography_data.types.message_data_type


class GenerateMacInput(TypedDict, closed=True):
    key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the MAC generation encryption key.</p>"""
    message_data: (
        "aws_sdk_payment_cryptography_data.types.message_data_type.MessageDataType"
    )
    """<p>The data for which a MAC is under generation. This value must be hexBinary.</p>"""
    generation_attributes: (
        "aws_sdk_payment_cryptography_data.types.mac_attributes.MacAttributes"
    )
    """<p>The attributes and data values to use for MAC generation within Amazon Web Services Payment Cryptography.</p>"""
    mac_length: NotRequired[
        "aws_sdk_payment_cryptography_data.types.integer_range_between4_and32.IntegerRangeBetween4And32"
    ]
    """<p>The length of a MAC under generation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateMacInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["MessageData"] = value["message_data"]
    import aws_sdk_payment_cryptography_data.types.mac_attributes

    out["GenerationAttributes"] = (
        aws_sdk_payment_cryptography_data.types.mac_attributes.serialize_json(
            value["generation_attributes"]
        )
    )
    if "mac_length" in value:
        out["MacLength"] = value["mac_length"]
    return out


def deserialize_json(data: dict) -> GenerateMacInput:
    out: GenerateMacInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError("GenerateMacInput.key_identifier required")
    if "MessageData" in data:
        out["message_data"] = data["MessageData"]
    else:
        raise DeserializationError("GenerateMacInput.message_data required")
    if "GenerationAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.mac_attributes

        out["generation_attributes"] = (
            aws_sdk_payment_cryptography_data.types.mac_attributes.deserialize_json(
                data["GenerationAttributes"]
            )
        )
    else:
        raise DeserializationError("GenerateMacInput.generation_attributes required")
    if "MacLength" in data:
        out["mac_length"] = data["MacLength"]
    return out
