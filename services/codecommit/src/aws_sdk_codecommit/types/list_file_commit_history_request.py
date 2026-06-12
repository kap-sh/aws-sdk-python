"""Generated from Smithy shape ``com.amazonaws.codecommit#ListFileCommitHistoryRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit_name
    import aws_sdk_codecommit.types.limit
    import aws_sdk_codecommit.types.next_token
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.repository_name


class ListFileCommitHistoryRequest(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the file.</p>"""
    commit_specifier: NotRequired["aws_sdk_codecommit.types.commit_name.CommitName"]
    """<p>The fully quaified reference that identifies the commit that contains the file. For example, you can specify a full commit ID, a tag, a branch name, or a reference such as <code>refs/heads/main</code>. If none is provided, the head commit is used.</p>"""
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The full path of the file whose history you want to retrieve, including the name of the file.</p>"""
    max_results: NotRequired["aws_sdk_codecommit.types.limit.Limit"]
    """<p>A non-zero, non-negative integer used to limit the number of returned results.</p>"""
    next_token: NotRequired["aws_sdk_codecommit.types.next_token.NextToken"]
    """<p>An enumeration token that allows the operation to batch the results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListFileCommitHistoryRequest) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "commit_specifier" in value:
        out["commitSpecifier"] = value["commit_specifier"]
    out["filePath"] = value["file_path"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListFileCommitHistoryRequest:
    out: ListFileCommitHistoryRequest = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "ListFileCommitHistoryRequest.repository_name required"
        )
    if "commitSpecifier" in data:
        out["commit_specifier"] = data["commitSpecifier"]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("ListFileCommitHistoryRequest.file_path required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
