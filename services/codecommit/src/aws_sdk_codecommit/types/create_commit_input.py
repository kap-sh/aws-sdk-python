"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateCommitInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.delete_file_entries
    import aws_sdk_codecommit.types.email
    import aws_sdk_codecommit.types.keep_empty_folders
    import aws_sdk_codecommit.types.message
    import aws_sdk_codecommit.types.name
    import aws_sdk_codecommit.types.put_file_entries
    import aws_sdk_codecommit.types.repository_name
    import aws_sdk_codecommit.types.set_file_mode_entries


class CreateCommitInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you create the commit.</p>"""
    branch_name: "aws_sdk_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch where you create the commit.</p>"""
    parent_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The ID of the commit that is the parent of the commit you create. Not required if this is an empty repository.</p>"""
    author_name: NotRequired["aws_sdk_codecommit.types.name.Name"]
    """<p>The name of the author who created the commit. This information is used as both the author and committer for the commit.</p>"""
    email: NotRequired["aws_sdk_codecommit.types.email.Email"]
    """<p>The email address of the person who created the commit.</p>"""
    commit_message: NotRequired["aws_sdk_codecommit.types.message.Message"]
    """<p>The commit message you want to include in the commit. Commit messages are limited to 256 KB. If no message is specified, a default message is used.</p>"""
    keep_empty_folders: "aws_sdk_codecommit.types.keep_empty_folders.KeepEmptyFolders"
    """<p>If the commit contains deletions, whether to keep a folder or folder structure if the changes leave the folders empty. If true, a ..gitkeep file is created for empty folders. The default is false.</p>"""
    put_files: NotRequired["aws_sdk_codecommit.types.put_file_entries.PutFileEntries"]
    """<p>The files to add or update in this commit.</p>"""
    delete_files: NotRequired[
        "aws_sdk_codecommit.types.delete_file_entries.DeleteFileEntries"
    ]
    """<p>The files to delete in this commit. These files still exist in earlier commits.</p>"""
    set_file_modes: NotRequired[
        "aws_sdk_codecommit.types.set_file_mode_entries.SetFileModeEntries"
    ]
    """<p>The file modes to update for files in this commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateCommitInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    if "parent_commit_id" in value:
        out["parentCommitId"] = value["parent_commit_id"]
    if "author_name" in value:
        out["authorName"] = value["author_name"]
    if "email" in value:
        out["email"] = value["email"]
    if "commit_message" in value:
        out["commitMessage"] = value["commit_message"]
    out["keepEmptyFolders"] = value.get("keep_empty_folders", False)
    if "put_files" in value:
        import aws_sdk_codecommit.types.put_file_entries

        out["putFiles"] = (
            aws_sdk_codecommit.types.put_file_entries.serialize_aws_json_1_1(
                value["put_files"]
            )
        )
    if "delete_files" in value:
        import aws_sdk_codecommit.types.delete_file_entries

        out["deleteFiles"] = (
            aws_sdk_codecommit.types.delete_file_entries.serialize_aws_json_1_1(
                value["delete_files"]
            )
        )
    if "set_file_modes" in value:
        import aws_sdk_codecommit.types.set_file_mode_entries

        out["setFileModes"] = (
            aws_sdk_codecommit.types.set_file_mode_entries.serialize_aws_json_1_1(
                value["set_file_modes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateCommitInput:
    out: CreateCommitInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("CreateCommitInput.repository_name required")
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("CreateCommitInput.branch_name required")
    if "parentCommitId" in data:
        out["parent_commit_id"] = data["parentCommitId"]
    if "authorName" in data:
        out["author_name"] = data["authorName"]
    if "email" in data:
        out["email"] = data["email"]
    if "commitMessage" in data:
        out["commit_message"] = data["commitMessage"]
    if "keepEmptyFolders" in data:
        out["keep_empty_folders"] = data["keepEmptyFolders"]
    else:
        out["keep_empty_folders"] = False
    if "putFiles" in data:
        import aws_sdk_codecommit.types.put_file_entries

        out["put_files"] = (
            aws_sdk_codecommit.types.put_file_entries.deserialize_aws_json_1_1(
                data["putFiles"]
            )
        )
    if "deleteFiles" in data:
        import aws_sdk_codecommit.types.delete_file_entries

        out["delete_files"] = (
            aws_sdk_codecommit.types.delete_file_entries.deserialize_aws_json_1_1(
                data["deleteFiles"]
            )
        )
    if "setFileModes" in data:
        import aws_sdk_codecommit.types.set_file_mode_entries

        out["set_file_modes"] = (
            aws_sdk_codecommit.types.set_file_mode_entries.deserialize_aws_json_1_1(
                data["setFileModes"]
            )
        )
    return out
