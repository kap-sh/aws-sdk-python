"""Generated from Smithy shape ``com.amazonaws.signer#Destination``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_signer.types.s3_destination


class Destination(TypedDict):
    s3: NotRequired["aws_sdk_signer.types.s3_destination.S3Destination"]
    """<p>The <code>S3Destination</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Destination) -> dict:
    out: dict = {}
    if "s3" in value:
        import aws_sdk_signer.types.s3_destination

        out["s3"] = aws_sdk_signer.types.s3_destination.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> Destination:
    out: Destination = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import aws_sdk_signer.types.s3_destination

        out["s3"] = aws_sdk_signer.types.s3_destination.deserialize_json(data["s3"])
    return out
