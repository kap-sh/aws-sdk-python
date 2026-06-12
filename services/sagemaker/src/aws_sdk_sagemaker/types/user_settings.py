"""Generated from Smithy shape ``com.amazonaws.sagemaker#UserSettings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.auto_mount_home_efs
    import aws_sdk_sagemaker.types.canvas_app_settings
    import aws_sdk_sagemaker.types.code_editor_app_settings
    import aws_sdk_sagemaker.types.custom_file_system_configs
    import aws_sdk_sagemaker.types.custom_posix_user_config
    import aws_sdk_sagemaker.types.default_space_storage_settings
    import aws_sdk_sagemaker.types.jupyter_lab_app_settings
    import aws_sdk_sagemaker.types.jupyter_server_app_settings
    import aws_sdk_sagemaker.types.kernel_gateway_app_settings
    import aws_sdk_sagemaker.types.landing_uri
    import aws_sdk_sagemaker.types.r_session_app_settings
    import aws_sdk_sagemaker.types.r_studio_server_pro_app_settings
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.security_group_ids
    import aws_sdk_sagemaker.types.sharing_settings
    import aws_sdk_sagemaker.types.studio_web_portal
    import aws_sdk_sagemaker.types.studio_web_portal_settings
    import aws_sdk_sagemaker.types.tensor_board_app_settings


class UserSettings(TypedDict):
    execution_role: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The execution role for the user.</p> <p>SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesn't apply this setting to shared spaces.</p>"""
    security_groups: NotRequired[
        "aws_sdk_sagemaker.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The security groups for the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.</p> <p>Optional when the <code>CreateDomain.AppNetworkAccessType</code> parameter is set to <code>PublicInternetOnly</code>.</p> <p>Required when the <code>CreateDomain.AppNetworkAccessType</code> parameter is set to <code>VpcOnly</code>, unless specified as part of the <code>DefaultUserSettings</code> for the domain.</p> <p>Amazon SageMaker AI adds a security group to allow NFS traffic from Amazon SageMaker AI Studio. Therefore, the number of security groups that you can specify is one less than the maximum number shown.</p> <p>SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.</p>"""
    sharing_settings: NotRequired[
        "aws_sdk_sagemaker.types.sharing_settings.SharingSettings"
    ]
    """<p>Specifies options for sharing Amazon SageMaker AI Studio notebooks.</p>"""
    jupyter_server_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.jupyter_server_app_settings.JupyterServerAppSettings"
    ]
    """<p>The Jupyter server's app settings.</p>"""
    kernel_gateway_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.kernel_gateway_app_settings.KernelGatewayAppSettings"
    ]
    """<p>The kernel gateway app settings.</p>"""
    tensor_board_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.tensor_board_app_settings.TensorBoardAppSettings"
    ]
    """<p>The TensorBoard app settings.</p>"""
    r_studio_server_pro_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.r_studio_server_pro_app_settings.RStudioServerProAppSettings"
    ]
    """<p>A collection of settings that configure user interaction with the <code>RStudioServerPro</code> app.</p>"""
    r_session_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.r_session_app_settings.RSessionAppSettings"
    ]
    """<p>A collection of settings that configure the <code>RSessionGateway</code> app.</p>"""
    canvas_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.canvas_app_settings.CanvasAppSettings"
    ]
    """<p>The Canvas app settings.</p> <p>SageMaker applies these settings only to private spaces that SageMaker creates for the Canvas app.</p>"""
    code_editor_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.code_editor_app_settings.CodeEditorAppSettings"
    ]
    """<p>The Code Editor application settings.</p> <p>SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.</p>"""
    jupyter_lab_app_settings: NotRequired[
        "aws_sdk_sagemaker.types.jupyter_lab_app_settings.JupyterLabAppSettings"
    ]
    """<p>The settings for the JupyterLab application.</p> <p>SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.</p>"""
    space_storage_settings: NotRequired[
        "aws_sdk_sagemaker.types.default_space_storage_settings.DefaultSpaceStorageSettings"
    ]
    """<p>The storage settings for a space.</p> <p>SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.</p>"""
    default_landing_uri: NotRequired["aws_sdk_sagemaker.types.landing_uri.LandingUri"]
    """<p>The default experience that the user is directed to when accessing the domain. The supported values are:</p> <ul> <li> <p> <code>studio::</code>: Indicates that Studio is the default experience. This value can only be passed if <code>StudioWebPortal</code> is set to <code>ENABLED</code>.</p> </li> <li> <p> <code>app:JupyterServer:</code>: Indicates that Studio Classic is the default experience.</p> </li> </ul>"""
    studio_web_portal: NotRequired[
        "aws_sdk_sagemaker.types.studio_web_portal.StudioWebPortal"
    ]
    """<p>Whether the user can access Studio. If this value is set to <code>DISABLED</code>, the user cannot access Studio, even if that is the default experience for the domain.</p>"""
    custom_posix_user_config: NotRequired[
        "aws_sdk_sagemaker.types.custom_posix_user_config.CustomPosixUserConfig"
    ]
    """<p>Details about the POSIX identity that is used for file system operations.</p> <p>SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.</p>"""
    custom_file_system_configs: NotRequired[
        "aws_sdk_sagemaker.types.custom_file_system_configs.CustomFileSystemConfigs"
    ]
    """<p>The settings for assigning a custom file system to a user profile. Permitted users can access this file system in Amazon SageMaker AI Studio.</p> <p>SageMaker applies these settings only to private spaces that the user creates in the domain. SageMaker doesn't apply these settings to shared spaces.</p>"""
    studio_web_portal_settings: NotRequired[
        "aws_sdk_sagemaker.types.studio_web_portal_settings.StudioWebPortalSettings"
    ]
    """<p>Studio settings. If these settings are applied on a user level, they take priority over the settings applied on a domain level.</p>"""
    auto_mount_home_efs: NotRequired[
        "aws_sdk_sagemaker.types.auto_mount_home_efs.AutoMountHomeEFS"
    ]
    """<p>Indicates whether auto-mounting of an EFS volume is supported for the user profile. The <code>DefaultAsDomain</code> value is only supported for user profiles. Do not use the <code>DefaultAsDomain</code> value when setting this parameter for a domain.</p> <p>SageMaker applies this setting only to private spaces that the user creates in the domain. SageMaker doesn't apply this setting to shared spaces.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UserSettings) -> dict:
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
    if "sharing_settings" in value:
        import aws_sdk_sagemaker.types.sharing_settings

        out["SharingSettings"] = (
            aws_sdk_sagemaker.types.sharing_settings.serialize_aws_json_1_1(
                value["sharing_settings"]
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
    if "tensor_board_app_settings" in value:
        import aws_sdk_sagemaker.types.tensor_board_app_settings

        out["TensorBoardAppSettings"] = (
            aws_sdk_sagemaker.types.tensor_board_app_settings.serialize_aws_json_1_1(
                value["tensor_board_app_settings"]
            )
        )
    if "r_studio_server_pro_app_settings" in value:
        import aws_sdk_sagemaker.types.r_studio_server_pro_app_settings

        out["RStudioServerProAppSettings"] = (
            aws_sdk_sagemaker.types.r_studio_server_pro_app_settings.serialize_aws_json_1_1(
                value["r_studio_server_pro_app_settings"]
            )
        )
    if "r_session_app_settings" in value:
        import aws_sdk_sagemaker.types.r_session_app_settings

        out["RSessionAppSettings"] = (
            aws_sdk_sagemaker.types.r_session_app_settings.serialize_aws_json_1_1(
                value["r_session_app_settings"]
            )
        )
    if "canvas_app_settings" in value:
        import aws_sdk_sagemaker.types.canvas_app_settings

        out["CanvasAppSettings"] = (
            aws_sdk_sagemaker.types.canvas_app_settings.serialize_aws_json_1_1(
                value["canvas_app_settings"]
            )
        )
    if "code_editor_app_settings" in value:
        import aws_sdk_sagemaker.types.code_editor_app_settings

        out["CodeEditorAppSettings"] = (
            aws_sdk_sagemaker.types.code_editor_app_settings.serialize_aws_json_1_1(
                value["code_editor_app_settings"]
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
    if "default_landing_uri" in value:
        out["DefaultLandingUri"] = value["default_landing_uri"]
    if "studio_web_portal" in value:
        import aws_sdk_sagemaker.types.studio_web_portal

        out["StudioWebPortal"] = (
            aws_sdk_sagemaker.types.studio_web_portal.serialize_aws_json_1_1(
                value["studio_web_portal"]
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
    if "studio_web_portal_settings" in value:
        import aws_sdk_sagemaker.types.studio_web_portal_settings

        out["StudioWebPortalSettings"] = (
            aws_sdk_sagemaker.types.studio_web_portal_settings.serialize_aws_json_1_1(
                value["studio_web_portal_settings"]
            )
        )
    if "auto_mount_home_efs" in value:
        import aws_sdk_sagemaker.types.auto_mount_home_efs

        out["AutoMountHomeEFS"] = (
            aws_sdk_sagemaker.types.auto_mount_home_efs.serialize_aws_json_1_1(
                value["auto_mount_home_efs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UserSettings:
    out: UserSettings = {}  # type: ignore[typeddict-item]
    if "ExecutionRole" in data:
        out["execution_role"] = data["ExecutionRole"]
    if "SecurityGroups" in data:
        import aws_sdk_sagemaker.types.security_group_ids

        out["security_groups"] = (
            aws_sdk_sagemaker.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroups"]
            )
        )
    if "SharingSettings" in data:
        import aws_sdk_sagemaker.types.sharing_settings

        out["sharing_settings"] = (
            aws_sdk_sagemaker.types.sharing_settings.deserialize_aws_json_1_1(
                data["SharingSettings"]
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
    if "TensorBoardAppSettings" in data:
        import aws_sdk_sagemaker.types.tensor_board_app_settings

        out["tensor_board_app_settings"] = (
            aws_sdk_sagemaker.types.tensor_board_app_settings.deserialize_aws_json_1_1(
                data["TensorBoardAppSettings"]
            )
        )
    if "RStudioServerProAppSettings" in data:
        import aws_sdk_sagemaker.types.r_studio_server_pro_app_settings

        out["r_studio_server_pro_app_settings"] = (
            aws_sdk_sagemaker.types.r_studio_server_pro_app_settings.deserialize_aws_json_1_1(
                data["RStudioServerProAppSettings"]
            )
        )
    if "RSessionAppSettings" in data:
        import aws_sdk_sagemaker.types.r_session_app_settings

        out["r_session_app_settings"] = (
            aws_sdk_sagemaker.types.r_session_app_settings.deserialize_aws_json_1_1(
                data["RSessionAppSettings"]
            )
        )
    if "CanvasAppSettings" in data:
        import aws_sdk_sagemaker.types.canvas_app_settings

        out["canvas_app_settings"] = (
            aws_sdk_sagemaker.types.canvas_app_settings.deserialize_aws_json_1_1(
                data["CanvasAppSettings"]
            )
        )
    if "CodeEditorAppSettings" in data:
        import aws_sdk_sagemaker.types.code_editor_app_settings

        out["code_editor_app_settings"] = (
            aws_sdk_sagemaker.types.code_editor_app_settings.deserialize_aws_json_1_1(
                data["CodeEditorAppSettings"]
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
    if "DefaultLandingUri" in data:
        out["default_landing_uri"] = data["DefaultLandingUri"]
    if "StudioWebPortal" in data:
        import aws_sdk_sagemaker.types.studio_web_portal

        out["studio_web_portal"] = (
            aws_sdk_sagemaker.types.studio_web_portal.deserialize_aws_json_1_1(
                data["StudioWebPortal"]
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
    if "StudioWebPortalSettings" in data:
        import aws_sdk_sagemaker.types.studio_web_portal_settings

        out["studio_web_portal_settings"] = (
            aws_sdk_sagemaker.types.studio_web_portal_settings.deserialize_aws_json_1_1(
                data["StudioWebPortalSettings"]
            )
        )
    if "AutoMountHomeEFS" in data:
        import aws_sdk_sagemaker.types.auto_mount_home_efs

        out["auto_mount_home_efs"] = (
            aws_sdk_sagemaker.types.auto_mount_home_efs.deserialize_aws_json_1_1(
                data["AutoMountHomeEFS"]
            )
        )
    return out
