"""Generated from Smithy shape ``com.amazonaws.datazone#S3Destination``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.notebook_s3_uri


class S3Destination(TypedDict, closed=True):
    uri: NotRequired["aws_sdk_datazone.types.notebook_s3_uri.NotebookS3Uri"]
    """<p>The Amazon Simple Storage Service URI of the exported notebook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3Destination) -> dict:
    out: dict = {}
    if "uri" in value:
        out["uri"] = value["uri"]
    return out


def deserialize_json(data: dict) -> S3Destination:
    out: S3Destination = {}  # type: ignore[typeddict-item]
    if "uri" in data:
        out["uri"] = data["uri"]
    return out
