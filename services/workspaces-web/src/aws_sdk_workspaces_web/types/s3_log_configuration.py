"""Generated from Smithy shape ``com.amazonaws.workspacesweb#S3LogConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_workspaces_web.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workspaces_web.types.folder_structure
    import aws_sdk_workspaces_web.types.log_file_format
    import aws_sdk_workspaces_web.types.s3_bucket
    import aws_sdk_workspaces_web.types.s3_bucket_owner
    import aws_sdk_workspaces_web.types.s3_key_prefix


class S3LogConfiguration(TypedDict):
    bucket: "aws_sdk_workspaces_web.types.s3_bucket.S3Bucket"
    """<p>The S3 bucket name where logs are delivered.</p>"""
    key_prefix: NotRequired["aws_sdk_workspaces_web.types.s3_key_prefix.S3KeyPrefix"]
    """<p>The S3 path prefix that determines where log files are stored.</p>"""
    bucket_owner: NotRequired[
        "aws_sdk_workspaces_web.types.s3_bucket_owner.S3BucketOwner"
    ]
    """<p>The expected bucket owner of the target S3 bucket. The caller must have permissions to write to the target bucket.</p>"""
    log_file_format: "aws_sdk_workspaces_web.types.log_file_format.LogFileFormat"
    """<p>The format of the LogFile that is written to S3.</p>"""
    folder_structure: "aws_sdk_workspaces_web.types.folder_structure.FolderStructure"
    """<p>The folder structure that defines the organizational structure for log files in S3.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3LogConfiguration) -> dict:
    out: dict = {}
    out["bucket"] = value["bucket"]
    if "key_prefix" in value:
        out["keyPrefix"] = value["key_prefix"]
    if "bucket_owner" in value:
        out["bucketOwner"] = value["bucket_owner"]
    import aws_sdk_workspaces_web.types.log_file_format

    out["logFileFormat"] = aws_sdk_workspaces_web.types.log_file_format.serialize_json(
        value["log_file_format"]
    )
    import aws_sdk_workspaces_web.types.folder_structure

    out["folderStructure"] = (
        aws_sdk_workspaces_web.types.folder_structure.serialize_json(
            value["folder_structure"]
        )
    )
    return out


def deserialize_json(data: dict) -> S3LogConfiguration:
    out: S3LogConfiguration = {}  # type: ignore[typeddict-item]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("S3LogConfiguration.bucket required")
    if "keyPrefix" in data:
        out["key_prefix"] = data["keyPrefix"]
    if "bucketOwner" in data:
        out["bucket_owner"] = data["bucketOwner"]
    if "logFileFormat" in data:
        import aws_sdk_workspaces_web.types.log_file_format

        out["log_file_format"] = (
            aws_sdk_workspaces_web.types.log_file_format.deserialize_json(
                data["logFileFormat"]
            )
        )
    else:
        raise DeserializationError("S3LogConfiguration.log_file_format required")
    if "folderStructure" in data:
        import aws_sdk_workspaces_web.types.folder_structure

        out["folder_structure"] = (
            aws_sdk_workspaces_web.types.folder_structure.deserialize_json(
                data["folderStructure"]
            )
        )
    else:
        raise DeserializationError("S3LogConfiguration.folder_structure required")
    return out
