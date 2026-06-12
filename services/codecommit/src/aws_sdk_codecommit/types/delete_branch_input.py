"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteBranchInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.repository_name


class DeleteBranchInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the branch to be deleted.</p>"""
    branch_name: "aws_sdk_codecommit.types.branch_name.BranchName"
    """<p>The name of the branch to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBranchInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["branchName"] = value["branch_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBranchInput:
    out: DeleteBranchInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("DeleteBranchInput.repository_name required")
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    else:
        raise DeserializationError("DeleteBranchInput.branch_name required")
    return out
