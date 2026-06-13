"""Generated from Smithy shape ``com.amazonaws.s3tables#PutTableBucketStorageClassRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.storage_class_configuration
    import aws_sdk_s3tables.types.table_bucket_arn


class PutTableBucketStorageClassRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    storage_class_configuration: (
        "aws_sdk_s3tables.types.storage_class_configuration.StorageClassConfiguration"
    )
    """<p>The storage class configuration to apply to the table bucket. This configuration will serve as the default for new tables created in this bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutTableBucketStorageClassRequest) -> dict:
    out: dict = {}
    import aws_sdk_s3tables.types.storage_class_configuration

    out["storageClassConfiguration"] = (
        aws_sdk_s3tables.types.storage_class_configuration.serialize_json(
            value["storage_class_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutTableBucketStorageClassRequest:
    out: PutTableBucketStorageClassRequest = {}  # type: ignore[typeddict-item]
    if "storageClassConfiguration" in data:
        import aws_sdk_s3tables.types.storage_class_configuration

        out["storage_class_configuration"] = (
            aws_sdk_s3tables.types.storage_class_configuration.deserialize_json(
                data["storageClassConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "PutTableBucketStorageClassRequest.storage_class_configuration required"
        )
    return out
