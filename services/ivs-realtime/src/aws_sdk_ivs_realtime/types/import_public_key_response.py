"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ImportPublicKeyResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_ivs_realtime.types.public_key


class ImportPublicKeyResponse(TypedDict):
    public_key: NotRequired["aws_sdk_ivs_realtime.types.public_key.PublicKey"]
    """<p>The public key that was imported.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportPublicKeyResponse) -> dict:
    out: dict = {}
    if "public_key" in value:
        import aws_sdk_ivs_realtime.types.public_key

        out["publicKey"] = aws_sdk_ivs_realtime.types.public_key.serialize_json(
            value["public_key"]
        )
    return out


def deserialize_json(data: dict) -> ImportPublicKeyResponse:
    out: ImportPublicKeyResponse = {}  # type: ignore[typeddict-item]
    if "publicKey" in data:
        import aws_sdk_ivs_realtime.types.public_key

        out["public_key"] = aws_sdk_ivs_realtime.types.public_key.deserialize_json(
            data["publicKey"]
        )
    return out
