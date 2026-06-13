"""Generated from Smithy shape ``com.amazonaws.s3vectors#VectorBucket``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3vectors.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_s3vectors.types.encryption_configuration
    import aws_sdk_s3vectors.types.vector_bucket_arn
    import aws_sdk_s3vectors.types.vector_bucket_name


class VectorBucket(TypedDict):
    vector_bucket_name: "aws_sdk_s3vectors.types.vector_bucket_name.VectorBucketName"
    """<p>The name of the vector bucket. </p>"""
    vector_bucket_arn: "aws_sdk_s3vectors.types.vector_bucket_arn.VectorBucketArn"
    """<p>The Amazon Resource Name (ARN) of the vector bucket. </p>"""
    creation_time: "datetime.datetime"
    """<p>Date and time when the vector bucket was created. </p>"""
    encryption_configuration: NotRequired[
        "aws_sdk_s3vectors.types.encryption_configuration.EncryptionConfiguration"
    ]
    """<p>The encryption configuration for the vector bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VectorBucket) -> dict:
    out: dict = {}
    out["vectorBucketName"] = value["vector_bucket_name"]
    out["vectorBucketArn"] = value["vector_bucket_arn"]
    import aws_sdk_s3vectors.types._prelude.timestamp

    out["creationTime"] = aws_sdk_s3vectors.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "encryption_configuration" in value:
        import aws_sdk_s3vectors.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_s3vectors.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> VectorBucket:
    out: VectorBucket = {}  # type: ignore[typeddict-item]
    if "vectorBucketName" in data:
        out["vector_bucket_name"] = data["vectorBucketName"]
    else:
        raise DeserializationError("VectorBucket.vector_bucket_name required")
    if "vectorBucketArn" in data:
        out["vector_bucket_arn"] = data["vectorBucketArn"]
    else:
        raise DeserializationError("VectorBucket.vector_bucket_arn required")
    if "creationTime" in data:
        import aws_sdk_s3vectors.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_s3vectors.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("VectorBucket.creation_time required")
    if "encryptionConfiguration" in data:
        import aws_sdk_s3vectors.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_s3vectors.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
