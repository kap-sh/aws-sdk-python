"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBranchInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.branch_name
    import aws_sdk_codecommit.types.repository_name


class GetBranchInput(TypedDict):
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository that contains the branch for which you want to retrieve information.</p>"""
    branch_name: NotRequired["aws_sdk_codecommit.types.branch_name.BranchName"]
    """<p>The name of the branch for which you want to retrieve information.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBranchInput) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBranchInput:
    out: GetBranchInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    return out
