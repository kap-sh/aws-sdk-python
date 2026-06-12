"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#GenerateAs2805KekValidationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_payment_cryptography_data.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.as2805_random_key_material
    import aws_sdk_payment_cryptography_data.types.key_arn
    import aws_sdk_payment_cryptography_data.types.key_check_value


class GenerateAs2805KekValidationOutput(TypedDict):
    key_arn: "aws_sdk_payment_cryptography_data.types.key_arn.KeyArn"
    """<p>The <code>keyARN</code> of sending KEK that Amazon Web Services Payment Cryptography validates for node-to-node initialization</p>"""
    key_check_value: (
        "aws_sdk_payment_cryptography_data.types.key_check_value.KeyCheckValue"
    )
    """<p>The key check value (KCV) of the sending KEK that Amazon Web Services Payment Cryptography validates for node-to-node initialization.</p>"""
    random_key_send: "aws_sdk_payment_cryptography_data.types.as2805_random_key_material.As2805RandomKeyMaterial"
    """<p>The random key generated for sending KEK validation.</p>"""
    random_key_receive: "aws_sdk_payment_cryptography_data.types.as2805_random_key_material.As2805RandomKeyMaterial"
    """<p>The random key generated for receiving KEK validation. The initiating node sends this key to its partner node for validation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GenerateAs2805KekValidationOutput) -> dict:
    out: dict = {}
    out["KeyArn"] = value["key_arn"]
    out["KeyCheckValue"] = value["key_check_value"]
    out["RandomKeySend"] = value["random_key_send"]
    out["RandomKeyReceive"] = value["random_key_receive"]
    return out


def deserialize_json(data: dict) -> GenerateAs2805KekValidationOutput:
    out: GenerateAs2805KekValidationOutput = {}  # type: ignore[typeddict-item]
    if "KeyArn" in data:
        out["key_arn"] = data["KeyArn"]
    else:
        raise DeserializationError("GenerateAs2805KekValidationOutput.key_arn required")
    if "KeyCheckValue" in data:
        out["key_check_value"] = data["KeyCheckValue"]
    else:
        raise DeserializationError(
            "GenerateAs2805KekValidationOutput.key_check_value required"
        )
    if "RandomKeySend" in data:
        out["random_key_send"] = data["RandomKeySend"]
    else:
        raise DeserializationError(
            "GenerateAs2805KekValidationOutput.random_key_send required"
        )
    if "RandomKeyReceive" in data:
        out["random_key_receive"] = data["RandomKeyReceive"]
    else:
        raise DeserializationError(
            "GenerateAs2805KekValidationOutput.random_key_receive required"
        )
    return out
