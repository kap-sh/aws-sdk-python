"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystemConfig``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.efs_file_system_config
    import aws_sdk_sagemaker.types.f_sx_lustre_file_system_config
    import aws_sdk_sagemaker.types.s3_file_system_config


class _CustomFileSystemConfig_EFSFileSystemConfig(TypedDict, closed=True):
    EFSFileSystemConfig: (
        "aws_sdk_sagemaker.types.efs_file_system_config.EFSFileSystemConfig"
    )


class _CustomFileSystemConfig_FSxLustreFileSystemConfig(TypedDict, closed=True):
    FSxLustreFileSystemConfig: "aws_sdk_sagemaker.types.f_sx_lustre_file_system_config.FSxLustreFileSystemConfig"


class _CustomFileSystemConfig_S3FileSystemConfig(TypedDict, closed=True):
    S3FileSystemConfig: (
        "aws_sdk_sagemaker.types.s3_file_system_config.S3FileSystemConfig"
    )


CustomFileSystemConfig: TypeAlias = (
    _CustomFileSystemConfig_EFSFileSystemConfig
    | _CustomFileSystemConfig_FSxLustreFileSystemConfig
    | _CustomFileSystemConfig_S3FileSystemConfig
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomFileSystemConfig) -> dict:
    if "EFSFileSystemConfig" in value:
        import aws_sdk_sagemaker.types.efs_file_system_config

        return {
            "EFSFileSystemConfig": aws_sdk_sagemaker.types.efs_file_system_config.serialize_aws_json_1_1(
                value["EFSFileSystemConfig"]
            )
        }
    elif "FSxLustreFileSystemConfig" in value:
        import aws_sdk_sagemaker.types.f_sx_lustre_file_system_config

        return {
            "FSxLustreFileSystemConfig": aws_sdk_sagemaker.types.f_sx_lustre_file_system_config.serialize_aws_json_1_1(
                value["FSxLustreFileSystemConfig"]
            )
        }
    elif "S3FileSystemConfig" in value:
        import aws_sdk_sagemaker.types.s3_file_system_config

        return {
            "S3FileSystemConfig": aws_sdk_sagemaker.types.s3_file_system_config.serialize_aws_json_1_1(
                value["S3FileSystemConfig"]
            )
        }
    else:
        raise SerializationError("CustomFileSystemConfig: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CustomFileSystemConfig:
    if "EFSFileSystemConfig" in data:
        import aws_sdk_sagemaker.types.efs_file_system_config

        return {
            "EFSFileSystemConfig": aws_sdk_sagemaker.types.efs_file_system_config.deserialize_aws_json_1_1(
                data["EFSFileSystemConfig"]
            )
        }
    elif "FSxLustreFileSystemConfig" in data:
        import aws_sdk_sagemaker.types.f_sx_lustre_file_system_config

        return {
            "FSxLustreFileSystemConfig": aws_sdk_sagemaker.types.f_sx_lustre_file_system_config.deserialize_aws_json_1_1(
                data["FSxLustreFileSystemConfig"]
            )
        }
    elif "S3FileSystemConfig" in data:
        import aws_sdk_sagemaker.types.s3_file_system_config

        return {
            "S3FileSystemConfig": aws_sdk_sagemaker.types.s3_file_system_config.deserialize_aws_json_1_1(
                data["S3FileSystemConfig"]
            )
        }
    else:
        raise DeserializationError("CustomFileSystemConfig: no recognized variant key")
