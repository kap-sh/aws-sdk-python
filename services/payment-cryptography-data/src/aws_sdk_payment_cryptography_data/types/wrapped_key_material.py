"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#WrappedKeyMaterial``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_payment_cryptography_data.types.ecdh_derivation_attributes
    import aws_sdk_payment_cryptography_data.types.tr31_wrapped_key_block


class _WrappedKeyMaterial_Tr31KeyBlock(TypedDict):
    Tr31KeyBlock: "aws_sdk_payment_cryptography_data.types.tr31_wrapped_key_block.Tr31WrappedKeyBlock"


class _WrappedKeyMaterial_DiffieHellmanSymmetricKey(TypedDict):
    DiffieHellmanSymmetricKey: "aws_sdk_payment_cryptography_data.types.ecdh_derivation_attributes.EcdhDerivationAttributes"


WrappedKeyMaterial: TypeAlias = (
    _WrappedKeyMaterial_Tr31KeyBlock | _WrappedKeyMaterial_DiffieHellmanSymmetricKey
)


# --- restJson1 ser/de ---
def serialize_json(value: WrappedKeyMaterial) -> dict:
    if "Tr31KeyBlock" in value:
        return {"Tr31KeyBlock": value["Tr31KeyBlock"]}
    elif "DiffieHellmanSymmetricKey" in value:
        import aws_sdk_payment_cryptography_data.types.ecdh_derivation_attributes

        return {
            "DiffieHellmanSymmetricKey": aws_sdk_payment_cryptography_data.types.ecdh_derivation_attributes.serialize_json(
                value["DiffieHellmanSymmetricKey"]
            )
        }
    else:
        raise SerializationError("WrappedKeyMaterial: no variant present")


def deserialize_json(data: dict) -> WrappedKeyMaterial:
    if "Tr31KeyBlock" in data:
        return {"Tr31KeyBlock": data["Tr31KeyBlock"]}
    elif "DiffieHellmanSymmetricKey" in data:
        import aws_sdk_payment_cryptography_data.types.ecdh_derivation_attributes

        return {
            "DiffieHellmanSymmetricKey": aws_sdk_payment_cryptography_data.types.ecdh_derivation_attributes.deserialize_json(
                data["DiffieHellmanSymmetricKey"]
            )
        }
    else:
        raise DeserializationError("WrappedKeyMaterial: no recognized variant key")
