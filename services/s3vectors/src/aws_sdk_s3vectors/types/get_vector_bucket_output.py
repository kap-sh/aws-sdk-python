"""Generated from Smithy shape ``com.amazonaws.s3vectors#GetVectorBucketOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.vector_bucket


class GetVectorBucketOutput(TypedDict):
    vector_bucket: "aws_sdk_s3vectors.types.vector_bucket.VectorBucket"
    """<p>The attributes of the vector bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetVectorBucketOutput) -> dict:
    out: dict = {}
    import aws_sdk_s3vectors.types.vector_bucket

    out["vectorBucket"] = aws_sdk_s3vectors.types.vector_bucket.serialize_json(
        value["vector_bucket"]
    )
    return out


def deserialize_json(data: dict) -> GetVectorBucketOutput:
    out: GetVectorBucketOutput = {}  # type: ignore[typeddict-item]
    if "vectorBucket" in data:
        import aws_sdk_s3vectors.types.vector_bucket

        out["vector_bucket"] = aws_sdk_s3vectors.types.vector_bucket.deserialize_json(
            data["vectorBucket"]
        )
    else:
        raise DeserializationError("GetVectorBucketOutput.vector_bucket required")
    return out
