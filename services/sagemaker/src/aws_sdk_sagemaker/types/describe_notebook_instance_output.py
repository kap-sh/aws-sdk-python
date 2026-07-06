"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeNotebookInstanceOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_code_repository_names_or_urls
    import aws_sdk_sagemaker.types.code_repository_name_or_url
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.direct_internet_access
    import aws_sdk_sagemaker.types.failure_reason
    import aws_sdk_sagemaker.types.instance_metadata_service_configuration
    import aws_sdk_sagemaker.types.instance_type
    import aws_sdk_sagemaker.types.ip_address_type
    import aws_sdk_sagemaker.types.kms_key_id
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.network_interface_id
    import aws_sdk_sagemaker.types.notebook_instance_accelerator_types
    import aws_sdk_sagemaker.types.notebook_instance_arn
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name
    import aws_sdk_sagemaker.types.notebook_instance_name
    import aws_sdk_sagemaker.types.notebook_instance_status
    import aws_sdk_sagemaker.types.notebook_instance_url
    import aws_sdk_sagemaker.types.notebook_instance_volume_size_in_gb
    import aws_sdk_sagemaker.types.platform_identifier
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.root_access
    import aws_sdk_sagemaker.types.security_group_ids
    import aws_sdk_sagemaker.types.subnet_id


class DescribeNotebookInstanceOutput(TypedDict, closed=True):
    notebook_instance_arn: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_arn.NotebookInstanceArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the notebook instance.</p>"""
    notebook_instance_name: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_name.NotebookInstanceName"
    ]
    """<p>The name of the SageMaker AI notebook instance. </p>"""
    notebook_instance_status: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_status.NotebookInstanceStatus"
    ]
    """<p>The status of the notebook instance.</p>"""
    failure_reason: NotRequired["aws_sdk_sagemaker.types.failure_reason.FailureReason"]
    """<p>If status is <code>Failed</code>, the reason it failed.</p>"""
    url: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_url.NotebookInstanceUrl"
    ]
    """<p>The URL that you use to connect to the Jupyter notebook that is running in your notebook instance. </p>"""
    instance_type: NotRequired["aws_sdk_sagemaker.types.instance_type.InstanceType"]
    """<p>The type of ML compute instance running on the notebook instance.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_sagemaker.types.ip_address_type.IPAddressType"
    ]
    """<p>The IP address type configured for the notebook instance. Returns <code>ipv4</code> for IPv4-only connectivity or <code>dualstack</code> for both IPv4 and IPv6 connectivity.</p>"""
    subnet_id: NotRequired["aws_sdk_sagemaker.types.subnet_id.SubnetId"]
    """<p>The ID of the VPC subnet.</p>"""
    security_groups: NotRequired[
        "aws_sdk_sagemaker.types.security_group_ids.SecurityGroupIds"
    ]
    """<p>The IDs of the VPC security groups.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role associated with the instance. </p>"""
    kms_key_id: NotRequired["aws_sdk_sagemaker.types.kms_key_id.KmsKeyId"]
    """<p>The Amazon Web Services KMS key ID SageMaker AI uses to encrypt data when storing it on the ML storage volume attached to the instance. </p>"""
    network_interface_id: NotRequired[
        "aws_sdk_sagemaker.types.network_interface_id.NetworkInterfaceId"
    ]
    """<p>The network interface IDs that SageMaker AI created at the time of creating the instance. </p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp. Use this parameter to retrieve the time when the notebook instance was last modified. </p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp. Use this parameter to return the time when the notebook instance was created</p>"""
    notebook_instance_lifecycle_config_name: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    r"""<p>Returns the name of a notebook instance lifecycle configuration.</p> <p>For information about notebook instance lifestyle configurations, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html\">Step 2.1: (Optional) Customize a Notebook Instance</a> </p>"""
    direct_internet_access: NotRequired[
        "aws_sdk_sagemaker.types.direct_internet_access.DirectInternetAccess"
    ]
    r"""<p>Describes whether SageMaker AI provides internet access to the notebook instance. If this value is set to <i>Disabled</i>, the notebook instance does not have internet access, and cannot connect to SageMaker AI training and endpoint services.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/appendix-additional-considerations.html#appendix-notebook-and-internet-access\">Notebook Instances Are Internet-Enabled by Default</a>.</p>"""
    volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_volume_size_in_gb.NotebookInstanceVolumeSizeInGB"
    ]
    """<p>The size, in GB, of the ML storage volume attached to the notebook instance.</p>"""
    accelerator_types: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_accelerator_types.NotebookInstanceAcceleratorTypes"
    ]
    """<p>This parameter is no longer supported. Elastic Inference (EI) is no longer available.</p> <p>This parameter was used to specify a list of the EI instance types associated with this notebook instance.</p>"""
    default_code_repository: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_name_or_url.CodeRepositoryNameOrUrl"
    ]
    r"""<p>The Git repository associated with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">Amazon Web Services CodeCommit</a> or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html\">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""
    additional_code_repositories: NotRequired[
        "aws_sdk_sagemaker.types.additional_code_repository_names_or_urls.AdditionalCodeRepositoryNamesOrUrls"
    ]
    r"""<p>An array of up to three Git repositories associated with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">Amazon Web Services CodeCommit</a> or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html\">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""
    root_access: NotRequired["aws_sdk_sagemaker.types.root_access.RootAccess"]
    """<p>Whether root access is enabled or disabled for users of the notebook instance.</p> <note> <p>Lifecycle configurations need root access to be able to set up a notebook instance. Because of this, lifecycle configurations associated with a notebook instance always run with root access even if you disable root access for users.</p> </note>"""
    platform_identifier: NotRequired[
        "aws_sdk_sagemaker.types.platform_identifier.PlatformIdentifier"
    ]
    """<p>The platform identifier of the notebook instance runtime environment.</p>"""
    instance_metadata_service_configuration: NotRequired[
        "aws_sdk_sagemaker.types.instance_metadata_service_configuration.InstanceMetadataServiceConfiguration"
    ]
    """<p>Information on the IMDS configuration of the notebook instance</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNotebookInstanceOutput) -> dict:
    out: dict = {}
    if "notebook_instance_arn" in value:
        out["NotebookInstanceArn"] = value["notebook_instance_arn"]
    if "notebook_instance_name" in value:
        out["NotebookInstanceName"] = value["notebook_instance_name"]
    if "notebook_instance_status" in value:
        import aws_sdk_sagemaker.types.notebook_instance_status

        out["NotebookInstanceStatus"] = (
            aws_sdk_sagemaker.types.notebook_instance_status.serialize_aws_json_1_1(
                value["notebook_instance_status"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "url" in value:
        out["Url"] = value["url"]
    if "instance_type" in value:
        import aws_sdk_sagemaker.types.instance_type

        out["InstanceType"] = (
            aws_sdk_sagemaker.types.instance_type.serialize_aws_json_1_1(
                value["instance_type"]
            )
        )
    if "ip_address_type" in value:
        import aws_sdk_sagemaker.types.ip_address_type

        out["IpAddressType"] = (
            aws_sdk_sagemaker.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "subnet_id" in value:
        out["SubnetId"] = value["subnet_id"]
    if "security_groups" in value:
        import aws_sdk_sagemaker.types.security_group_ids

        out["SecurityGroups"] = (
            aws_sdk_sagemaker.types.security_group_ids.serialize_aws_json_1_1(
                value["security_groups"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "kms_key_id" in value:
        out["KmsKeyId"] = value["kms_key_id"]
    if "network_interface_id" in value:
        out["NetworkInterfaceId"] = value["network_interface_id"]
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
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


def deserialize_aws_json_1_1(data: dict) -> DescribeNotebookInstanceOutput:
    out: DescribeNotebookInstanceOutput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceArn" in data:
        out["notebook_instance_arn"] = data["NotebookInstanceArn"]
    if "NotebookInstanceName" in data:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
    if "NotebookInstanceStatus" in data:
        import aws_sdk_sagemaker.types.notebook_instance_status

        out["notebook_instance_status"] = (
            aws_sdk_sagemaker.types.notebook_instance_status.deserialize_aws_json_1_1(
                data["NotebookInstanceStatus"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "Url" in data:
        out["url"] = data["Url"]
    if "InstanceType" in data:
        import aws_sdk_sagemaker.types.instance_type

        out["instance_type"] = (
            aws_sdk_sagemaker.types.instance_type.deserialize_aws_json_1_1(
                data["InstanceType"]
            )
        )
    if "IpAddressType" in data:
        import aws_sdk_sagemaker.types.ip_address_type

        out["ip_address_type"] = (
            aws_sdk_sagemaker.types.ip_address_type.deserialize_aws_json_1_1(
                data["IpAddressType"]
            )
        )
    if "SubnetId" in data:
        out["subnet_id"] = data["SubnetId"]
    if "SecurityGroups" in data:
        import aws_sdk_sagemaker.types.security_group_ids

        out["security_groups"] = (
            aws_sdk_sagemaker.types.security_group_ids.deserialize_aws_json_1_1(
                data["SecurityGroups"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "KmsKeyId" in data:
        out["kms_key_id"] = data["KmsKeyId"]
    if "NetworkInterfaceId" in data:
        out["network_interface_id"] = data["NetworkInterfaceId"]
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "NotebookInstanceLifecycleConfigName" in data:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
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
