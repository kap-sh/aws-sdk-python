"""Generated from Smithy shape ``com.amazonaws.iot#KeyPair``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iot.types.private_key
    import capo_iot.types.public_key


class KeyPair(TypedDict, closed=True):
    public_key: NotRequired["capo_iot.types.public_key.PublicKey"]
    """<p>The public key.</p>"""
    private_key: NotRequired["capo_iot.types.private_key.PrivateKey"]
    """<p>The private key.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KeyPair) -> dict:
    out: dict = {}
    if "public_key" in value:
        out["PublicKey"] = value["public_key"]
    if "private_key" in value:
        out["PrivateKey"] = value["private_key"]
    return out


def deserialize_json(data: dict) -> KeyPair:
    out: KeyPair = {}  # type: ignore[typeddict-item]
    if "PublicKey" in data:
        out["public_key"] = data["PublicKey"]
    if "PrivateKey" in data:
        out["private_key"] = data["PrivateKey"]
    return out
