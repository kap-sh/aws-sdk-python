"""Generated from Smithy shape ``com.amazonaws.s3vectors#CreateIndexInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3vectors.types.data_type
    import aws_sdk_s3vectors.types.dimension
    import aws_sdk_s3vectors.types.distance_metric
    import aws_sdk_s3vectors.types.encryption_configuration
    import aws_sdk_s3vectors.types.index_name
    import aws_sdk_s3vectors.types.metadata_configuration
    import aws_sdk_s3vectors.types.tags_map
    import aws_sdk_s3vectors.types.vector_bucket_arn
    import aws_sdk_s3vectors.types.vector_bucket_name


class CreateIndexInput(TypedDict, closed=True):
    vector_bucket_name: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    ]
    """<p>The name of the vector bucket to create the vector index in. </p>"""
    vector_bucket_arn: NotRequired[
        "aws_sdk_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the vector bucket to create the vector index in.</p>"""
    index_name: "aws_sdk_s3vectors.types.index_name.IndexName"
    """<p>The name of the vector index to create. </p>"""
    data_type: "aws_sdk_s3vectors.types.data_type.DataType"
    """<p>The data type of the vectors to be inserted into the vector index. </p>"""
    dimension: "aws_sdk_s3vectors.types.dimension.Dimension"
    """<p>The dimensions of the vectors to be inserted into the vector index. </p>"""
    distance_metric: "aws_sdk_s3vectors.types.distance_metric.DistanceMetric"
    """<p>The distance metric to be used for similarity search. </p>"""
    metadata_configuration: NotRequired[
        "aws_sdk_s3vectors.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>The metadata configuration for the vector index. </p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_s3vectors.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.</p>"""
    tags: NotRequired["aws_sdk_s3vectors.types.tags_map.TagsMap"]
    r"""<p>An array of user-defined tags that you would like to apply to the vector index that you are creating. A tag is a key-value pair that you apply to your resources. Tags can help you organize, track costs, and control access to resources. For more information, see <a href=\"https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging.html\">Tagging for cost allocation or attribute-based access control (ABAC)</a>.</p> <note> <p>You must have the <code>s3vectors:TagResource</code> permission in addition to <code>s3vectors:CreateIndex</code> permission to create a vector index with tags.</p> </note>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIndexInput) -> dict:
    out: dict = {}
    if "vector_bucket_name" in value:
        out["vectorBucketName"] = value["vector_bucket_name"]
    if "vector_bucket_arn" in value:
        out["vectorBucketArn"] = value["vector_bucket_arn"]
    out["indexName"] = value["index_name"]
    import aws_sdk_s3vectors.types.data_type

    out["dataType"] = aws_sdk_s3vectors.types.data_type.serialize_json(
        value["data_type"]
    )
    out["dimension"] = value["dimension"]
    import aws_sdk_s3vectors.types.distance_metric

    out["distanceMetric"] = aws_sdk_s3vectors.types.distance_metric.serialize_json(
        value["distance_metric"]
    )
    if "metadata_configuration" in value:
        import aws_sdk_s3vectors.types.metadata_configuration

        out["metadataConfiguration"] = (
            aws_sdk_s3vectors.types.metadata_configuration.serialize_json(
                value["metadata_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import aws_sdk_s3vectors.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_s3vectors.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_s3vectors.types.tags_map

        out["tags"] = aws_sdk_s3vectors.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIndexInput:
    out: CreateIndexInput = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    else:
        raise DeserializationError("CreateIndexInput.index_name required")
    if "dataType" in data:
        import aws_sdk_s3vectors.types.data_type

        out["data_type"] = aws_sdk_s3vectors.types.data_type.deserialize_json(
            data["dataType"]
        )
    else:
        raise DeserializationError("CreateIndexInput.data_type required")
    if "dimension" in data:
        out["dimension"] = data["dimension"]
    else:
        raise DeserializationError("CreateIndexInput.dimension required")
    if "distanceMetric" in data:
        import aws_sdk_s3vectors.types.distance_metric

        out["distance_metric"] = (
            aws_sdk_s3vectors.types.distance_metric.deserialize_json(
                data["distanceMetric"]
            )
        )
    else:
        raise DeserializationError("CreateIndexInput.distance_metric required")
    if "metadataConfiguration" in data:
        import aws_sdk_s3vectors.types.metadata_configuration

        out["metadata_configuration"] = (
            aws_sdk_s3vectors.types.metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    if "encryptionConfiguration" in data:
        import aws_sdk_s3vectors.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_s3vectors.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_s3vectors.types.tags_map

        out["tags"] = aws_sdk_s3vectors.types.tags_map.deserialize_json(data["tags"])
    return out
