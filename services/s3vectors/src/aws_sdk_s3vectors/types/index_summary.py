"""Generated from Smithy shape ``com.amazonaws.s3vectors#IndexSummary``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_s3vectors.types.index_arn
    import aws_sdk_s3vectors.types.index_name
    import aws_sdk_s3vectors.types.vector_bucket_name


class IndexSummary(TypedDict):
    vector_bucket_name: "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: "aws_sdk_s3vectors.types.index_name.IndexName"
    """<p>The name of the vector index.</p>"""
    index_arn: "aws_sdk_s3vectors.types.index_arn.IndexArn"
    """<p>The Amazon Resource Name (ARN) of the vector index.</p>"""
    creation_time: "datetime.datetime"
    """<p>Date and time when the vector index was created. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IndexSummary) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    out["indexName"] = value["index_name"]
    out["indexArn"] = value["index_arn"]
    import aws_sdk_s3vectors.types._prelude.timestamp

    out["creationTime"] = aws_sdk_s3vectors.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    return out


def deserialize_json(data: dict) -> IndexSummary:
    out: IndexSummary = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        raise DeserializationError("IndexSummary.vector_bucket_name required")
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    else:
        raise DeserializationError("IndexSummary.index_name required")
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    else:
        raise DeserializationError("IndexSummary.index_arn required")
    if "creationTime" in data:
        import aws_sdk_s3vectors.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_s3vectors.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("IndexSummary.creation_time required")
    return out
