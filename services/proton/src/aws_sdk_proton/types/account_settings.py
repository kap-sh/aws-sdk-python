"""Generated from Smithy shape ``com.amazonaws.proton#AccountSettings``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired
if TYPE_CHECKING:
    import aws_sdk_proton.types.repository_branch
    import aws_sdk_proton.types.role_arn_or_empty_string

class AccountSettings(TypedDict):
    pipeline_service_role_arn: NotRequired["aws_sdk_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the service role you want to use for provisioning pipelines. Assumed by Proton for Amazon Web Services-managed provisioning, and by customer-owned automation for self-managed provisioning.</p>"""
    pipeline_provisioning_repository: NotRequired["aws_sdk_proton.types.repository_branch.RepositoryBranch"]
    """<p>The linked repository for pipeline provisioning. Required if you have environments configured for self-managed provisioning with services that include pipelines. A linked repository is a repository that has been registered with Proton. For more information, see <a>CreateRepository</a>.</p>"""
    pipeline_codebuild_role_arn: NotRequired["aws_sdk_proton.types.role_arn_or_empty_string.RoleArnOrEmptyString"]
    """<p>The Amazon Resource Name (ARN) of the service role that Proton uses for provisioning pipelines. Proton assumes this role for CodeBuild-based provisioning.</p>"""

# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AccountSettings) -> dict:
    out: dict = {}
    if "pipeline_service_role_arn" in value:
        out["pipelineServiceRoleArn"] = value["pipeline_service_role_arn"]
    if "pipeline_provisioning_repository" in value:
        import aws_sdk_proton.types.repository_branch
        out["pipelineProvisioningRepository"] = aws_sdk_proton.types.repository_branch.serialize_aws_json_1_0(value["pipeline_provisioning_repository"])
    if "pipeline_codebuild_role_arn" in value:
        out["pipelineCodebuildRoleArn"] = value["pipeline_codebuild_role_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AccountSettings:
    out: AccountSettings = {}  # type: ignore[typeddict-item]
    if "pipelineServiceRoleArn" in data:
        out["pipeline_service_role_arn"] = data["pipelineServiceRoleArn"]
    if "pipelineProvisioningRepository" in data:
        import aws_sdk_proton.types.repository_branch
        out["pipeline_provisioning_repository"] = aws_sdk_proton.types.repository_branch.deserialize_aws_json_1_0(data["pipelineProvisioningRepository"])
    if "pipelineCodebuildRoleArn" in data:
        out["pipeline_codebuild_role_arn"] = data["pipelineCodebuildRoleArn"]
    return out