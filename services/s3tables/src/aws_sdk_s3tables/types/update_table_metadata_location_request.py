"""Generated from Smithy shape ``com.amazonaws.s3tables#UpdateTableMetadataLocationRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_s3tables.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_s3tables.types.metadata_location
    import aws_sdk_s3tables.types.namespace_name
    import aws_sdk_s3tables.types.table_bucket_arn
    import aws_sdk_s3tables.types.table_name
    import aws_sdk_s3tables.types.version_token


class UpdateTableMetadataLocationRequest(TypedDict):
    table_bucket_arn: "aws_sdk_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket. </p>"""
    namespace: "aws_sdk_s3tables.types.namespace_name.NamespaceName"
    """<p>The namespace of the table.</p>"""
    name: "aws_sdk_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    version_token: "aws_sdk_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table. </p>"""
    metadata_location: "aws_sdk_s3tables.types.metadata_location.MetadataLocation"
    """<p>The new metadata location for the table. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTableMetadataLocationRequest) -> dict:
    out: dict = {}
    out["versionToken"] = value["version_token"]
    out["metadataLocation"] = value["metadata_location"]
    return out


def deserialize_json(data: dict) -> UpdateTableMetadataLocationRequest:
    out: UpdateTableMetadataLocationRequest = {}  # type: ignore[typeddict-item]
    if "versionToken" in data:
        out["version_token"] = data["versionToken"]
    else:
        raise DeserializationError(
            "UpdateTableMetadataLocationRequest.version_token required"
        )
    if "metadataLocation" in data:
        out["metadata_location"] = data["metadataLocation"]
    else:
        raise DeserializationError(
            "UpdateTableMetadataLocationRequest.metadata_location required"
        )
    return out
