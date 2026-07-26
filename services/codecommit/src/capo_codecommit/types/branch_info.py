"""Generated from Smithy shape ``com.amazonaws.codecommit#BranchInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.branch_name
    import capo_codecommit.types.commit_id


class BranchInfo(TypedDict, closed=True):
    branch_name: NotRequired["capo_codecommit.types.branch_name.BranchName"]
    """<p>The name of the branch.</p>"""
    commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The ID of the last commit made to the branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BranchInfo) -> dict:
    out: dict = {}
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BranchInfo:
    out: BranchInfo = {}  # type: ignore[typeddict-item]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    return out
