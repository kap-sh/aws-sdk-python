"""Generated from Smithy shape ``com.amazonaws.glue#UpdateJobFromSourceControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_glue.types.auth_token_string
    import aws_sdk_glue.types.commit_id_string
    import aws_sdk_glue.types.name_string
    import aws_sdk_glue.types.source_control_auth_strategy
    import aws_sdk_glue.types.source_control_provider


class UpdateJobFromSourceControlRequest(TypedDict, closed=True):
    job_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the Glue job to be synchronized to or from the remote repository.</p>"""
    provider: NotRequired[
        "aws_sdk_glue.types.source_control_provider.SourceControlProvider"
    ]
    """<p> The provider for the remote repository. Possible values: GITHUB, AWS_CODE_COMMIT, GITLAB, BITBUCKET. </p>"""
    repository_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The name of the remote repository that contains the job artifacts. For BitBucket providers, <code>RepositoryName</code> should include <code>WorkspaceName</code>. Use the format <code><WorkspaceName>/<RepositoryName></code>. </p>"""
    repository_owner: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>The owner of the remote repository that contains the job artifacts.</p>"""
    branch_name: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>An optional branch in the remote repository.</p>"""
    folder: NotRequired["aws_sdk_glue.types.name_string.NameString"]
    """<p>An optional folder in the remote repository.</p>"""
    commit_id: NotRequired["aws_sdk_glue.types.commit_id_string.CommitIdString"]
    """<p>A commit ID for a commit in the remote repository.</p>"""
    auth_strategy: NotRequired[
        "aws_sdk_glue.types.source_control_auth_strategy.SourceControlAuthStrategy"
    ]
    """<p>The type of authentication, which can be an authentication token stored in Amazon Web Services Secrets Manager, or a personal access token.</p>"""
    auth_token: NotRequired["aws_sdk_glue.types.auth_token_string.AuthTokenString"]
    """<p>The value of the authorization token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateJobFromSourceControlRequest) -> dict:
    out: dict = {}
    if "job_name" in value:
        out["JobName"] = value["job_name"]
    if "provider" in value:
        import aws_sdk_glue.types.source_control_provider

        out["Provider"] = (
            aws_sdk_glue.types.source_control_provider.serialize_aws_json_1_1(
                value["provider"]
            )
        )
    if "repository_name" in value:
        out["RepositoryName"] = value["repository_name"]
    if "repository_owner" in value:
        out["RepositoryOwner"] = value["repository_owner"]
    if "branch_name" in value:
        out["BranchName"] = value["branch_name"]
    if "folder" in value:
        out["Folder"] = value["folder"]
    if "commit_id" in value:
        out["CommitId"] = value["commit_id"]
    if "auth_strategy" in value:
        import aws_sdk_glue.types.source_control_auth_strategy

        out["AuthStrategy"] = (
            aws_sdk_glue.types.source_control_auth_strategy.serialize_aws_json_1_1(
                value["auth_strategy"]
            )
        )
    if "auth_token" in value:
        out["AuthToken"] = value["auth_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateJobFromSourceControlRequest:
    out: UpdateJobFromSourceControlRequest = {}  # type: ignore[typeddict-item]
    if "JobName" in data:
        out["job_name"] = data["JobName"]
    if "Provider" in data:
        import aws_sdk_glue.types.source_control_provider

        out["provider"] = (
            aws_sdk_glue.types.source_control_provider.deserialize_aws_json_1_1(
                data["Provider"]
            )
        )
    if "RepositoryName" in data:
        out["repository_name"] = data["RepositoryName"]
    if "RepositoryOwner" in data:
        out["repository_owner"] = data["RepositoryOwner"]
    if "BranchName" in data:
        out["branch_name"] = data["BranchName"]
    if "Folder" in data:
        out["folder"] = data["Folder"]
    if "CommitId" in data:
        out["commit_id"] = data["CommitId"]
    if "AuthStrategy" in data:
        import aws_sdk_glue.types.source_control_auth_strategy

        out["auth_strategy"] = (
            aws_sdk_glue.types.source_control_auth_strategy.deserialize_aws_json_1_1(
                data["AuthStrategy"]
            )
        )
    if "AuthToken" in data:
        out["auth_token"] = data["AuthToken"]
    return out
