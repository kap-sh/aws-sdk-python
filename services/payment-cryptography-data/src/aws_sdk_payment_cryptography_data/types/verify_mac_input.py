"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#VerifyMacInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.integer_range_between4_and32
    import aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type
    import aws_sdk_payment_cryptography_data.types.mac_attributes
    import aws_sdk_payment_cryptography_data.types.mac_type
    import aws_sdk_payment_cryptography_data.types.message_data_type


class VerifyMacInput(TypedDict, closed=True):
    key_identifier: "aws_sdk_payment_cryptography_data.types.key_arn_or_key_alias_type.KeyArnOrKeyAliasType"
    """<p>The <code>keyARN</code> of the encryption key that Amazon Web Services Payment Cryptography uses to verify MAC data.</p>"""
    message_data: (
        "aws_sdk_payment_cryptography_data.types.message_data_type.MessageDataType"
    )
    """<p>The data on for which MAC is under verification. This value must be hexBinary.</p>"""
    mac: "aws_sdk_payment_cryptography_data.types.mac_type.MacType"
    """<p>The MAC being verified.</p>"""
    verification_attributes: (
        "aws_sdk_payment_cryptography_data.types.mac_attributes.MacAttributes"
    )
    """<p>The attributes and data values to use for MAC verification within Amazon Web Services Payment Cryptography.</p>"""
    mac_length: NotRequired[
        "aws_sdk_payment_cryptography_data.types.integer_range_between4_and32.IntegerRangeBetween4And32"
    ]
    """<p>The length of the MAC.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VerifyMacInput) -> dict:
    out: dict = {}
    out["KeyIdentifier"] = value["key_identifier"]
    out["MessageData"] = value["message_data"]
    out["Mac"] = value["mac"]
    import aws_sdk_payment_cryptography_data.types.mac_attributes

    out["VerificationAttributes"] = (
        aws_sdk_payment_cryptography_data.types.mac_attributes.serialize_json(
            value["verification_attributes"]
        )
    )
    if "mac_length" in value:
        out["MacLength"] = value["mac_length"]
    return out


def deserialize_json(data: dict) -> VerifyMacInput:
    out: VerifyMacInput = {}  # type: ignore[typeddict-item]
    if "KeyIdentifier" in data:
        out["key_identifier"] = data["KeyIdentifier"]
    else:
        raise DeserializationError("VerifyMacInput.key_identifier required")
    if "MessageData" in data:
        out["message_data"] = data["MessageData"]
    else:
        raise DeserializationError("VerifyMacInput.message_data required")
    if "Mac" in data:
        out["mac"] = data["Mac"]
    else:
        raise DeserializationError("VerifyMacInput.mac required")
    if "VerificationAttributes" in data:
        import aws_sdk_payment_cryptography_data.types.mac_attributes

        out["verification_attributes"] = (
            aws_sdk_payment_cryptography_data.types.mac_attributes.deserialize_json(
                data["VerificationAttributes"]
            )
        )
    else:
        raise DeserializationError("VerifyMacInput.verification_attributes required")
    if "MacLength" in data:
        out["mac_length"] = data["MacLength"]
    return out
