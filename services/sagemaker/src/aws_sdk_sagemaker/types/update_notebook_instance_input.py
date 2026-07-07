"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateNotebookInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.additional_code_repository_names_or_urls
    import aws_sdk_sagemaker.types.code_repository_name_or_url
    import aws_sdk_sagemaker.types.disassociate_additional_code_repositories
    import aws_sdk_sagemaker.types.disassociate_default_code_repository
    import aws_sdk_sagemaker.types.disassociate_notebook_instance_accelerator_types
    import aws_sdk_sagemaker.types.disassociate_notebook_instance_lifecycle_config
    import aws_sdk_sagemaker.types.instance_metadata_service_configuration
    import aws_sdk_sagemaker.types.instance_type
    import aws_sdk_sagemaker.types.ip_address_type
    import aws_sdk_sagemaker.types.notebook_instance_accelerator_types
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name
    import aws_sdk_sagemaker.types.notebook_instance_name
    import aws_sdk_sagemaker.types.notebook_instance_volume_size_in_gb
    import aws_sdk_sagemaker.types.platform_identifier
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.root_access


class UpdateNotebookInstanceInput(TypedDict, closed=True):
    notebook_instance_name: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_name.NotebookInstanceName"
    ]
    """<p>The name of the notebook instance to update.</p>"""
    instance_type: NotRequired["aws_sdk_sagemaker.types.instance_type.InstanceType"]
    """<p>The Amazon ML compute instance type.</p>"""
    ip_address_type: NotRequired[
        "aws_sdk_sagemaker.types.ip_address_type.IPAddressType"
    ]
    """<p>The IP address type for the notebook instance. Specify <code>ipv4</code> for IPv4-only connectivity or <code>dualstack</code> for both IPv4 and IPv6 connectivity. The notebook instance must be stopped before updating this setting. When you specify <code>dualstack</code>, the subnet must support IPv6 addressing.</p>"""
    platform_identifier: NotRequired[
        "aws_sdk_sagemaker.types.platform_identifier.PlatformIdentifier"
    ]
    """<p>The platform identifier of the notebook instance runtime environment.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of the IAM role that SageMaker AI can assume to access the notebook instance. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html\">SageMaker AI Roles</a>. </p> <note> <p>To be able to pass this role to SageMaker AI, the caller of this API must have the <code>iam:PassRole</code> permission.</p> </note>"""
    lifecycle_config_name: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    r"""<p>The name of a lifecycle configuration to associate with the notebook instance. For information about lifestyle configurations, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/notebook-lifecycle-config.html\">Step 2.1: (Optional) Customize a Notebook Instance</a>.</p>"""
    disassociate_lifecycle_config: NotRequired[
        "aws_sdk_sagemaker.types.disassociate_notebook_instance_lifecycle_config.DisassociateNotebookInstanceLifecycleConfig"
    ]
    """<p>Set to <code>true</code> to remove the notebook instance lifecycle configuration currently associated with the notebook instance. This operation is idempotent. If you specify a lifecycle configuration that is not associated with the notebook instance when you call this method, it does not throw an error.</p>"""
    volume_size_in_gb: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_volume_size_in_gb.NotebookInstanceVolumeSizeInGB"
    ]
    """<p>The size, in GB, of the ML storage volume to attach to the notebook instance. The default value is 5 GB. ML storage volumes are encrypted, so SageMaker AI can't determine the amount of available free space on the volume. Because of this, you can increase the volume size when you update a notebook instance, but you can't decrease the volume size. If you want to decrease the size of the ML storage volume in use, create a new notebook instance with the desired size.</p>"""
    default_code_repository: NotRequired[
        "aws_sdk_sagemaker.types.code_repository_name_or_url.CodeRepositoryNameOrUrl"
    ]
    r"""<p>The Git repository to associate with the notebook instance as its default code repository. This can be either the name of a Git repository stored as a resource in your account, or the URL of a Git repository in <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">Amazon Web Services CodeCommit</a> or in any other Git repository. When you open a notebook instance, it opens in the directory that contains this repository. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html\">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""
    additional_code_repositories: NotRequired[
        "aws_sdk_sagemaker.types.additional_code_repository_names_or_urls.AdditionalCodeRepositoryNamesOrUrls"
    ]
    r"""<p>An array of up to three Git repositories to associate with the notebook instance. These can be either the names of Git repositories stored as resources in your account, or the URL of Git repositories in <a href=\"https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html\">Amazon Web Services CodeCommit</a> or in any other Git repository. These repositories are cloned at the same level as the default repository of your notebook instance. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-repo.html\">Associating Git Repositories with SageMaker AI Notebook Instances</a>.</p>"""
    accelerator_types: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_accelerator_types.NotebookInstanceAcceleratorTypes"
    ]
    """<p>This parameter is no longer supported. Elastic Inference (EI) is no longer available.</p> <p>This parameter was used to specify a list of the EI instance types to associate with this notebook instance.</p>"""
    disassociate_accelerator_types: NotRequired[
        "aws_sdk_sagemaker.types.disassociate_notebook_instance_accelerator_types.DisassociateNotebookInstanceAcceleratorTypes"
    ]
    """<p>This parameter is no longer supported. Elastic Inference (EI) is no longer available.</p> <p>This parameter was used to specify a list of the EI instance types to remove from this notebook instance.</p>"""
    disassociate_default_code_repository: NotRequired[
        "aws_sdk_sagemaker.types.disassociate_default_code_repository.DisassociateDefaultCodeRepository"
    ]
    """<p>The name or URL of the default Git repository to remove from this notebook instance. This operation is idempotent. If you specify a Git repository that is not associated with the notebook instance when you call this method, it does not throw an error.</p>"""
    disassociate_additional_code_repositories: NotRequired[
        "aws_sdk_sagemaker.types.disassociate_additional_code_repositories.DisassociateAdditionalCodeRepositories"
    ]
    """<p>A list of names or URLs of the default Git repositories to remove from this notebook instance. This operation is idempotent. If you specify a Git repository that is not associated with the notebook instance when you call this method, it does not throw an error.</p>"""
    root_access: NotRequired["aws_sdk_sagemaker.types.root_access.RootAccess"]
    """<p>Whether root access is enabled or disabled for users of the notebook instance. The default value is <code>Enabled</code>.</p> <note> <p>If you set this to <code>Disabled</code>, users don't have root access on the notebook instance, but lifecycle configuration scripts still run with root permissions.</p> </note>"""
    instance_metadata_service_configuration: NotRequired[
        "aws_sdk_sagemaker.types.instance_metadata_service_configuration.InstanceMetadataServiceConfiguration"
    ]
    """<p>Information on the IMDS configuration of the notebook instance</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotebookInstanceInput) -> dict:
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
    if "ip_address_type" in value:
        import aws_sdk_sagemaker.types.ip_address_type

        out["IpAddressType"] = (
            aws_sdk_sagemaker.types.ip_address_type.serialize_aws_json_1_1(
                value["ip_address_type"]
            )
        )
    if "platform_identifier" in value:
        out["PlatformIdentifier"] = value["platform_identifier"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "lifecycle_config_name" in value:
        out["LifecycleConfigName"] = value["lifecycle_config_name"]
    if "disassociate_lifecycle_config" in value:
        out["DisassociateLifecycleConfig"] = value["disassociate_lifecycle_config"]
    if "volume_size_in_gb" in value:
        out["VolumeSizeInGB"] = value["volume_size_in_gb"]
    if "default_code_repository" in value:
        out["DefaultCodeRepository"] = value["default_code_repository"]
    if "additional_code_repositories" in value:
        import aws_sdk_sagemaker.types.additional_code_repository_names_or_urls

        out["AdditionalCodeRepositories"] = (
            aws_sdk_sagemaker.types.additional_code_repository_names_or_urls.serialize_aws_json_1_1(
                value["additional_code_repositories"]
            )
        )
    if "accelerator_types" in value:
        import aws_sdk_sagemaker.types.notebook_instance_accelerator_types

        out["AcceleratorTypes"] = (
            aws_sdk_sagemaker.types.notebook_instance_accelerator_types.serialize_aws_json_1_1(
                value["accelerator_types"]
            )
        )
    if "disassociate_accelerator_types" in value:
        out["DisassociateAcceleratorTypes"] = value["disassociate_accelerator_types"]
    if "disassociate_default_code_repository" in value:
        out["DisassociateDefaultCodeRepository"] = value[
            "disassociate_default_code_repository"
        ]
    if "disassociate_additional_code_repositories" in value:
        out["DisassociateAdditionalCodeRepositories"] = value[
            "disassociate_additional_code_repositories"
        ]
    if "root_access" in value:
        import aws_sdk_sagemaker.types.root_access

        out["RootAccess"] = aws_sdk_sagemaker.types.root_access.serialize_aws_json_1_1(
            value["root_access"]
        )
    if "instance_metadata_service_configuration" in value:
        import aws_sdk_sagemaker.types.instance_metadata_service_configuration

        out["InstanceMetadataServiceConfiguration"] = (
            aws_sdk_sagemaker.types.instance_metadata_service_configuration.serialize_aws_json_1_1(
                value["instance_metadata_service_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotebookInstanceInput:
    out: UpdateNotebookInstanceInput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceName" in data:
        out["notebook_instance_name"] = data["NotebookInstanceName"]
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
    if "PlatformIdentifier" in data:
        out["platform_identifier"] = data["PlatformIdentifier"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "LifecycleConfigName" in data:
        out["lifecycle_config_name"] = data["LifecycleConfigName"]
    if "DisassociateLifecycleConfig" in data:
        out["disassociate_lifecycle_config"] = data["DisassociateLifecycleConfig"]
    if "VolumeSizeInGB" in data:
        out["volume_size_in_gb"] = data["VolumeSizeInGB"]
    if "DefaultCodeRepository" in data:
        out["default_code_repository"] = data["DefaultCodeRepository"]
    if "AdditionalCodeRepositories" in data:
        import aws_sdk_sagemaker.types.additional_code_repository_names_or_urls

        out["additional_code_repositories"] = (
            aws_sdk_sagemaker.types.additional_code_repository_names_or_urls.deserialize_aws_json_1_1(
                data["AdditionalCodeRepositories"]
            )
        )
    if "AcceleratorTypes" in data:
        import aws_sdk_sagemaker.types.notebook_instance_accelerator_types

        out["accelerator_types"] = (
            aws_sdk_sagemaker.types.notebook_instance_accelerator_types.deserialize_aws_json_1_1(
                data["AcceleratorTypes"]
            )
        )
    if "DisassociateAcceleratorTypes" in data:
        out["disassociate_accelerator_types"] = data["DisassociateAcceleratorTypes"]
    if "DisassociateDefaultCodeRepository" in data:
        out["disassociate_default_code_repository"] = data[
            "DisassociateDefaultCodeRepository"
        ]
    if "DisassociateAdditionalCodeRepositories" in data:
        out["disassociate_additional_code_repositories"] = data[
            "DisassociateAdditionalCodeRepositories"
        ]
    if "RootAccess" in data:
        import aws_sdk_sagemaker.types.root_access

        out["root_access"] = (
            aws_sdk_sagemaker.types.root_access.deserialize_aws_json_1_1(
                data["RootAccess"]
            )
        )
    if "InstanceMetadataServiceConfiguration" in data:
        import aws_sdk_sagemaker.types.instance_metadata_service_configuration

        out["instance_metadata_service_configuration"] = (
            aws_sdk_sagemaker.types.instance_metadata_service_configuration.deserialize_aws_json_1_1(
                data["InstanceMetadataServiceConfiguration"]
            )
        )
    return out
