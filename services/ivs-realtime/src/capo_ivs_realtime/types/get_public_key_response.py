"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#GetPublicKeyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.public_key


class GetPublicKeyResponse(TypedDict, closed=True):
    public_key: NotRequired["capo_ivs_realtime.types.public_key.PublicKey"]
    """<p>The public key that is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPublicKeyResponse) -> dict:
    out: dict = {}
    if "public_key" in value:
        import capo_ivs_realtime.types.public_key

        out["publicKey"] = capo_ivs_realtime.types.public_key.serialize_json(
            value["public_key"]
        )
    return out


def deserialize_json(data: dict) -> GetPublicKeyResponse:
    out: GetPublicKeyResponse = {}  # type: ignore[typeddict-item]
    if "publicKey" in data:
        import capo_ivs_realtime.types.public_key

        out["public_key"] = capo_ivs_realtime.types.public_key.deserialize_json(
            data["publicKey"]
        )
    return out
