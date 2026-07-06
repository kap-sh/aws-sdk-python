"""Generated from Smithy shape ``com.amazonaws.proton#UpdateAccountSettingsInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_proton.types.repository_branch_input
    import aws_sdk_proton.types.role_arn_or_empty_string


class UpdateAccountSettingsInput(TypedDict, closed=True):
    pipeline_service_role_arn: NotRequired[
        "aws_sdk_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Assumed by Proton for Amazon Web Services-managed provisioning, and by customer-owned automation for self-managed provisioning.</p> <p>To remove a previously configured ARN, specify an empty string.</p>"""
    pipeline_provisioning_repository: NotRequired[
        "aws_sdk_proton.types.repository_branch_input.RepositoryBranchInput"
    ]
    """<p>A linked repository for pipeline provisioning. Specify it if you have environments configured for self-managed provisioning with services that include pipelines. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p> <p>To remove a previously configured repository, set <code>deletePipelineProvisioningRepository</code> to <code>true</code>, and don't set <code>pipelineProvisioningRepository</code>.</p>"""
    delete_pipeline_provisioning_repository: NotRequired["bool"]
    """<p>Set to <code>true</code> to remove a configured pipeline repository from the account settings. Don't set this field if you are updating the configured pipeline repository.</p>"""
    pipeline_codebuild_role_arn: NotRequired[
        "aws_sdk_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"
    ]
    """<p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Proton assumes this role for CodeBuild-based provisioning.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateAccountSettingsInput) -> dict:
    out: dict = {}
    if "pipeline_service_role_arn" in value:
        out["pipelineServiceRoleArn"] = value["pipeline_service_role_arn"]
    if "pipeline_provisioning_repository" in value:
        import aws_sdk_proton.types.repository_branch_input

        out["pipelineProvisioningRepository"] = (
            aws_sdk_proton.types.repository_branch_input.serialize_aws_json_1_0(
                value["pipeline_provisioning_repository"]
            )
        )
    if "delete_pipeline_provisioning_repository" in value:
        out["deletePipelineProvisioningRepository"] = value[
            "delete_pipeline_provisioning_repository"
        ]
    if "pipeline_codebuild_role_arn" in value:
        out["pipelineCodebuildRoleArn"] = value["pipeline_codebuild_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateAccountSettingsInput:
    out: UpdateAccountSettingsInput = {}  # type: ignore[typeddict-item]
    if "pipelineServiceRoleArn" in data:
        out["pipeline_service_role_arn"] = data["pipelineServiceRoleArn"]
    if "pipelineProvisioningRepository" in data:
        import aws_sdk_proton.types.repository_branch_input

        out["pipeline_provisioning_repository"] = (
            aws_sdk_proton.types.repository_branch_input.deserialize_aws_json_1_0(
                data["pipelineProvisioningRepository"]
            )
        )
    if "deletePipelineProvisioningRepository" in data:
        out["delete_pipeline_provisioning_repository"] = data[
            "deletePipelineProvisioningRepository"
        ]
    if "pipelineCodebuildRoleArn" in data:
        out["pipeline_codebuild_role_arn"] = data["pipelineCodebuildRoleArn"]
    return out
