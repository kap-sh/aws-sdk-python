"""Generated from Smithy shape ``com.amazonaws.iot#KeyPair``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_iot.types.private_key
    import aws_sdk_iot.types.public_key


class KeyPair(TypedDict):
    public_key: NotRequired["aws_sdk_iot.types.public_key.PublicKey"]
    """<p>The public key.</p>"""
    private_key: NotRequired["aws_sdk_iot.types.private_key.PrivateKey"]
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
