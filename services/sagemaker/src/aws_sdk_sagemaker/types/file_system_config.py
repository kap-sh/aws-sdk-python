"""Generated from Smithy shape ``com.amazonaws.sagemaker#FileSystemConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.default_gid
    import aws_sdk_sagemaker.types.default_uid
    import aws_sdk_sagemaker.types.mount_path


class FileSystemConfig(TypedDict):
    mount_path: NotRequired["aws_sdk_sagemaker.types.mount_path.MountPath"]
    """<p>The path within the image to mount the user's EFS home directory. The directory should be empty. If not specified, defaults to <i>/home/sagemaker-user</i>.</p>"""
    default_uid: NotRequired["aws_sdk_sagemaker.types.default_uid.DefaultUid"]
    """<p>The default POSIX user ID (UID). If not specified, defaults to <code>1000</code>.</p>"""
    default_gid: NotRequired["aws_sdk_sagemaker.types.default_gid.DefaultGid"]
    """<p>The default POSIX group ID (GID). If not specified, defaults to <code>100</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileSystemConfig) -> dict:
    out: dict = {}
    if "mount_path" in value:
        out["MountPath"] = value["mount_path"]
    if "default_uid" in value:
        out["DefaultUid"] = value["default_uid"]
    if "default_gid" in value:
        out["DefaultGid"] = value["default_gid"]
    return out


def deserialize_aws_json_1_1(data: dict) -> FileSystemConfig:
    out: FileSystemConfig = {}  # type: ignore[typeddict-item]
    if "MountPath" in data:
        out["mount_path"] = data["MountPath"]
    if "DefaultUid" in data:
        out["default_uid"] = data["DefaultUid"]
    if "DefaultGid" in data:
        out["default_gid"] = data["DefaultGid"]
    return out
