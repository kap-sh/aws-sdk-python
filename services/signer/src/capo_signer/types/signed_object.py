"""Generated from Smithy shape ``com.amazonaws.signer#SignedObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.s3_signed_object


class SignedObject(TypedDict, closed=True):
    s3: NotRequired["capo_signer.types.s3_signed_object.S3SignedObject"]
    """<p>The <code>S3SignedObject</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SignedObject) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_signer.types.s3_signed_object

        out["s3"] = capo_signer.types.s3_signed_object.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> SignedObject:
    out: SignedObject = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import capo_signer.types.s3_signed_object

        out["s3"] = capo_signer.types.s3_signed_object.deserialize_json(data["s3"])
    return out
