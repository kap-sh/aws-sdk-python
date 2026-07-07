"""Generated from Smithy shape ``com.amazonaws.sagemaker#CustomFileSystem``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_sagemaker.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.efs_file_system
    import aws_sdk_sagemaker.types.f_sx_lustre_file_system
    import aws_sdk_sagemaker.types.s3_file_system


class _CustomFileSystem_EFSFileSystem(TypedDict, closed=True):
    EFSFileSystem: "aws_sdk_sagemaker.types.efs_file_system.EFSFileSystem"


class _CustomFileSystem_FSxLustreFileSystem(TypedDict, closed=True):
    FSxLustreFileSystem: (
        "aws_sdk_sagemaker.types.f_sx_lustre_file_system.FSxLustreFileSystem"
    )


class _CustomFileSystem_S3FileSystem(TypedDict, closed=True):
    S3FileSystem: "aws_sdk_sagemaker.types.s3_file_system.S3FileSystem"


CustomFileSystem: TypeAlias = (
    _CustomFileSystem_EFSFileSystem
    | _CustomFileSystem_FSxLustreFileSystem
    | _CustomFileSystem_S3FileSystem
)


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomFileSystem) -> dict:
    if "EFSFileSystem" in value:
        import aws_sdk_sagemaker.types.efs_file_system

        return {
            "EFSFileSystem": aws_sdk_sagemaker.types.efs_file_system.serialize_aws_json_1_1(
                value["EFSFileSystem"]
            )
        }
    elif "FSxLustreFileSystem" in value:
        import aws_sdk_sagemaker.types.f_sx_lustre_file_system

        return {
            "FSxLustreFileSystem": aws_sdk_sagemaker.types.f_sx_lustre_file_system.serialize_aws_json_1_1(
                value["FSxLustreFileSystem"]
            )
        }
    elif "S3FileSystem" in value:
        import aws_sdk_sagemaker.types.s3_file_system

        return {
            "S3FileSystem": aws_sdk_sagemaker.types.s3_file_system.serialize_aws_json_1_1(
                value["S3FileSystem"]
            )
        }
    else:
        raise SerializationError("CustomFileSystem: no variant present")


def deserialize_aws_json_1_1(data: dict) -> CustomFileSystem:
    if "EFSFileSystem" in data:
        import aws_sdk_sagemaker.types.efs_file_system

        return {
            "EFSFileSystem": aws_sdk_sagemaker.types.efs_file_system.deserialize_aws_json_1_1(
                data["EFSFileSystem"]
            )
        }
    elif "FSxLustreFileSystem" in data:
        import aws_sdk_sagemaker.types.f_sx_lustre_file_system

        return {
            "FSxLustreFileSystem": aws_sdk_sagemaker.types.f_sx_lustre_file_system.deserialize_aws_json_1_1(
                data["FSxLustreFileSystem"]
            )
        }
    elif "S3FileSystem" in data:
        import aws_sdk_sagemaker.types.s3_file_system

        return {
            "S3FileSystem": aws_sdk_sagemaker.types.s3_file_system.deserialize_aws_json_1_1(
                data["S3FileSystem"]
            )
        }
    else:
        raise DeserializationError("CustomFileSystem: no recognized variant key")
