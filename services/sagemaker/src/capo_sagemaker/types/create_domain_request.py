"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateDomainRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_network_access_type
    import capo_sagemaker.types.app_security_group_management
    import capo_sagemaker.types.auth_mode
    import capo_sagemaker.types.default_space_settings
    import capo_sagemaker.types.domain_name
    import capo_sagemaker.types.domain_settings
    import capo_sagemaker.types.home_efs_file_system_creation
    import capo_sagemaker.types.kms_key_id
    import capo_sagemaker.types.subnets
    import capo_sagemaker.types.tag_list
    import capo_sagemaker.types.tag_propagation
    import capo_sagemaker.types.user_settings
    import capo_sagemaker.types.vpc_id


class CreateDomainRequest(TypedDict, closed=True):
    domain_name: NotRequired["capo_sagemaker.types.domain_name.DomainName"]
    """<p>A name for the domain.</p>"""
    auth_mode: NotRequired["capo_sagemaker.types.auth_mode.AuthMode"]
    """<p>The mode of authentication that members use to access the domain.</p>"""
    default_user_settings: NotRequired[
        "capo_sagemaker.types.user_settings.UserSettings"
    ]
    """<p>The default settings to use to create a user profile when <code>UserSettings</code> isn't specified in the call to the <code>CreateUserProfile</code> API.</p> <p> <code>SecurityGroups</code> is aggregated when specified in both calls. For all other settings in <code>UserSettings</code>, the values specified in <code>CreateUserProfile</code> take precedence over those specified in <code>CreateDomain</code>.</p>"""
    domain_settings: NotRequired["capo_sagemaker.types.domain_settings.DomainSettings"]
    """<p>A collection of <code>Domain</code> settings.</p>"""
    subnet_ids: NotRequired["capo_sagemaker.types.subnets.Subnets"]
    """<p>The VPC subnets that the domain uses for communication.</p> <p>The field is optional when the <code>AppNetworkAccessType</code> parameter is set to <code>PublicInternetOnly</code> for domains created from Amazon SageMaker Unified Studio.</p>"""
    vpc_id: NotRequired["capo_sagemaker.types.vpc_id.VpcId"]
    """<p>The ID of the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.</p> <p>The field is optional when the <code>AppNetworkAccessType</code> parameter is set to <code>PublicInternetOnly</code> for domains created from Amazon SageMaker Unified Studio.</p>"""
    tags: NotRequired["capo_sagemaker.types.tag_list.TagList"]
    """<p>Tags to associated with the Domain. Each tag consists of a key and an optional value. Tag keys must be unique per resource. Tags are searchable using the <code>Search</code> API.</p> <p>Tags that you specify for the Domain are also added to all Apps that the Domain launches.</p>"""
    app_network_access_type: NotRequired[
        "capo_sagemaker.types.app_network_access_type.AppNetworkAccessType"
    ]
    """<p>Specifies the VPC used for non-EFS traffic. The default value is <code>PublicInternetOnly</code>.</p> <ul> <li> <p> <code>PublicInternetOnly</code> - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access</p> </li> <li> <p> <code>VpcOnly</code> - All traffic is through the specified VPC and subnets</p> </li> </ul>"""
    home_efs_file_system_kms_key_id: NotRequired[
        "capo_sagemaker.types.kms_key_id.KmsKeyId"
    ]
    """<p>Use <code>KmsKeyId</code>.</p>"""
    kms_key_id: NotRequired["capo_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>SageMaker AI uses Amazon Web Services KMS to encrypt EFS and EBS volumes attached to the domain with an Amazon Web Services managed key by default. For more control, specify a customer managed key.</p>"""
    app_security_group_management: NotRequired[
        "capo_sagemaker.types.app_security_group_management.AppSecurityGroupManagement"
    ]
    """<p>The entity that creates and manages the required security groups for inter-app communication in <code>VPCOnly</code> mode. Required when <code>CreateDomain.AppNetworkAccessType</code> is <code>VPCOnly</code> and <code>DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn</code> is provided. If setting up the domain for use with RStudio, this value must be set to <code>Service</code>.</p>"""
    home_efs_file_system_creation: NotRequired[
        "capo_sagemaker.types.home_efs_file_system_creation.HomeEfsFileSystemCreation"
    ]
    """<p>Indicates whether to create a home EFS file system for the domain. Defaults to <code>Enabled</code>. Set to <code>Disabled</code> to skip EFS creation and reduce domain creation time. You can enable EFS later by calling <code>UpdateDomain</code>.</p>"""
    tag_propagation: NotRequired["capo_sagemaker.types.tag_propagation.TagPropagation"]
    """<p>Indicates whether custom tag propagation is supported for the domain. Defaults to <code>DISABLED</code>.</p>"""
    default_space_settings: NotRequired[
        "capo_sagemaker.types.default_space_settings.DefaultSpaceSettings"
    ]
    """<p>The default settings for shared spaces that users create in the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateDomainRequest) -> dict:
    out: dict = {}
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "auth_mode" in value:
        import capo_sagemaker.types.auth_mode

        out["AuthMode"] = capo_sagemaker.types.auth_mode.serialize_aws_json_1_1(
            value["auth_mode"]
        )
    if "default_user_settings" in value:
        import capo_sagemaker.types.user_settings

        out["DefaultUserSettings"] = (
            capo_sagemaker.types.user_settings.serialize_aws_json_1_1(
                value["default_user_settings"]
            )
        )
    if "domain_settings" in value:
        import capo_sagemaker.types.domain_settings

        out["DomainSettings"] = (
            capo_sagemaker.types.domain_settings.serialize_aws_json_1_1(
                value["domain_settings"]
            )
        )
    if "subnet_ids" in value:
        import capo_sagemaker.types.subnets

        out["SubnetIds"] = capo_sagemaker.types.subnets.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "tags" in value:
        import capo_sagemaker.types.tag_list

        out["Tags"] = capo_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "app_network_access_type" in value:
        import capo_sagemaker.types.app_network_access_type

        out["AppNetworkAccessType"] = (
            capo_sagemaker.types.app_network_access_type.serialize_aws_json_1_1(
                value["app_network_access_type"]
            )
        )
    if "home_efs_file_system_kms_key_id" in value:
        out["HomeEfsFileSystemKmsKeyId"] = value["home_efs_file_system_kms_key_id"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "app_security_group_management" in value:
        import capo_sagemaker.types.app_security_group_management

        out["AppSecurityGroupManagement"] = (
            capo_sagemaker.types.app_security_group_management.serialize_aws_json_1_1(
                value["app_security_group_management"]
            )
        )
    if "home_efs_file_system_creation" in value:
        import capo_sagemaker.types.home_efs_file_system_creation

        out["HomeEfsFileSystemCreation"] = (
            capo_sagemaker.types.home_efs_file_system_creation.serialize_aws_json_1_1(
                value["home_efs_file_system_creation"]
            )
        )
    if "tag_propagation" in value:
        import capo_sagemaker.types.tag_propagation

        out["TagPropagation"] = (
            capo_sagemaker.types.tag_propagation.serialize_aws_json_1_1(
                value["tag_propagation"]
            )
        )
    if "default_space_settings" in value:
        import capo_sagemaker.types.default_space_settings

        out["DefaultSpaceSettings"] = (
            capo_sagemaker.types.default_space_settings.serialize_aws_json_1_1(
                value["default_space_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateDomainRequest:
    out: CreateDomainRequest = {}  # type: ignore[typeddict-item]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "AuthMode" in data:
        import capo_sagemaker.types.auth_mode

        out["auth_mode"] = capo_sagemaker.types.auth_mode.deserialize_aws_json_1_1(
            data["AuthMode"]
        )
    if "DefaultUserSettings" in data:
        import capo_sagemaker.types.user_settings

        out["default_user_settings"] = (
            capo_sagemaker.types.user_settings.deserialize_aws_json_1_1(
                data["DefaultUserSettings"]
            )
        )
    if "DomainSettings" in data:
        import capo_sagemaker.types.domain_settings

        out["domain_settings"] = (
            capo_sagemaker.types.domain_settings.deserialize_aws_json_1_1(
                data["DomainSettings"]
            )
        )
    if "SubnetIds" in data:
        import capo_sagemaker.types.subnets

        out["subnet_ids"] = capo_sagemaker.types.subnets.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "Tags" in data:
        import capo_sagemaker.types.tag_list

        out["tags"] = capo_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "AppNetworkAccessType" in data:
        import capo_sagemaker.types.app_network_access_type

        out["app_network_access_type"] = (
            capo_sagemaker.types.app_network_access_type.deserialize_aws_json_1_1(
                data["AppNetworkAccessType"]
            )
        )
    if "HomeEfsFileSystemKmsKeyId" in data:
        out["home_efs_file_system_kms_key_id"] = data["HomeEfsFileSystemKmsKeyId"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "AppSecurityGroupManagement" in data:
        import capo_sagemaker.types.app_security_group_management

        out["app_security_group_management"] = (
            capo_sagemaker.types.app_security_group_management.deserialize_aws_json_1_1(
                data["AppSecurityGroupManagement"]
            )
        )
    if "HomeEfsFileSystemCreation" in data:
        import capo_sagemaker.types.home_efs_file_system_creation

        out["home_efs_file_system_creation"] = (
            capo_sagemaker.types.home_efs_file_system_creation.deserialize_aws_json_1_1(
                data["HomeEfsFileSystemCreation"]
            )
        )
    if "TagPropagation" in data:
        import capo_sagemaker.types.tag_propagation

        out["tag_propagation"] = (
            capo_sagemaker.types.tag_propagation.deserialize_aws_json_1_1(
                data["TagPropagation"]
            )
        )
    if "DefaultSpaceSettings" in data:
        import capo_sagemaker.types.default_space_settings

        out["default_space_settings"] = (
            capo_sagemaker.types.default_space_settings.deserialize_aws_json_1_1(
                data["DefaultSpaceSettings"]
            )
        )
    return out
