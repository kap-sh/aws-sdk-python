"""Generated from Smithy shape ``com.amazonaws.signer#Source``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_signer.types.s3_source


class Source(TypedDict, closed=True):
    s3: NotRequired["capo_signer.types.s3_source.S3Source"]
    """<p>The <code>S3Source</code> object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Source) -> dict:
    out: dict = {}
    if "s3" in value:
        import capo_signer.types.s3_source

        out["s3"] = capo_signer.types.s3_source.serialize_json(value["s3"])
    return out


def deserialize_json(data: dict) -> Source:
    out: Source = {}  # type: ignore[typeddict-item]
    if "s3" in data:
        import capo_signer.types.s3_source

        out["s3"] = capo_signer.types.s3_source.deserialize_json(data["s3"])
    return out
