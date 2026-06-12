"""Generated from Smithy shape ``com.amazonaws.batch#S3FilesVolumeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_batch.types.integer
    import aws_sdk_batch.types.string


class S3FilesVolumeConfiguration(TypedDict):
    file_system_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the S3Files file system to use.</p>"""
    root_directory: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The directory within the S3Files file system to mount as the root directory.</p>"""
    transit_encryption_port: NotRequired["aws_sdk_batch.types.integer.Integer"]
    """<p>The port to use when sending encrypted data between the Amazon ECS host and the S3Files file system server.</p>"""
    access_point_arn: NotRequired["aws_sdk_batch.types.string.String"]
    """<p>The Amazon Resource Name (ARN) of the S3Files access point to use.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: S3FilesVolumeConfiguration) -> dict:
    out: dict = {}
    if "file_system_arn" in value:
        out["fileSystemArn"] = value["file_system_arn"]
    if "root_directory" in value:
        out["rootDirectory"] = value["root_directory"]
    if "transit_encryption_port" in value:
        out["transitEncryptionPort"] = value["transit_encryption_port"]
    if "access_point_arn" in value:
        out["accessPointArn"] = value["access_point_arn"]
    return out


def deserialize_json(data: dict) -> S3FilesVolumeConfiguration:
    out: S3FilesVolumeConfiguration = {}  # type: ignore[typeddict-item]
    if "fileSystemArn" in data:
        out["file_system_arn"] = data["fileSystemArn"]
    if "rootDirectory" in data:
        out["root_directory"] = data["rootDirectory"]
    if "transitEncryptionPort" in data:
        out["transit_encryption_port"] = data["transitEncryptionPort"]
    if "accessPointArn" in data:
        out["access_point_arn"] = data["accessPointArn"]
    return out
