"""Generated from Smithy shape ``com.amazonaws.paymentcryptographydata#IncomingKeyMaterial``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_payment_cryptography_data.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block


class _IncomingKeyMaterial_DiffieHellmanTr31KeyBlock(TypedDict, closed=True):
    DiffieHellmanTr31KeyBlock: "capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block.IncomingDiffieHellmanTr31KeyBlock"


IncomingKeyMaterial: TypeAlias = _IncomingKeyMaterial_DiffieHellmanTr31KeyBlock


# --- restJson1 ser/de ---
def serialize_json(value: IncomingKeyMaterial) -> dict:
    if "DiffieHellmanTr31KeyBlock" in value:
        import capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block.serialize_json(
                value["DiffieHellmanTr31KeyBlock"]
            )
        }
    else:
        raise SerializationError("IncomingKeyMaterial: no variant present")


def deserialize_json(data: dict) -> IncomingKeyMaterial:
    if "DiffieHellmanTr31KeyBlock" in data:
        import capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block

        return {
            "DiffieHellmanTr31KeyBlock": capo_payment_cryptography_data.types.incoming_diffie_hellman_tr31_key_block.deserialize_json(
                data["DiffieHellmanTr31KeyBlock"]
            )
        }
    else:
        raise DeserializationError("IncomingKeyMaterial: no recognized variant key")
