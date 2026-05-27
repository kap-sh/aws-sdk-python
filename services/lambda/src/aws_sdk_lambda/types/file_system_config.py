"""Generated from Smithy shape ``com.amazonaws.lambda#FileSystemConfig``."""

from typing import TYPE_CHECKING, TypedDict
from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.file_system_arn
    import aws_sdk_lambda.types.local_mount_path


class FileSystemConfig(TypedDict):
    arn: "aws_sdk_lambda.types.file_system_arn.FileSystemArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon EFS or Amazon S3 Files access point that provides access to the file system.</p>"""
    local_mount_path: "aws_sdk_lambda.types.local_mount_path.LocalMountPath"
    """<p>The path where the function can access the file system, starting with <code>/mnt/</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileSystemConfig) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    out["LocalMountPath"] = value["local_mount_path"]
    return out


def deserialize_json(data: dict) -> FileSystemConfig:
    out: FileSystemConfig = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("FileSystemConfig.arn required")
    if "LocalMountPath" in data:
        out["local_mount_path"] = data["LocalMountPath"]
    else:
        raise DeserializationError("FileSystemConfig.local_mount_path required")
    return out
