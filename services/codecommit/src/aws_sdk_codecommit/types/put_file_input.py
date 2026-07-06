"""Generated from Smithy shape ``com.amazonaws.codecommit#PutFileInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.email
    import aws_sdk_codecommit.types.file_content
    import aws_sdk_codecommit.types.file_mode_type_enum
    import aws_sdk_codecommit.types.message
    import aws_sdk_codecommit.types.name
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.repository_name


class PutFileInput(TypedDict, closed=True):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to add or update the file.</p>"""
    branch_name: "aws_sdk_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch where you want to add or update the file. If this is an empty repository, this branch is created.</p>"""
    file_content: "aws_sdk_codecommit.types.file_content.FileContent"
    """<p>The content of the file, in binary object format. </p>"""
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The name of the file you want to add or update, including the relative path to the file in the repository.</p> <note> <p>If the path does not currently exist in the repository, the path is created as part of adding the file.</p> </note>"""
    file_mode: NotRequired[
        "aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    ]
    """<p>The file mode permissions of the blob. Valid file mode permissions are listed here.</p>"""
    parent_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the head commit in the branch where you want to add or update the file. If this is an empty repository, no commit ID is required. If this is not an empty repository, a commit ID is required. </p> <p>The commit ID must match the ID of the head commit at the time of the operation. Otherwise, an error occurs, and the file is not added or updated.</p>"""
    commit_message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>A message about why this file was added or updated. Although it is optional, a message makes the commit history for your repository more useful.</p>"""
    name: NotRequired["aws_sdk_codecommit.types.name.Name"]
    """<p>The name of the person adding or updating the file. Although it is optional, a name makes the commit history for your repository more useful.</p>"""
    email: NotRequired["aws_sdk_codecommit.types.email.Email"]
    """<p>An email address for the person adding or updating the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFileInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    import aws_sdk_codecommit.types.file_content

    out["fileContent"] = aws_sdk_codecommit.types.file_content.serialize_aws_json_1_1(
        value["file_content"]
    )
    out["filePath"] = value["file_path"]
    if "file_mode" in value:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    if "parent_commit_id" in value:
        out["parentCommitId"] = value["parent_commit_id"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    if "name" in value:
        out["name"] = value["name"]
    if "email" in value:
        out["email"] = value["email"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFileInput:
    out: PutFileInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("PutFileInput.repository_name required")
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("PutFileInput.branch_name required")
    if "fileContent" in data:
        import aws_sdk_codecommit.types.file_content

        out["file_content"] = (
            aws_sdk_codecommit.types.file_content.deserialize_aws_json_1_1(
                data["fileContent"]
            )
        )
    else:
        raise DeserializationError("PutFileInput.file_content required")
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("PutFileInput.file_path required")
    if "fileMode" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    if "parentCommitId" in data:
        out["parent_commit_id"] = data["parentCommitId"]
    if "commitMessage" in data:
        out["commit_message"] = data["commitMessage"]
    if "name" in data:
        out["name"] = data["name"]
    if "email" in data:
        out["email"] = data["email"]
    return out
