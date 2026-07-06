"""Generated from Smithy shape ``com.amazonaws.codecommit#RepositoryMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.account_id
    import aws_sdk_codecommit.types.arn
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.clone_url_http
    import aws_sdk_codecommit.types.clone_url_ssh
    import aws_sdk_codecommit.types.creation_date
    import aws_sdk_codecommit.types.kms_key_id
    import aws_sdk_codecommit.types.last_modified_date
    import aws_sdk_codecommit.types.repository_description
    import aws_sdk_codecommit.types.repository_id
    import aws_sdk_codecommit.types.repository_name


class RepositoryMetadata(TypedDict, closed=True):
    account_id: NotRequired["aws_sdk_codecommit.types.account_id.AccountId"]
    """<p>The ID of the Amazon Web Services account associated with the repository.</p>"""
    repository_id: NotRequired["aws_sdk_codecommit.types.repository_id.RepositoryId"]
    """<p>The ID of the repository.</p>"""
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The repository's name.</p>"""
    repository_description: NotRequired[
        "aws_sdk_codecommit.types.repository_description.RepositoryDescription"
    ]
    """<p>A comment or description about the repository.</p>"""
    default_branch: NotRequired["aws_sdk_codecommit.types.branch_name.BranchName"]
    """<p>The repository's default branch name.</p>"""
    last_modified_date: NotRequired[
        "aws_sdk_codecommit.types.last_modified_date.LastModifiedDate"
    ]
    """<p>The date and time the repository was last modified, in timestamp format.</p>"""
    creation_date: NotRequired["aws_sdk_codecommit.types.creation_date.CreationDate"]
    """<p>The date and time the repository was created, in timestamp format.</p>"""
    clone_url_http: NotRequired["aws_sdk_codecommit.types.clone_url_http.CloneUrlHttp"]
    """<p>The URL to use for cloning the repository over HTTPS.</p>"""
    clone_url_ssh: NotRequired["aws_sdk_codecommit.types.clone_url_ssh.CloneUrlSsh"]
    """<p>The URL to use for cloning the repository over SSH.</p>"""
    arn: NotRequired["aws_sdk_codecommit.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the repository.</p>"""
    kms_key_id: NotRequired["aws_sdk_codecommit.types.kms_key_id.KmsKeyId"]
    """<p>The ID of the Key Management Service encryption key used to encrypt and decrypt the repository.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RepositoryMetadata) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "repository_id" in value:
        out["repositoryId"] = value["repository_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "repository_description" in value:
        out["repositoryDescription"] = value["repository_description"]
    if "default_branch" in value:
        out["defaultBranch"] = value["default_branch"]
    if "last_modified_date" in value:
        import aws_sdk_codecommit.types.last_modified_date

        out["lastModifiedDate"] = (
            aws_sdk_codecommit.types.last_modified_date.serialize_aws_json_1_1(
                value["last_modified_date"]
            )
        )
    if "creation_date" in value:
        import aws_sdk_codecommit.types.creation_date

        out["creationDate"] = (
            aws_sdk_codecommit.types.creation_date.serialize_aws_json_1_1(
                value["creation_date"]
            )
        )
    if "clone_url_http" in value:
        out["cloneUrlHttp"] = value["clone_url_http"]
    if "clone_url_ssh" in value:
        out["cloneUrlSsh"] = value["clone_url_ssh"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "kms_key_id" in value:
        out["kmsKeyId"] = value["kms_key_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RepositoryMetadata:
    out: RepositoryMetadata = {}  # type: ignore[typeddict-item]
    if "accountId" in data:
        out["account_id"] = data["accountId"]
    if "repositoryId" in data:
        out["repository_id"] = data["repositoryId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "repositoryDescription" in data:
        out["repository_description"] = data["repositoryDescription"]
    if "defaultBranch" in data:
        out["default_branch"] = data["defaultBranch"]
    if "lastModifiedDate" in data:
        import aws_sdk_codecommit.types.last_modified_date

        out["last_modified_date"] = (
            aws_sdk_codecommit.types.last_modified_date.deserialize_aws_json_1_1(
                data["lastModifiedDate"]
            )
        )
    if "creationDate" in data:
        import aws_sdk_codecommit.types.creation_date

        out["creation_date"] = (
            aws_sdk_codecommit.types.creation_date.deserialize_aws_json_1_1(
                data["creationDate"]
            )
        )
    if "cloneUrlHttp" in data:
        out["clone_url_http"] = data["cloneUrlHttp"]
    if "cloneUrlSsh" in data:
        out["clone_url_ssh"] = data["cloneUrlSsh"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "kmsKeyId" in data:
        out["kms_key_id"] = data["kmsKeyId"]
    return out
