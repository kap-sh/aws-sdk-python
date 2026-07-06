"""Generated from Smithy shape ``com.amazonaws.omics#AnnotationImportItemSource``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_omics.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_omics.types.s3_uri


class AnnotationImportItemSource(TypedDict, closed=True):
    source: "aws_sdk_omics.types.s3_uri.S3Uri"
    """<p>The source file's location in Amazon S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AnnotationImportItemSource) -> dict:
    out: dict = {}
    out["source"] = value["source"]
    return out


def deserialize_json(data: dict) -> AnnotationImportItemSource:
    out: AnnotationImportItemSource = {}  # type: ignore[typeddict-item]
    if "source" in data:
        out["source"] = data["source"]
    else:
        raise DeserializationError("AnnotationImportItemSource.source required")
    return out
