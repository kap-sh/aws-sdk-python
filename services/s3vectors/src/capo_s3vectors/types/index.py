"""Generated from Smithy shape ``com.amazonaws.s3vectors#Index``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_s3vectors.types.data_type
    import capo_s3vectors.types.dimension
    import capo_s3vectors.types.distance_metric
    import capo_s3vectors.types.encryption_configuration
    import capo_s3vectors.types.index_arn
    import capo_s3vectors.types.index_name
    import capo_s3vectors.types.metadata_configuration
    import capo_s3vectors.types.vector_bucket_name


class Index(TypedDict, closed=True):
    vector_bucket_name: "capo_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket that contains the vector index. </p>"""
    index_name: "capo_s3vectors.types.index_name.IndexName"
    """<p>The name of the vector index.</p>"""
    index_arn: "capo_s3vectors.types.index_arn.IndexArn"
    """<p>The Amazon Resource Name (ARN) of the vector index.</p>"""
    creation_time: "datetime.datetime"
    """<p>Date and time when the vector index was created. </p>"""
    data_type: "capo_s3vectors.types.data_type.DataType"
    """<p>The data type of the vectors inserted into the vector index. </p>"""
    dimension: "capo_s3vectors.types.dimension.Dimension"
    """<p>The number of values in the vectors that are inserted into the vector index. </p>"""
    distance_metric: "capo_s3vectors.types.distance_metric.DistanceMetric"
    """<p>The distance metric to be used for similarity search. </p>"""
    metadata_configuration: NotRequired[
        "capo_s3vectors.types.metadata_configuration.MetadataConfiguration"
    ]
    """<p>The metadata configuration for the vector index. </p>"""
    encryption_configuration: NotRequired[
        "capo_s3vectors.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for a vector index. By default, if you don't specify, all new vectors in the vector index will use the encryption configuration of the vector bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Index) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    out["indexName"] = value["index_name"]
    out["indexArn"] = value["index_arn"]
    import capo_s3vectors.types._prelude.timestamp

    out["creationTime"] = capo_s3vectors.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    import capo_s3vectors.types.data_type

    out["dataType"] = capo_s3vectors.types.data_type.serialize_json(value["data_type"])
    out["dimension"] = value["dimension"]
    import capo_s3vectors.types.distance_metric

    out["distanceMetric"] = capo_s3vectors.types.distance_metric.serialize_json(
        value["distance_metric"]
    )
    if "metadata_configuration" in value:
        import capo_s3vectors.types.metadata_configuration

        out["metadataConfiguration"] = (
            capo_s3vectors.types.metadata_configuration.serialize_json(
                value["metadata_configuration"]
            )
        )
    if "encryption_configuration" in value:
        import capo_s3vectors.types.encryption_configuration

        out["encryptionConfiguration"] = (
            capo_s3vectors.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Index:
    out: Index = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        raise DeserializationError("Index.vector_bucket_name required")
    if "indexName" in data:
        out["index_name"] = data["indexName"]
    else:
        raise DeserializationError("Index.index_name required")
    if "indexArn" in data:
        out["index_arn"] = data["indexArn"]
    else:
        raise DeserializationError("Index.index_arn required")
    if "creationTime" in data:
        import capo_s3vectors.types._prelude.timestamp

        out["creation_time"] = capo_s3vectors.types._prelude.timestamp.deserialize_json(
            data["creationTime"]
        )
    else:
        raise DeserializationError("Index.creation_time required")
    if "dataType" in data:
        import capo_s3vectors.types.data_type

        out["data_type"] = capo_s3vectors.types.data_type.deserialize_json(
            data["dataType"]
        )
    else:
        raise DeserializationError("Index.data_type required")
    if "dimension" in data:
        out["dimension"] = data["dimension"]
    else:
        raise DeserializationError("Index.dimension required")
    if "distanceMetric" in data:
        import capo_s3vectors.types.distance_metric

        out["distance_metric"] = capo_s3vectors.types.distance_metric.deserialize_json(
            data["distanceMetric"]
        )
    else:
        raise DeserializationError("Index.distance_metric required")
    if "metadataConfiguration" in data:
        import capo_s3vectors.types.metadata_configuration

        out["metadata_configuration"] = (
            capo_s3vectors.types.metadata_configuration.deserialize_json(
                data["metadataConfiguration"]
            )
        )
    if "encryptionConfiguration" in data:
        import capo_s3vectors.types.encryption_configuration

        out["encryption_configuration"] = (
            capo_s3vectors.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
