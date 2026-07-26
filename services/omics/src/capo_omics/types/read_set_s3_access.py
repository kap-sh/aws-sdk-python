"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetS3Access``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.s3_uri


class ReadSetS3Access(TypedDict, closed=True):
    s3_uri: NotRequired["capo_omics.types.s3_uri.S3Uri"]
    """<p>The S3 URI for each read set file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetS3Access) -> dict:
    out: dict = {}
    if "s3_uri" in value:
        out["s3Uri"] = value["s3_uri"]
    return out


def deserialize_json(data: dict) -> ReadSetS3Access:
    out: ReadSetS3Access = {}  # type: ignore[typeddict-item]
    if "s3Uri" in data:
        out["s3_uri"] = data["s3Uri"]
    return out
