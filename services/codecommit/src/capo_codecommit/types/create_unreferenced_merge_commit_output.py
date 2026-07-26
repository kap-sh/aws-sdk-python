"""Generated from Smithy shape ``com.amazonaws.codecommit#CreateUnreferencedMergeCommitOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.object_id


class CreateUnreferencedMergeCommitOutput(TypedDict, closed=True):
    commit_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full commit ID of the commit that contains your merge results.</p>"""
    tree_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full SHA-1 pointer of the tree information for the commit that contains the merge results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateUnreferencedMergeCommitOutput) -> dict:
    out: dict = {}
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateUnreferencedMergeCommitOutput:
    out: CreateUnreferencedMergeCommitOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    return out
