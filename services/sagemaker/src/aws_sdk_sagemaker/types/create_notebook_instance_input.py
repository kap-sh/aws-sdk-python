"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateNotebookInstanceInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_code_repository_names_or_urls
    import aws_sdk_sagemaker.types.code_repository_name_or_url
    import aws_sdk_sagemaker.types.direct_internet_access
    import aws_sdk_sagemaker.types.instance_metadata_service_configuration
    import aws_sdk_sagemaker.types.instance_type
    import aws_sdk_sagemaker.types.ip_address_type
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.notebook_instance_accelerator_types
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name
    import aws_sdk_sagemaker.types.notebook_instance_name
    import aws_sdk_sagemaker.types.notebook_instance_volume_size_in_gb
    import aws_sdk_sagemaker.types.platform_identifier
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.root_access
    import aws_sdk_sagemaker.types.security_group_ids
    import aws_sdk_sagemaker.types.subnet_id
    import aws_sdk_sagemaker.types.tag_list


class CreateNotebookInstanceInput(TypedDict):
    notebook_instance_name: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_name.NotebookInstanceName"
    ]
    """<p>The name of the new notebook instance.</p>"""
    instance_type: NotRequired["aws_sdk_sagemaker.types.instance_type.InstanceType"]
    """<p>The type of ML compute instance to launch for the notebook instance.</p>"""
    subnet_id: NotRequired["aws_sdk_sagemaker.types.subnet_id.SubnetId"]
    """<p>The ID of the subnet in a VPC to which you would like to have a connectivity from your ML compute instance. </p>"""
    security_group_ids: NotRequired[
        "aws_sdk_sagemaker.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The VPC security group IDs, in the form sg-xxxxxxxx. The security groups must be for the same VPC as specified in the subnet. </p>"""
    ip_address_type: NotRequired[
        "aws_sdk_sagemaker.types.ip_address_type.IPAddressType"
    ]
    """<p>The IP address type for the notebook instance. Specify <code>ipv4</code> for IPv4-only connectivity or <code>dualstack</code> for both IPv4 and IPv6 connectivity. When you specify <code>dualstack</code>, the subnet must support IPv6 CIDR blocks. If not specified, defaults to <code>ipv4</code>.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    r"""<p> When you send any requests to Amazon Web Services resources from the notebook instance, SageMaker AI assumes this role to perform tasks on your behalf. You must grant this role necessary permissions so SageMaker AI can perform these tasks. The policy must allow the SageMaker AI service principal (sagemaker.amazonaws.com) permissions to assume this role. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html\">SageMaker AI Roles</a>. </p> <note> <p>To be able to pass this role to SageMaker AI, the caller of this API must have the <code>iam:PassRole</code> permission.</p> </note>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    r"""<p>The Amazon Resource Name (ARN) of a Amazon Web Services Key Management Service key that SageMaker AI uses to encrypt data on the storage volume attached to your notebook instance. The KMS key you provide must be enabled. For information, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/enabling-keys.html\">Enabling and Disabling Keys</a> in the <i>Amazon Web Services Key Management Service Developer Guide</i>.</p>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p>"""
    lifecycle_config_name: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    r"""<p>The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html\">Step 2.1: (Optional) Customize a Notebook Instance</a>.</p>"""
    direct_internet_access: NotRequired[
        "aws_sdk_sagemaker.types.direct_internet_access.DirectInternetAccess"
    ]
    r"""<p>Sets whether SageMaker AI provides internet access to the notebook instance. If you set this to <code>Disabled</code> this notebook instance is able to access resources only in your VPC, and is not be able to connect to SageMaker AI training and endpoint services unless you configure a NAT Gateway in your VPC.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access\">Notebook Instances Are Internet-Enabled by Default</a>. You can set the value of this parameter to <code>Disabled</code> only if you set a value for the <code>SubnetId</code> parameter.</p>"""
    volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_volume_size_in_gb.NotebookInstanceVolumeSizeInGB"
    ]
    """<p>The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB.</p>"""
    accelerator_types: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_accelerator_types.NotebookInstanceAcceleratorTypes"
    ]
    """<p>This parameter is no longer supported. Elastic Inference (EI) is no longer available.</p> <p>This parameter was used to specify a list of EI instance types to associate with this notebook instance.</p>"""
    default_code_repository: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_name_or_url.CodeRepositoryNameOrUrl"
    ]
    r"""<p>A Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">Amazon Web Services CodeCommit</a> or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html\">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""
    additional_code_repositories: NotRequired[
        "aws_sdk_sagemaker.types.additional_code_repository_names_or_urls.AdditionalCodeRepositoryNamesOrUrls"
    ]
    r"""<p>An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">Amazon Web Services CodeCommit</a> or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html\">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""
    root_access: NotRequired["aws_sdk_sagemaker.types.root_access.RootAccess"]
    """<p>Whether root access is enabled or disabled for users of the notebook instance. The default value is <code>Enabled</code>.</p> <note> <p>Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.</p> </note>"""
    platform_identifier: NotRequired[
        "aws_sdk_sagemaker.types.platform_identifier.PlatformIdentifier"
    ]
    """<p>The platform identifier of the notebook instance runtime environment. The default value is <code>notebook-al2023-v1</code>.</p>"""
    instance_metadata_service_configuration: NotRequired[
        "aws_sdk_sagemaker.types.instance_metadata_service_configuration.InstanceMetadataServiceConfiguration"
    ]
    """<p>Information on the IMDS configuration of the notebook instance</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNotebookInstanceInput) -> dict:
    out: dict = {}
    if "notebook_instance_name" in value:
        out["NotebookInstanceName"] = value["notebook_instance_name"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "security_group_ids" in value:
        import aws_sdk_sagemaker.types.security_group_ids

        out["SecurityGroupIds"] = (
            aws_sdk_sagemaker.types.security_group_ids.serialize_aws_json_1_1(
                value["security_group_ids"]
            )
        )
    if "ip_address_type" in value:
        import aws_sdk_sagemaker.types.ip_address_type

        out["IpAddressType"] = (
            aws_sdk_sagemaker.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "lifecycle_config_name" in value:
        out["LifecycleConfigName"] = value["lifecycle_config_name"]
    if "direct_internet_access" in value:
        import aws_sdk_sagemaker.types.direct_internet_access

        out["DirectInternetAccess"] = (
            aws_sdk_sagemaker.types.direct_internet_access.serialize_aws_json_1_1(
                value["direct_internet_access"]
            )
        )
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "accelerator_types" in value:
        import aws_sdk_sagemaker.types.notebook_instance_accelerator_types

        out["AcceleratorTypes"] = (
            aws_sdk_sagemaker.types.notebook_instance_accelerator_types.serialize_aws_json_1_1(
                value["accelerator_types"]
            )
        )
    if "default_code_repository" in value:
        out["DefaultCodeRepository"] = value["default_code_repository"]
    if "additional_code_repositories" in value:
        import aws_sdk_sagemaker.types.additional_code_repository_names_or_urls

        out["AdditionalCodeRepositories"] = (
            aws_sdk_sagemaker.types.additional_code_repository_names_or_urls.serialize_aws_json_1_1(
                value["additional_code_repositories"]
            )
        )
    if "root_access" in value:
        import aws_sdk_sagemaker.types.root_access

        out["RootAccess"] = aws_sdk_sagemaker.types.root_access.serialize_aws_json_1_1(
            value["root_access"]
        )
    if "platform_identifier" in value:
        out["PlatformIdentifier"] = value["platform_identifier"]
    if "instance_metadata_service_configuration" in value:
        import aws_sdk_sagemaker.types.instance_metadata_service_configuration

        out["InstanceMetadataServiceConfiguration"] = (
            aws_sdk_sagemaker.types.instance_metadata_service_configuration.serialize_aws_json_1_1(
                value["instance_metadata_service_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNotebookInstanceInput:
    out: CreateNotebookInstanceInput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceName" in data:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "SecurityGroupIds" in data:
        import aws_sdk_sagemaker.types.security_group_ids

        out["security_group_ids"] = (
            aws_sdk_sagemaker.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroupIds"]
            )
        )
    if "IpAddressType" in data:
        import aws_sdk_sagemaker.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_sagemaker.types.ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "LifecycleConfigName" in data:
        out["lifecycle_config_name"] = data["LifecycleConfigName"]
    if "DirectInternetAccess" in data:
        import aws_sdk_sagemaker.types.direct_internet_access

        out["direct_internet_access"] = (
            aws_sdk_sagemaker.types.direct_internet_access.deserialize_aws_json_1_1(
                data["DirectInternetAccess"]
            )
        )
    if "VolumeSizeInGB" in data:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if "AcceleratorTypes" in data:
        import aws_sdk_sagemaker.types.notebook_instance_accelerator_types

        out["accelerator_types"] = (
            aws_sdk_sagemaker.types.notebook_instance_accelerator_types.deserialize_aws_json_1_1(
                data["AcceleratorTypes"]
            )
        )
    if "DefaultCodeRepository" in data:
        out["default_code_repository"] = data["DefaultCodeRepository"]
    if "AdditionalCodeRepositories" in data:
        import aws_sdk_sagemaker.types.additional_code_repository_names_or_urls

        out["additional_code_repositories"] = (
            aws_sdk_sagemaker.types.additional_code_repository_names_or_urls.deserialize_aws_json_1_1(
                data["AdditionalCodeRepositories"]
            )
        )
    if "RootAccess" in data:
        import aws_sdk_sagemaker.types.root_access

        out["root_access"] = (
            aws_sdk_sagemaker.types.root_access.deserialize_aws_json_1_1(
                data["RootAccess"]
            )
        )
    if "PlatformIdentifier" in data:
        out["platform_identifier"] = data["PlatformIdentifier"]
    if "InstanceMetadataServiceConfiguration" in data:
        import aws_sdk_sagemaker.types.instance_metadata_service_configuration

        out["instance_metadata_service_configuration"] = (
            aws_sdk_sagemaker.types.instance_metadata_service_configuration.deserialize_aws_json_1_1(
                data["InstanceMetadataServiceConfiguration"]
            )
        )
    return out
