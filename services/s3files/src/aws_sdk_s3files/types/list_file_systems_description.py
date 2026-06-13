"""Generated from Smithy shape ``com.amazonaws.s3files#ListFileSystemsDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_s3files.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_s3files.types.aws_account_id
    import aws_sdk_s3files.types.bucket_arn
    import aws_sdk_s3files.types.file_system_arn
    import aws_sdk_s3files.types.file_system_id
    import aws_sdk_s3files.types.life_cycle_state
    import aws_sdk_s3files.types.role_arn
    import aws_sdk_s3files.types.status_message
    import aws_sdk_s3files.types.tag_value


class ListFileSystemsDescription(TypedDict):
    creation_time: "datetime.datetime"
    """<p>The time when the file system was created.</p>"""
    file_system_arn: "aws_sdk_s3files.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the file system.</p>"""
    file_system_id: "aws_sdk_s3files.types.file_system_id.FileSystemId"
    """<p>The ID of the file system.</p>"""
    name: NotRequired["aws_sdk_s3files.types.tag_value.TagValue"]
    """<p>The name of the file system.</p>"""
    bucket: "aws_sdk_s3files.types.bucket_arn.BucketArn"
    """<p>The Amazon Resource Name (ARN) of the S3 bucket.</p>"""
    status: "aws_sdk_s3files.types.life_cycle_state.LifeCycleState"
    """<p>The current status of the file system.</p>"""
    status_message: NotRequired["aws_sdk_s3files.types.status_message.StatusMessage"]
    """<p>Additional information about the file system status.</p>"""
    role_arn: "aws_sdk_s3files.types.role_arn.RoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role used for S3 access.</p>"""
    owner_id: "aws_sdk_s3files.types.aws_account_id.AwsAccountId"
    """<p>The Amazon Web Services account ID of the file system owner.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFileSystemsDescription) -> dict:
    out: dict = {}
    import aws_sdk_s3files.types._prelude.timestamp

    out["creationTime"] = aws_sdk_s3files.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    out["fileSystemArn"] = value["file_system_arn"]
    out["fileSystemId"] = value["file_system_id"]
    if "name" in value:
        out["name"] = value["name"]
    out["bucket"] = value["bucket"]
    import aws_sdk_s3files.types.life_cycle_state

    out["status"] = aws_sdk_s3files.types.life_cycle_state.serialize_json(
        value["status"]
    )
    if "status_message" in value:
        out["statusMessage"] = value["status_message"]
    out["roleArn"] = value["role_arn"]
    out["ownerId"] = value["owner_id"]
    return out


def deserialize_json(data: dict) -> ListFileSystemsDescription:
    out: ListFileSystemsDescription = {}  # type: ignore[typeddict-item]
    if "creationTime" in data:
        import aws_sdk_s3files.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_s3files.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("ListFileSystemsDescription.creation_time required")
    if "fileSystemArn" in data:
        out["file_system_arn"] = data["fileSystemArn"]
    else:
        raise DeserializationError(
            "ListFileSystemsDescription.file_system_arn required"
        )
    if "fileSystemId" in data:
        out["file_system_id"] = data["fileSystemId"]
    else:
        raise DeserializationError("ListFileSystemsDescription.file_system_id required")
    if "name" in data:
        out["name"] = data["name"]
    if "bucket" in data:
        out["bucket"] = data["bucket"]
    else:
        raise DeserializationError("ListFileSystemsDescription.bucket required")
    if "status" in data:
        import aws_sdk_s3files.types.life_cycle_state

        out["status"] = aws_sdk_s3files.types.life_cycle_state.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ListFileSystemsDescription.status required")
    if "statusMessage" in data:
        out["status_message"] = data["statusMessage"]
    if "roleArn" in data:
        out["role_arn"] = data["roleArn"]
    else:
        raise DeserializationError("ListFileSystemsDescription.role_arn required")
    if "ownerId" in data:
        out["owner_id"] = data["ownerId"]
    else:
        raise DeserializationError("ListFileSystemsDescription.owner_id required")
    return out
