"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_network_access_type
    import capo_sagemaker.types.app_security_group_management
    import capo_sagemaker.types.default_space_settings
    import capo_sagemaker.types.domain_id
    import capo_sagemaker.types.domain_settings_for_update
    import capo_sagemaker.types.home_efs_file_system_creation
    import capo_sagemaker.types.subnets
    import capo_sagemaker.types.tag_propagation
    import capo_sagemaker.types.user_settings
    import capo_sagemaker.types.vpc_id


class UpdateDomainRequest(TypedDict, closed=True):
    domain_id: NotRequired["capo_sagemaker.types.domain_id.DomainId"]
    """<p>The ID of the domain to be updated.</p>"""
    default_user_settings: NotRequired[
        "capo_sagemaker.types.user_settings.UserSettings"
    ]
    """<p>A collection of settings.</p>"""
    domain_settings_for_update: NotRequired[
        "capo_sagemaker.types.domain_settings_for_update.DomainSettingsForUpdate"
    ]
    """<p>A collection of <code>DomainSettings</code> configuration values to update.</p>"""
    app_security_group_management: NotRequired[
        "capo_sagemaker.types.app_security_group_management.AppSecurityGroupManagement"
    ]
    """<p>The entity that creates and manages the required security groups for inter-app communication in <code>VPCOnly</code> mode. Required when <code>CreateDomain.AppNetworkAccessType</code> is <code>VPCOnly</code> and <code>DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn</code> is provided. If setting up the domain for use with RStudio, this value must be set to <code>Service</code>.</p>"""
    default_space_settings: NotRequired[
        "capo_sagemaker.types.default_space_settings.DefaultSpaceSettings"
    ]
    """<p>The default settings for shared spaces that users create in the domain.</p>"""
    subnet_ids: NotRequired["capo_sagemaker.types.subnets.Subnets"]
    """<p>The VPC subnets that Studio uses for communication.</p> <p>If removing subnets, ensure there are no apps in the <code>InService</code>, <code>Pending</code>, or <code>Deleting</code> state.</p>"""
    app_network_access_type: NotRequired[
        "capo_sagemaker.types.app_network_access_type.AppNetworkAccessType"
    ]
    """<p>Specifies the VPC used for non-EFS traffic.</p> <ul> <li> <p> <code>PublicInternetOnly</code> - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access.</p> </li> <li> <p> <code>VpcOnly</code> - All Studio traffic is through the specified VPC and subnets.</p> </li> </ul> <p>This configuration can only be modified if there are no apps in the <code>InService</code>, <code>Pending</code>, or <code>Deleting</code> state. The configuration cannot be updated if <code>DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn</code> is already set or <code>DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn</code> is provided as part of the same request.</p>"""
    tag_propagation: NotRequired["capo_sagemaker.types.tag_propagation.TagPropagation"]
    """<p>Indicates whether custom tag propagation is supported for the domain. Defaults to <code>DISABLED</code>.</p>"""
    home_efs_file_system_creation: NotRequired[
        "capo_sagemaker.types.home_efs_file_system_creation.HomeEfsFileSystemCreation"
    ]
    """<p>Indicates whether to create a home EFS file system for the domain. You can change from <code>Disabled</code> to <code>Enabled</code> to provision EFS on demand, but you cannot change from <code>Enabled</code> to <code>Disabled</code>.</p>"""
    vpc_id: NotRequired["capo_sagemaker.types.vpc_id.VpcId"]
    """<p>The identifier for the VPC used by the domain for network communication. Use this field only when adding VPC configuration to a SageMaker AI domain used in Amazon SageMaker Unified Studio that was created without VPC settings. SageMaker AI doesn't automatically apply VPC updates to existing applications. Stop and restart your applications to apply the changes.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDomainRequest) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "default_user_settings" in value:
        import capo_sagemaker.types.user_settings

        out["DefaultUserSettings"] = (
            capo_sagemaker.types.user_settings.serialize_aws_json_1_1(
                value["default_user_settings"]
            )
        )
    if "domain_settings_for_update" in value:
        import capo_sagemaker.types.domain_settings_for_update

        out["DomainSettingsForUpdate"] = (
            capo_sagemaker.types.domain_settings_for_update.serialize_aws_json_1_1(
                value["domain_settings_for_update"]
            )
        )
    if "app_security_group_management" in value:
        import capo_sagemaker.types.app_security_group_management

        out["AppSecurityGroupManagement"] = (
            capo_sagemaker.types.app_security_group_management.serialize_aws_json_1_1(
                value["app_security_group_management"]
            )
        )
    if "default_space_settings" in value:
        import capo_sagemaker.types.default_space_settings

        out["DefaultSpaceSettings"] = (
            capo_sagemaker.types.default_space_settings.serialize_aws_json_1_1(
                value["default_space_settings"]
            )
        )
    if "subnet_ids" in value:
        import capo_sagemaker.types.subnets

        out["SubnetIds"] = capo_sagemaker.types.subnets.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "app_network_access_type" in value:
        import capo_sagemaker.types.app_network_access_type

        out["AppNetworkAccessType"] = (
            capo_sagemaker.types.app_network_access_type.serialize_aws_json_1_1(
                value["app_network_access_type"]
            )
        )
    if "tag_propagation" in value:
        import capo_sagemaker.types.tag_propagation

        out["TagPropagation"] = (
            capo_sagemaker.types.tag_propagation.serialize_aws_json_1_1(
                value["tag_propagation"]
            )
        )
    if "home_efs_file_system_creation" in value:
        import capo_sagemaker.types.home_efs_file_system_creation

        out["HomeEfsFileSystemCreation"] = (
            capo_sagemaker.types.home_efs_file_system_creation.serialize_aws_json_1_1(
                value["home_efs_file_system_creation"]
            )
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDomainRequest:
    out: UpdateDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "DefaultUserSettings" in data:
        import capo_sagemaker.types.user_settings

        out["default_user_settings"] = (
            capo_sagemaker.types.user_settings.deserialize_aws_json_1_1(
                data["DefaultUserSettings"]
            )
        )
    if "DomainSettingsForUpdate" in data:
        import capo_sagemaker.types.domain_settings_for_update

        out["domain_settings_for_update"] = (
            capo_sagemaker.types.domain_settings_for_update.deserialize_aws_json_1_1(
                data["DomainSettingsForUpdate"]
            )
        )
    if "AppSecurityGroupManagement" in data:
        import capo_sagemaker.types.app_security_group_management

        out["app_security_group_management"] = (
            capo_sagemaker.types.app_security_group_management.deserialize_aws_json_1_1(
                data["AppSecurityGroupManagement"]
            )
        )
    if "DefaultSpaceSettings" in data:
        import capo_sagemaker.types.default_space_settings

        out["default_space_settings"] = (
            capo_sagemaker.types.default_space_settings.deserialize_aws_json_1_1(
                data["DefaultSpaceSettings"]
            )
        )
    if "SubnetIds" in data:
        import capo_sagemaker.types.subnets

        out["subnet_ids"] = capo_sagemaker.types.subnets.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "AppNetworkAccessType" in data:
        import capo_sagemaker.types.app_network_access_type

        out["app_network_access_type"] = (
            capo_sagemaker.types.app_network_access_type.deserialize_aws_json_1_1(
                data["AppNetworkAccessType"]
            )
        )
    if "TagPropagation" in data:
        import capo_sagemaker.types.tag_propagation

        out["tag_propagation"] = (
            capo_sagemaker.types.tag_propagation.deserialize_aws_json_1_1(
                data["TagPropagation"]
            )
        )
    if "HomeEfsFileSystemCreation" in data:
        import capo_sagemaker.types.home_efs_file_system_creation

        out["home_efs_file_system_creation"] = (
            capo_sagemaker.types.home_efs_file_system_creation.deserialize_aws_json_1_1(
                data["HomeEfsFileSystemCreation"]
            )
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    return out
