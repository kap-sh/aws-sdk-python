"""Generated from Smithy shape ``com.amazonaws.s3vectors#QueryOutputVector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_key
    import aws_sdk_s3vectors.types.vector_metadata


class QueryOutputVector(TypedDict, closed=True):
    distance: NotRequired["float"]
    """<p>The measure of similarity between the vector in the response and the query vector.</p>"""
    key: "aws_sdk_s3vectors.types.vector_key.VectorKey"
    """<p>The key of the vector in the approximate nearest neighbor search.</p>"""
    metadata: NotRequired["aws_sdk_s3vectors.types.vector_metadata.VectorMetadata"]
    """<p>The metadata associated with the vector, if requested.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QueryOutputVector) -> dict:
    out: dict = {}
    if "distance" in value:
        out["distance"] = value["distance"]
    out["key"] = value["key"]
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> QueryOutputVector:
    out: QueryOutputVector = {}  # type: ignore[typeddict-item]
    if "distance" in data:
        out["distance"] = data["distance"]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("QueryOutputVector.key required")
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    return out
