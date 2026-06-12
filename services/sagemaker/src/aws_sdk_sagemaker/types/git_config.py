"""Generated from Smithy shape ``com.amazonaws.sagemaker#GitConfig``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.branch
    import aws_sdk_sagemaker.types.git_config_url
    import aws_sdk_sagemaker.types.secret_arn


class GitConfig(TypedDict):
    repository_url: NotRequired["aws_sdk_sagemaker.types.git_config_url.GitConfigUrl"]
    """<p>The URL where the Git repository is located.</p>"""
    branch: NotRequired["aws_sdk_sagemaker.types.branch.Branch"]
    """<p>The default branch for the Git repository.</p>"""
    secret_arn: NotRequired["aws_sdk_sagemaker.types.secret_arn.SecretArn"]
    """<p>The Amazon Resource Name (ARN) of the Amazon Web Services Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of <code>AWSCURRENT</code> and must be in the following format:</p> <p> <code>{\"username\": <i>UserName</i>, \"password\": <i>Password</i>}</code> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GitConfig) -> dict:
    out: dict = {}
    if "repository_url" in value:
        out["RepositoryUrl"] = value["repository_url"]
    if "branch" in value:
        out["Branch"] = value["branch"]
    if "secret_arn" in value:
        out["SecretArn"] = value["secret_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GitConfig:
    out: GitConfig = {}  # type: ignore[typeddict-item]
    if "RepositoryUrl" in data:
        out["repository_url"] = data["RepositoryUrl"]
    if "Branch" in data:
        out["branch"] = data["Branch"]
    if "SecretArn" in data:
        out["secret_arn"] = data["SecretArn"]
    return out
