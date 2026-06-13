"""Generated from Smithy shape ``com.amazonaws.s3vectors#ListOutputVector``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_data
    import aws_sdk_s3vectors.types.vector_key
    import aws_sdk_s3vectors.types.vector_metadata


class ListOutputVector(TypedDict):
    key: "aws_sdk_s3vectors.types.vector_key.VectorKey"
    """<p>The name of the vector. </p>"""
    data: NotRequired["aws_sdk_s3vectors.types.vector_data.VectorData"]
    """<p>The vector data of the vector. </p>"""
    metadata: NotRequired["aws_sdk_s3vectors.types.vector_metadata.VectorMetadata"]
    """<p>Metadata about the vector. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListOutputVector) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    if "data" in value:
        import aws_sdk_s3vectors.types.vector_data

        out["data"] = aws_sdk_s3vectors.types.vector_data.serialize_json(value["data"])
    if "metadata" in value:
        out["metadata"] = value["metadata"]
    return out


def deserialize_json(data: dict) -> ListOutputVector:
    out: ListOutputVector = {}  # type: ignore[typeddict-item]
    if "key" in data:
        out["key"] = data["key"]
    else:
        raise DeserializationError("ListOutputVector.key required")
    if "data" in data:
        import aws_sdk_s3vectors.types.vector_data

        out["data"] = aws_sdk_s3vectors.types.vector_data.deserialize_json(data["data"])
    if "metadata" in data:
        out["metadata"] = data["metadata"]
    return out
