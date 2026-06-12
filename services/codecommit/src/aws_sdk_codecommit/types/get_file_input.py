"""Generated from Smithy shape ``com.amazonaws.codecommit#GetFileInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit_name
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.repository_name


class GetFileInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the file.</p>"""
    commit_specifier: NotRequired["aws_sdk_codecommit.types.commit_name.CommitName"]
    """<p>The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as refs/heads/main. If none is provided, the head commit is used.</p>"""
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The fully qualified path to the file, including the full name and extension of the file. For example, /examples/file.md is the fully qualified path to a file named file.md in a folder named examples.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetFileInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "commit_specifier" in value:
        out["commitSpecifier"] = value["commit_specifier"]
    out["filePath"] = value["file_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetFileInput:
    out: GetFileInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("GetFileInput.repository_name required")
    if "commitSpecifier" in data:
        out["commit_specifier"] = data["commitSpecifier"]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("GetFileInput.file_path required")
    return out
