"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#FilesystemConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.efs_access_point_configuration
    import aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_configuration
    import aws_sdk_bedrock_agentcore_control.types.session_storage_configuration


class _FilesystemConfiguration_sessionStorage(TypedDict):
    sessionStorage: "aws_sdk_bedrock_agentcore_control.types.session_storage_configuration.SessionStorageConfiguration"


class _FilesystemConfiguration_s3FilesAccessPoint(TypedDict):
    s3FilesAccessPoint: "aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_configuration.S3FilesAccessPointConfiguration"


class _FilesystemConfiguration_efsAccessPoint(TypedDict):
    efsAccessPoint: "aws_sdk_bedrock_agentcore_control.types.efs_access_point_configuration.EfsAccessPointConfiguration"


FilesystemConfiguration: TypeAlias = (
    _FilesystemConfiguration_sessionStorage
    | _FilesystemConfiguration_s3FilesAccessPoint
    | _FilesystemConfiguration_efsAccessPoint
)


# --- restJson1 ser/de ---
def serialize_json(value: FilesystemConfiguration) -> dict:
    if "sessionStorage" in value:
        import aws_sdk_bedrock_agentcore_control.types.session_storage_configuration

        return {
            "sessionStorage": aws_sdk_bedrock_agentcore_control.types.session_storage_configuration.serialize_json(
                value["sessionStorage"]
            )
        }
    elif "s3FilesAccessPoint" in value:
        import aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_configuration

        return {
            "s3FilesAccessPoint": aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_configuration.serialize_json(
                value["s3FilesAccessPoint"]
            )
        }
    elif "efsAccessPoint" in value:
        import aws_sdk_bedrock_agentcore_control.types.efs_access_point_configuration

        return {
            "efsAccessPoint": aws_sdk_bedrock_agentcore_control.types.efs_access_point_configuration.serialize_json(
                value["efsAccessPoint"]
            )
        }
    else:
        raise SerializationError("FilesystemConfiguration: no variant present")


def deserialize_json(data: dict) -> FilesystemConfiguration:
    if "sessionStorage" in data:
        import aws_sdk_bedrock_agentcore_control.types.session_storage_configuration

        return {
            "sessionStorage": aws_sdk_bedrock_agentcore_control.types.session_storage_configuration.deserialize_json(
                data["sessionStorage"]
            )
        }
    elif "s3FilesAccessPoint" in data:
        import aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_configuration

        return {
            "s3FilesAccessPoint": aws_sdk_bedrock_agentcore_control.types.s3_files_access_point_configuration.deserialize_json(
                data["s3FilesAccessPoint"]
            )
        }
    elif "efsAccessPoint" in data:
        import aws_sdk_bedrock_agentcore_control.types.efs_access_point_configuration

        return {
            "efsAccessPoint": aws_sdk_bedrock_agentcore_control.types.efs_access_point_configuration.deserialize_json(
                data["efsAccessPoint"]
            )
        }
    else:
        raise DeserializationError("FilesystemConfiguration: no recognized variant key")
