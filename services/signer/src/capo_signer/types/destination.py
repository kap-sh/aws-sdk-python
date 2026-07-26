"""Generated from Smithy shape ``com.amazonaws.signer#Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.s3_destination


class Destination(TypedDict, closed=True):
    s3: NotRequired["capo_signer.types.s3_destination.S3Destination"]
    """<p>The <code>S3Destination</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_signer.types.s3_destination

        out["s3"] = capo_signer.types.s3_destination.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import capo_signer.types.s3_destination

        out["s3"] = capo_signer.types.s3_destination.deserialize_json(data["s3"])
    return out
