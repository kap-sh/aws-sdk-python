"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#VersionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.branch_name


class VersionFilter(TypedDict, closed=True):
    branch_name: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.branch_name.BranchName"
    ]
    """<p>Filter by branch name.</p>"""
    created_by_name: NotRequired["str"]
    """<p>Filter by creation source name.</p>"""
    latest_per_branch: NotRequired["bool"]
    """<p>When true, returns only the latest version for each branch. When false or not specified, returns all versions. Can be combined with <code>branchName</code> to get the latest version for a specific branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: VersionFilter) -> dict:
    out: dict = {}
    if "branch_name" in value:
        out["branchName"] = value["branch_name"]
    if "created_by_name" in value:
        out["createdByName"] = value["created_by_name"]
    if "latest_per_branch" in value:
        out["latestPerBranch"] = value["latest_per_branch"]
    return out


def deserialize_json(data: dict) -> VersionFilter:
    out: VersionFilter = {}  # type: ignore[typeddict-item]
    if "branchName" in data:
        out["branch_name"] = data["branchName"]
    if "createdByName" in data:
        out["created_by_name"] = data["createdByName"]
    if "latestPerBranch" in data:
        out["latest_per_branch"] = data["latestPerBranch"]
    return out
