"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeDomainResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_network_access_type
    import aws_sdk_sagemaker.types.app_security_group_management
    import aws_sdk_sagemaker.types.auth_mode
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.default_space_settings
    import aws_sdk_sagemaker.types.domain_arn
    import aws_sdk_sagemaker.types.domain_id
    import aws_sdk_sagemaker.types.domain_name
    import aws_sdk_sagemaker.types.domain_settings
    import aws_sdk_sagemaker.types.domain_status
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.home_efs_file_system_creation
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.resource_id
    import aws_sdk_sagemaker.types.security_group_id
    import aws_sdk_sagemaker.types.single_sign_on_application_arn
    import aws_sdk_sagemaker.types.string256
    import aws_sdk_sagemaker.types.string1024
    import aws_sdk_sagemaker.types.subnets
    import aws_sdk_sagemaker.types.tag_propagation
    import aws_sdk_sagemaker.types.user_settings
    import aws_sdk_sagemaker.types.vpc_id


class DescribeDomainResponse(TypedDict):
    domain_arn: NotRequired["aws_sdk_sagemaker.types.domain_arn.DomainArn"]
    """<p>The domain's Amazon Resource Name (ARN).</p>"""
    domain_id: NotRequired["aws_sdk_sagemaker.types.domain_id.DomainId"]
    """<p>The domain ID.</p>"""
    domain_name: NotRequired["aws_sdk_sagemaker.types.domain_name.DomainName"]
    """<p>The domain name.</p>"""
    home_efs_file_system_id: NotRequired[
        "aws_sdk_sagemaker.types.resource_id.ResourceId"
    ]
    """<p>The ID of the Amazon Elastic File System managed by this Domain.</p>"""
    single_sign_on_managed_application_instance_id: NotRequired[
        "aws_sdk_sagemaker.types.string256.String256"
    ]
    """<p>The IAM Identity Center managed application instance ID.</p>"""
    single_sign_on_application_arn: NotRequired[
        "aws_sdk_sagemaker.types.single_sign_on_application_arn.SingleSignOnApplicationArn"
    ]
    """<p>The ARN of the application managed by SageMaker AI in IAM Identity Center. This value is only returned for domains created after October 1, 2023.</p>"""
    status: NotRequired["aws_sdk_sagemaker.types.domain_status.DomainStatus"]
    """<p>The status.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>The creation time.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The last modified time.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>The failure reason.</p>"""
    security_group_id_for_domain_boundary: NotRequired[
        "aws_sdk_sagemaker.types.security_group_id.SecurityGroupId"
    ]
    """<p>The ID of the security group that authorizes traffic between the <code>RSessionGateway</code> apps and the <code>RStudioServerPro</code> app.</p>"""
    auth_mode: NotRequired["aws_sdk_sagemaker.types.auth_mode.AuthMode"]
    """<p>The domain's authentication mode.</p>"""
    default_user_settings: NotRequired[
        "aws_sdk_sagemaker.types.user_settings.UserSettings"
    ]
    """<p>Settings which are applied to UserProfiles in this domain if settings are not explicitly specified in a given UserProfile. </p>"""
    domain_settings: NotRequired[
        "aws_sdk_sagemaker.types.domain_settings.DomainSettings"
    ]
    """<p>A collection of <code>Domain</code> settings.</p>"""
    app_network_access_type: NotRequired[
        "aws_sdk_sagemaker.types.app_network_access_type.AppNetworkAccessType"
    ]
    """<p>Specifies the VPC used for non-EFS traffic. The default value is <code>PublicInternetOnly</code>.</p> <ul> <li> <p> <code>PublicInternetOnly</code> - Non-EFS traffic is through a VPC managed by Amazon SageMaker AI, which allows direct internet access</p> </li> <li> <p> <code>VpcOnly</code> - All traffic is through the specified VPC and subnets</p> </li> </ul>"""
    home_efs_file_system_kms_key_id: NotRequired[
        "aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"
    ]
    """<p>Use <code>KmsKeyId</code>.</p>"""
    subnet_ids: NotRequired["aws_sdk_sagemaker.types.subnets.Subnets"]
    """<p>The VPC subnets that the domain uses for communication.</p>"""
    url: NotRequired["aws_sdk_sagemaker.types.string1024.String1024"]
    """<p>The domain's URL.</p>"""
    vpc_id: NotRequired["aws_sdk_sagemaker.types.vpc_id.VpcId"]
    """<p>The ID of the Amazon Virtual Private Cloud (VPC) that the domain uses for communication.</p>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS customer managed key used to encrypt the EFS volume attached to the domain.</p>"""
    app_security_group_management: NotRequired[
        "aws_sdk_sagemaker.types.app_security_group_management.AppSecurityGroupManagement"
    ]
    """<p>The entity that creates and manages the required security groups for inter-app communication in <code>VPCOnly</code> mode. Required when <code>CreateDomain.AppNetworkAccessType</code> is <code>VPCOnly</code> and <code>DomainSettings.RStudioServerProDomainSettings.DomainExecutionRoleArn</code> is provided.</p>"""
    home_efs_file_system_creation: NotRequired[
        "aws_sdk_sagemaker.types.home_efs_file_system_creation.HomeEfsFileSystemCreation"
    ]
    """<p>Indicates whether a home EFS file system is created for the domain.</p>"""
    tag_propagation: NotRequired[
        "aws_sdk_sagemaker.types.tag_propagation.TagPropagation"
    ]
    """<p>Indicates whether custom tag propagation is supported for the domain.</p>"""
    default_space_settings: NotRequired[
        "aws_sdk_sagemaker.types.default_space_settings.DefaultSpaceSettings"
    ]
    """<p>The default settings for shared spaces that users create in the domain.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeDomainResponse) -> dict:
    out: dict = {}
    if "domain_arn" in value:
        out["DomainArn"] = value["domain_arn"]
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "domain_name" in value:
        out["DomainName"] = value["domain_name"]
    if "home_efs_file_system_id" in value:
        out["HomeEfsFileSystemId"] = value["home_efs_file_system_id"]
    if "single_sign_on_managed_application_instance_id" in value:
        out["SingleSignOnManagedApplicationInstanceId"] = value[
            "single_sign_on_managed_application_instance_id"
        ]
    if "single_sign_on_application_arn" in value:
        out["SingleSignOnApplicationArn"] = value["single_sign_on_application_arn"]
    if "status" in value:
        import aws_sdk_sagemaker.types.domain_status

        out["Status"] = aws_sdk_sagemaker.types.domain_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "security_group_id_for_domain_boundary" in value:
        out["SecurityGroupIdForDomainBoundary"] = value[
            "security_group_id_for_domain_boundary"
        ]
    if "auth_mode" in value:
        import aws_sdk_sagemaker.types.auth_mode

        out["AuthMode"] = aws_sdk_sagemaker.types.auth_mode.serialize_aws_json_1_1(
            value["auth_mode"]
        )
    if "default_user_settings" in value:
        import aws_sdk_sagemaker.types.user_settings

        out["DefaultUserSettings"] = (
            aws_sdk_sagemaker.types.user_settings.serialize_aws_json_1_1(
                value["default_user_settings"]
            )
        )
    if "domain_settings" in value:
        import aws_sdk_sagemaker.types.domain_settings

        out["DomainSettings"] = (
            aws_sdk_sagemaker.types.domain_settings.serialize_aws_json_1_1(
                value["domain_settings"]
            )
        )
    if "app_network_access_type" in value:
        import aws_sdk_sagemaker.types.app_network_access_type

        out["AppNetworkAccessType"] = (
            aws_sdk_sagemaker.types.app_network_access_type.serialize_aws_json_1_1(
                value["app_network_access_type"]
            )
        )
    if "home_efs_file_system_kms_key_id" in value:
        out["HomeEfsFileSystemKmsKeyId"] = value["home_efs_file_system_kms_key_id"]
    if "subnet_ids" in value:
        import aws_sdk_sagemaker.types.subnets

        out["SubnetIds"] = aws_sdk_sagemaker.types.subnets.serialize_aws_json_1_1(
            value["subnet_ids"]
        )
    if "url" in value:
        out["Url"] = value["url"]
    if "vpc_id" in value:
        out["VpcId"] = value["vpc_id"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "app_security_group_management" in value:
        import aws_sdk_sagemaker.types.app_security_group_management

        out["AppSecurityGroupManagement"] = (
            aws_sdk_sagemaker.types.app_security_group_management.serialize_aws_json_1_1(
                value["app_security_group_management"]
            )
        )
    if "home_efs_file_system_creation" in value:
        import aws_sdk_sagemaker.types.home_efs_file_system_creation

        out["HomeEfsFileSystemCreation"] = (
            aws_sdk_sagemaker.types.home_efs_file_system_creation.serialize_aws_json_1_1(
                value["home_efs_file_system_creation"]
            )
        )
    if "tag_propagation" in value:
        import aws_sdk_sagemaker.types.tag_propagation

        out["TagPropagation"] = (
            aws_sdk_sagemaker.types.tag_propagation.serialize_aws_json_1_1(
                value["tag_propagation"]
            )
        )
    if "default_space_settings" in value:
        import aws_sdk_sagemaker.types.default_space_settings

        out["DefaultSpaceSettings"] = (
            aws_sdk_sagemaker.types.default_space_settings.serialize_aws_json_1_1(
                value["default_space_settings"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeDomainResponse:
    out: DescribeDomainResponse = {}  # type: ignore[typeddict-item]
    if "DomainArn" in data:
        out["domain_arn"] = data["DomainArn"]
    if "DomainId" in data:
        out["domain_id"] = data["DomainId"]
    if "DomainName" in data:
        out["domain_name"] = data["DomainName"]
    if "HomeEfsFileSystemId" in data:
        out["home_efs_file_system_id"] = data["HomeEfsFileSystemId"]
    if "SingleSignOnManagedApplicationInstanceId" in data:
        out["single_sign_on_managed_application_instance_id"] = data[
            "SingleSignOnManagedApplicationInstanceId"
        ]
    if "SingleSignOnApplicationArn" in data:
        out["single_sign_on_application_arn"] = data["SingleSignOnApplicationArn"]
    if "Status" in data:
        import aws_sdk_sagemaker.types.domain_status

        out["status"] = aws_sdk_sagemaker.types.domain_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "SecurityGroupIdForDomainBoundary" in data:
        out["security_group_id_for_domain_boundary"] = data[
            "SecurityGroupIdForDomainBoundary"
        ]
    if "AuthMode" in data:
        import aws_sdk_sagemaker.types.auth_mode

        out["auth_mode"] = aws_sdk_sagemaker.types.auth_mode.deserialize_aws_json_1_1(
            data["AuthMode"]
        )
    if "DefaultUserSettings" in data:
        import aws_sdk_sagemaker.types.user_settings

        out["default_user_settings"] = (
            aws_sdk_sagemaker.types.user_settings.deserialize_aws_json_1_1(
                data["DefaultUserSettings"]
            )
        )
    if "DomainSettings" in data:
        import aws_sdk_sagemaker.types.domain_settings

        out["domain_settings"] = (
            aws_sdk_sagemaker.types.domain_settings.deserialize_aws_json_1_1(
                data["DomainSettings"]
            )
        )
    if "AppNetworkAccessType" in data:
        import aws_sdk_sagemaker.types.app_network_access_type

        out["app_network_access_type"] = (
            aws_sdk_sagemaker.types.app_network_access_type.deserialize_aws_json_1_1(
                data["AppNetworkAccessType"]
            )
        )
    if "HomeEfsFileSystemKmsKeyId" in data:
        out["home_efs_file_system_kms_key_id"] = data["HomeEfsFileSystemKmsKeyId"]
    if "SubnetIds" in data:
        import aws_sdk_sagemaker.types.subnets

        out["subnet_ids"] = aws_sdk_sagemaker.types.subnets.deserialize_aws_json_1_1(
            data["SubnetIds"]
        )
    if "Url" in data:
        out["url"] = data["Url"]
    if "VpcId" in data:
        out["vpc_id"] = data["VpcId"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "AppSecurityGroupManagement" in data:
        import aws_sdk_sagemaker.types.app_security_group_management

        out["app_security_group_management"] = (
            aws_sdk_sagemaker.types.app_security_group_management.deserialize_aws_json_1_1(
                data["AppSecurityGroupManagement"]
            )
        )
    if "HomeEfsFileSystemCreation" in data:
        import aws_sdk_sagemaker.types.home_efs_file_system_creation

        out["home_efs_file_system_creation"] = (
            aws_sdk_sagemaker.types.home_efs_file_system_creation.deserialize_aws_json_1_1(
                data["HomeEfsFileSystemCreation"]
            )
        )
    if "TagPropagation" in data:
        import aws_sdk_sagemaker.types.tag_propagation

        out["tag_propagation"] = (
            aws_sdk_sagemaker.types.tag_propagation.deserialize_aws_json_1_1(
                data["TagPropagation"]
            )
        )
    if "DefaultSpaceSettings" in data:
        import aws_sdk_sagemaker.types.default_space_settings

        out["default_space_settings"] = (
            aws_sdk_sagemaker.types.default_space_settings.deserialize_aws_json_1_1(
                data["DefaultSpaceSettings"]
            )
        )
    return out
