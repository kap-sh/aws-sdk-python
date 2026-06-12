"""Generated from Smithy shape ``com.amazonaws.sagemaker#DefaultSpaceSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.custom_file_system_configs
    import aws_sdk_sagemaker.types.custom_posix_user_config
    import aws_sdk_sagemaker.types.default_space_storage_settings
    import aws_sdk_sagemaker.types.jupyter_lab_app_settings
    import aws_sdk_sagemaker.types.jupyter_server_app_settings
    import aws_sdk_sagemaker.types.kernel_gateway_app_settings
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.security_group_ids


class DefaultSpaceSettings(TypedDict):
    execution_role: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role for the space.</p>"""
    security_groups: NotRequired[
        "aws_sdk_sagemaker.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security group IDs for the Amazon VPC that the space uses for communication.</p>"""
    jupyter_server_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.jupyter_server_app_settings.JupyterServerAppSettings"
    ]
    kernel_gateway_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.kernel_gateway_app_settings.KernelGatewayAppSettings"
    ]
    jupyter_lab_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.jupyter_lab_app_settings.JupyterLabAppSettings"
    ]
    space_storage_settings: NotRequired[
        "aws_sdk_sagemaker.types.default_space_storage_settings.DefaultSpaceStorageSettings"
    ]
    custom_posix_user_config: NotRequired[
        "aws_sdk_sagemaker.types.custom_posix_user_config.CustomPosixUserConfig"
    ]
    custom_file_system_configs: NotRequired[
        "aws_sdk_sagemaker.types.custom_file_system_configs.CustomFileSystemConfigs"
    ]
    """<p>The settings for assigning a custom file system to a domain. Permitted users can access this file system in Amazon SageMaker AI Studio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultSpaceSettings) -> dict:
    out: dict = {}
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "security_groups" in value:
        import aws_sdk_sagemaker.types.security_group_ids

        out["SecurityGroups"] = (
            aws_sdk_sagemaker.types.security_group_ids.serialize_aws_json_1_1(
                value["security_groups"]
            )
        )
    if "jupyter_server_app_settings" in value:
        import aws_sdk_sagemaker.types.jupyter_server_app_settings

        out["JupyterServerAppSettings"] = (
            aws_sdk_sagemaker.types.jupyter_server_app_settings.serialize_aws_json_1_1(
                value["jupyter_server_app_settings"]
            )
        )
    if "kernel_gateway_app_settings" in value:
        import aws_sdk_sagemaker.types.kernel_gateway_app_settings

        out["KernelGatewayAppSettings"] = (
            aws_sdk_sagemaker.types.kernel_gateway_app_settings.serialize_aws_json_1_1(
                value["kernel_gateway_app_settings"]
            )
        )
    if "jupyter_lab_app_settings" in value:
        import aws_sdk_sagemaker.types.jupyter_lab_app_settings

        out["JupyterLabAppSettings"] = (
            aws_sdk_sagemaker.types.jupyter_lab_app_settings.serialize_aws_json_1_1(
                value["jupyter_lab_app_settings"]
            )
        )
    if "space_storage_settings" in value:
        import aws_sdk_sagemaker.types.default_space_storage_settings

        out["SpaceStorageSettings"] = (
            aws_sdk_sagemaker.types.default_space_storage_settings.serialize_aws_json_1_1(
                value["space_storage_settings"]
            )
        )
    if "custom_posix_user_config" in value:
        import aws_sdk_sagemaker.types.custom_posix_user_config

        out["CustomPosixUserConfig"] = (
            aws_sdk_sagemaker.types.custom_posix_user_config.serialize_aws_json_1_1(
                value["custom_posix_user_config"]
            )
        )
    if "custom_file_system_configs" in value:
        import aws_sdk_sagemaker.types.custom_file_system_configs

        out["CustomFileSystemConfigs"] = (
            aws_sdk_sagemaker.types.custom_file_system_configs.serialize_aws_json_1_1(
                value["custom_file_system_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultSpaceSettings:
    out: DefaultSpaceSettings = {}  # type: ignore[typeddict-item]
    if "ExecutionRole" in data:
        out["execution_role"] = data["ExecutionRole"]
    if "SecurityGroups" in data:
        import aws_sdk_sagemaker.types.security_group_ids

        out["security_groups"] = (
            aws_sdk_sagemaker.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroups"]
            )
        )
    if "JupyterServerAppSettings" in data:
        import aws_sdk_sagemaker.types.jupyter_server_app_settings

        out["jupyter_server_app_settings"] = (
            aws_sdk_sagemaker.types.jupyter_server_app_settings.deserialize_aws_json_1_1(
                data["JupyterServerAppSettings"]
            )
        )
    if "KernelGatewayAppSettings" in data:
        import aws_sdk_sagemaker.types.kernel_gateway_app_settings

        out["kernel_gateway_app_settings"] = (
            aws_sdk_sagemaker.types.kernel_gateway_app_settings.deserialize_aws_json_1_1(
                data["KernelGatewayAppSettings"]
            )
        )
    if "JupyterLabAppSettings" in data:
        import aws_sdk_sagemaker.types.jupyter_lab_app_settings

        out["jupyter_lab_app_settings"] = (
            aws_sdk_sagemaker.types.jupyter_lab_app_settings.deserialize_aws_json_1_1(
                data["JupyterLabAppSettings"]
            )
        )
    if "SpaceStorageSettings" in data:
        import aws_sdk_sagemaker.types.default_space_storage_settings

        out["space_storage_settings"] = (
            aws_sdk_sagemaker.types.default_space_storage_settings.deserialize_aws_json_1_1(
                data["SpaceStorageSettings"]
            )
        )
    if "CustomPosixUserConfig" in data:
        import aws_sdk_sagemaker.types.custom_posix_user_config

        out["custom_posix_user_config"] = (
            aws_sdk_sagemaker.types.custom_posix_user_config.deserialize_aws_json_1_1(
                data["CustomPosixUserConfig"]
            )
        )
    if "CustomFileSystemConfigs" in data:
        import aws_sdk_sagemaker.types.custom_file_system_configs

        out["custom_file_system_configs"] = (
            aws_sdk_sagemaker.types.custom_file_system_configs.deserialize_aws_json_1_1(
                data["CustomFileSystemConfigs"]
            )
        )
    return out
