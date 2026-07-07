"""Generated from Smithy shape ``com.amazonaws.sagemaker#S3FileSystemConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.s3_schema_uri
    import aws_sdk_sagemaker.types.string1024


class S3FileSystemConfig(TypedDict, closed=True):
    mount_path: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p>The file system path where the Amazon S3 storage location will be mounted within the Amazon SageMaker Studio environment.</p>"""
    s3_uri: NotRequired["aws_sdk_sagemaker.types.s3_schema_uri.S3SchemaUri"]
    """<p>The Amazon S3 URI of the S3 file system configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: S3FileSystemConfig) -> dict:
    out: dict = {}
    if "mount_path" in value:
        out["MountPath"] = value["mount_path"]
    if "s3_uri" in value:
        out["S3Uri"] = value["s3_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> S3FileSystemConfig:
    out: S3FileSystemConfig = {}  # type: ignore[typeddict-item]
    if "MountPath" in data:
        out["mount_path"] = data["MountPath"]
    if "S3Uri" in data:
        out["s3_uri"] = data["S3Uri"]
    return out
