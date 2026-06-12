"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeBranchesByFastForwardOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id


class MergeBranchesByFastForwardOutput(TypedDict):
    commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge in the destination or target branch.</p>"""
    tree_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The tree ID of the merge in the destination or target branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeBranchesByFastForwardOutput) -> dict:
    out: dict = {}
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeBranchesByFastForwardOutput:
    out: MergeBranchesByFastForwardOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    return out
