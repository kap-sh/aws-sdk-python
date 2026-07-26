"""Generated from Smithy shape ``com.amazonaws.s3vectors#VectorBucketSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_s3vectors.types.vector_bucket_arn
    import capo_s3vectors.types.vector_bucket_name


class VectorBucketSummary(TypedDict, closed=True):
    vector_bucket_name: "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket. </p>"""
    vector_bucket_arn: "capo_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    """<p>The Amazon Resource Name (ARN) of the vector bucket. </p>"""
    creation_time: "datetime.datetime"
    """<p>Date and time when the vector bucket was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorBucketSummary) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    out["vectorBucketArn"] = value["vector_bucket_arn"]
    import capo_s3vectors.types._prelude.timestamp

    out["creationTime"] = capo_s3vectors.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> VectorBucketSummary:
    out: VectorBucketSummary = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        raise DeserializationError("VectorBucketSummary.vector_bucket_name required")
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    else:
        raise DeserializationError("VectorBucketSummary.vector_bucket_arn required")
    if "creationTime" in data:
        import capo_s3vectors.types._prelude.timestamp

        out["creation_time"] = capo_s3vectors.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("VectorBucketSummary.creation_time required")
    return out
