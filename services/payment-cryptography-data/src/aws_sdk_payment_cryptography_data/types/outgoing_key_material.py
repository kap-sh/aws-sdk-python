"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#OutgoingKeyMaterial``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.outgoing_tr31_key_block


class _OutgoingKeyMaterial_Tr31KeyBlock(TypedDict):
    Tr31KeyBlock: "aws_sdk_payment_cryptography_data.types.outgoing_tr31_key_block.OutgoingTr31KeyBlock"


OutgoingKeyMaterial: TypeAlias = _OutgoingKeyMaterial_Tr31KeyBlock


# --- restJson1 ser/de ---
def serialize_json(value: OutgoingKeyMaterial) -> dict:
    if "Tr31KeyBlock" in value:
        import aws_sdk_payment_cryptography_data.types.outgoing_tr31_key_block

        return {
            "Tr31KeyBlock": aws_sdk_payment_cryptography_data.types.outgoing_tr31_key_block.serialize_json(
                value["Tr31KeyBlock"]
            )
        }
    else:
        raise SerializationError("OutgoingKeyMaterial: no variant present")


def deserialize_json(data: dict) -> OutgoingKeyMaterial:
    if "Tr31KeyBlock" in data:
        import aws_sdk_payment_cryptography_data.types.outgoing_tr31_key_block

        return {
            "Tr31KeyBlock": aws_sdk_payment_cryptography_data.types.outgoing_tr31_key_block.deserialize_json(
                data["Tr31KeyBlock"]
            )
        }
    else:
        raise DeserializationError("OutgoingKeyMaterial: no recognized variant key")
