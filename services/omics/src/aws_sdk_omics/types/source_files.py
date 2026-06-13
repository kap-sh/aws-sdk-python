"""Generated from Smithy shape ``com.amazonaws.omics#SourceFiles``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.s3_uri


class SourceFiles(TypedDict):
    source1: "aws_sdk_omics.types.s3_uri.S3Uri"
    """<p>The location of the first file in Amazon S3.</p>"""
    source2: NotRequired["aws_sdk_omics.types.s3_uri.S3Uri"]
    """<p>The location of the second file in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SourceFiles) -> dict:
    out: dict = {}
    out["source1"] = value["source1"]
    if "source2" in value:
        out["source2"] = value["source2"]
    return out


def deserialize_json(data: dict) -> SourceFiles:
    out: SourceFiles = {}  # type: ignore[typeddict-item]
    if "source1" in data:
        out["source1"] = data["source1"]
    else:
        raise DeserializationError("SourceFiles.source1 required")
    if "source2" in data:
        out["source2"] = data["source2"]
    return out
