"""Generated from Smithy shape ``com.amazonaws.s3vectors#DeleteVectorsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.delete_vectors_input_list
    import aws_sdk_s3vectors.types.index_arn
    import aws_sdk_s3vectors.types.index_name
    import aws_sdk_s3vectors.types.vector_bucket_name


class DeleteVectorsInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: NotRequired["aws_sdk_s3vectors.types.index_name.IndexName"]
    """<p>The name of the vector index that contains a vector you want to delete.</p>"""
    index_arn: NotRequired["aws_sdk_s3vectors.types.index_arn.IndexArn"]
    """<p>The ARN of the vector index that contains a vector you want to delete.</p>"""
    keys: "aws_sdk_s3vectors.types.delete_vectors_input_list.DeleteVectorsInputList"
    """<p>The keys of the vectors to delete. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteVectorsInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "index_name" in value:
        out["indexName"] = value["index_name"]
    if "index_arn" in value:
        out["indexArn"] = value["index_arn"]
    import aws_sdk_s3vectors.types.delete_vectors_input_list

    out["keys"] = aws_sdk_s3vectors.types.delete_vectors_input_list.serialize_json(
        value["keys"]
    )
    return out


def deserialize_json(data: dict) -> DeleteVectorsInput:
    out: DeleteVectorsInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    if "keys" in data:
        import aws_sdk_s3vectors.types.delete_vectors_input_list

        out["keys"] = (
            aws_sdk_s3vectors.types.delete_vectors_input_list.deserialize_json(
                data["keys"]
            )
        )
    else:
        raise DeserializationError("DeleteVectorsInput.keys required")
    return out
