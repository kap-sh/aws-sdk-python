"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateSourceRepositoryBranchRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.source_repository_branch_string
    import aws_sdk_codecatalyst.types.source_repository_name_string


class CreateSourceRepositoryBranchRequest(TypedDict):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    source_repository_name: "aws_sdk_codecatalyst.types.source_repository_name_string.SourceRepositoryNameString"
    """<p>The name of the repository where you want to create a branch.</p>"""
    name: "aws_sdk_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    """<p>The name for the branch you're creating.</p>"""
    head_commit_id: NotRequired["str"]
    """<p>The commit ID in an existing branch from which you want to create the new branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceRepositoryBranchRequest) -> dict:
    out: dict = {}
    if "head_commit_id" in value:
        out["headCommitId"] = value["head_commit_id"]
    return out


def deserialize_json(data: dict) -> CreateSourceRepositoryBranchRequest:
    out: CreateSourceRepositoryBranchRequest = {}  # type: ignore[typeddict-item]
    if "headCommitId" in data:
        out["head_commit_id"] = data["headCommitId"]
    return out
