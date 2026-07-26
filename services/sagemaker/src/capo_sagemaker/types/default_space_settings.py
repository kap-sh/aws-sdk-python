"""Generated from Smithy shape ``com.amazonaws.sagemaker#DefaultSpaceSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.custom_file_system_configs
    import capo_sagemaker.types.custom_posix_user_config
    import capo_sagemaker.types.default_space_storage_settings
    import capo_sagemaker.types.jupyter_lab_app_settings
    import capo_sagemaker.types.jupyter_server_app_settings
    import capo_sagemaker.types.kernel_gateway_app_settings
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.security_group_ids


class DefaultSpaceSettings(TypedDict, closed=True):
    execution_role: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the execution role for the space.</p>"""
    security_groups: NotRequired[
        "capo_sagemaker.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security group IDs for the Amazon VPC that the space uses for communication.</p>"""
    jupyter_server_app_settings: NotRequired[
        "capo_sagemaker.types.jupyter_server_app_settings.JupyterServerAppSettings"
    ]
    kernel_gateway_app_settings: NotRequired[
        "capo_sagemaker.types.kernel_gateway_app_settings.KernelGatewayAppSettings"
    ]
    jupyter_lab_app_settings: NotRequired[
        "capo_sagemaker.types.jupyter_lab_app_settings.JupyterLabAppSettings"
    ]
    space_storage_settings: NotRequired[
        "capo_sagemaker.types.default_space_storage_settings.DefaultSpaceStorageSettings"
    ]
    custom_posix_user_config: NotRequired[
        "capo_sagemaker.types.custom_posix_user_config.CustomPosixUserConfig"
    ]
    custom_file_system_configs: NotRequired[
        "capo_sagemaker.types.custom_file_system_configs.CustomFileSystemConfigs"
    ]
    """<p>The settings for assigning a custom file system to a domain. Permitted users can access this file system in Amazon SageMaker AI Studio.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DefaultSpaceSettings) -> dict:
    out: dict = {}
    if "execution_role" in value:
        out["ExecutionRole"] = value["execution_role"]
    if "security_groups" in value:
        import capo_sagemaker.types.security_group_ids

        out["SecurityGroups"] = (
            capo_sagemaker.types.security_group_ids.serialize_aws_json_1_1(
                value["security_groups"]
            )
        )
    if "jupyter_server_app_settings" in value:
        import capo_sagemaker.types.jupyter_server_app_settings

        out["JupyterServerAppSettings"] = (
            capo_sagemaker.types.jupyter_server_app_settings.serialize_aws_json_1_1(
                value["jupyter_server_app_settings"]
            )
        )
    if "kernel_gateway_app_settings" in value:
        import capo_sagemaker.types.kernel_gateway_app_settings

        out["KernelGatewayAppSettings"] = (
            capo_sagemaker.types.kernel_gateway_app_settings.serialize_aws_json_1_1(
                value["kernel_gateway_app_settings"]
            )
        )
    if "jupyter_lab_app_settings" in value:
        import capo_sagemaker.types.jupyter_lab_app_settings

        out["JupyterLabAppSettings"] = (
            capo_sagemaker.types.jupyter_lab_app_settings.serialize_aws_json_1_1(
                value["jupyter_lab_app_settings"]
            )
        )
    if "space_storage_settings" in value:
        import capo_sagemaker.types.default_space_storage_settings

        out["SpaceStorageSettings"] = (
            capo_sagemaker.types.default_space_storage_settings.serialize_aws_json_1_1(
                value["space_storage_settings"]
            )
        )
    if "custom_posix_user_config" in value:
        import capo_sagemaker.types.custom_posix_user_config

        out["CustomPosixUserConfig"] = (
            capo_sagemaker.types.custom_posix_user_config.serialize_aws_json_1_1(
                value["custom_posix_user_config"]
            )
        )
    if "custom_file_system_configs" in value:
        import capo_sagemaker.types.custom_file_system_configs

        out["CustomFileSystemConfigs"] = (
            capo_sagemaker.types.custom_file_system_configs.serialize_aws_json_1_1(
                value["custom_file_system_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DefaultSpaceSettings:
    out: DefaultSpaceSettings = {}  # type: ignore[typeddict-item]
    if "ExecutionRole" in data:
        out["execution_role"] = data["ExecutionRole"]
    if "SecurityGroups" in data:
        import capo_sagemaker.types.security_group_ids

        out["security_groups"] = (
            capo_sagemaker.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroups"]
            )
        )
    if "JupyterServerAppSettings" in data:
        import capo_sagemaker.types.jupyter_server_app_settings

        out["jupyter_server_app_settings"] = (
            capo_sagemaker.types.jupyter_server_app_settings.deserialize_aws_json_1_1(
                data["JupyterServerAppSettings"]
            )
        )
    if "KernelGatewayAppSettings" in data:
        import capo_sagemaker.types.kernel_gateway_app_settings

        out["kernel_gateway_app_settings"] = (
            capo_sagemaker.types.kernel_gateway_app_settings.deserialize_aws_json_1_1(
                data["KernelGatewayAppSettings"]
            )
        )
    if "JupyterLabAppSettings" in data:
        import capo_sagemaker.types.jupyter_lab_app_settings

        out["jupyter_lab_app_settings"] = (
            capo_sagemaker.types.jupyter_lab_app_settings.deserialize_aws_json_1_1(
                data["JupyterLabAppSettings"]
            )
        )
    if "SpaceStorageSettings" in data:
        import capo_sagemaker.types.default_space_storage_settings

        out["space_storage_settings"] = (
            capo_sagemaker.types.default_space_storage_settings.deserialize_aws_json_1_1(
                data["SpaceStorageSettings"]
            )
        )
    if "CustomPosixUserConfig" in data:
        import capo_sagemaker.types.custom_posix_user_config

        out["custom_posix_user_config"] = (
            capo_sagemaker.types.custom_posix_user_config.deserialize_aws_json_1_1(
                data["CustomPosixUserConfig"]
            )
        )
    if "CustomFileSystemConfigs" in data:
        import capo_sagemaker.types.custom_file_system_configs

        out["custom_file_system_configs"] = (
            capo_sagemaker.types.custom_file_system_configs.deserialize_aws_json_1_1(
                data["CustomFileSystemConfigs"]
            )
        )
    return out
