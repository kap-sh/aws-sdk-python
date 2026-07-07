"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateBranchInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.repository_name


class CreateBranchInput(TypedDict, closed=True):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository in which you want to create the new branch.</p>"""
    branch_name: "aws_sdk_codecommit.types.branch_name.BranchName"
    """<p>The name of the new branch to create.</p>"""
    commit_id: "aws_sdk_codecommit.types.commit_id.CommitId"
    """<p>The ID of the commit to point the new branch to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateBranchInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    out["commitId"] = value["commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateBranchInput:
    out: CreateBranchInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("CreateBranchInput.repository_name required")
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("CreateBranchInput.branch_name required")
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    else:
        raise DeserializationError("CreateBranchInput.commit_id required")
    return out
