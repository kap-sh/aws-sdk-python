"""Generated from Smithy shape ``com.amazonaws.codecommit#MergeBranchesByThreeWayOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id


class MergeBranchesByThreeWayOutput(TypedDict, closed=True):
    commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge in the destination or target branch.</p>"""
    tree_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The tree ID of the merge in the destination or target branch.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MergeBranchesByThreeWayOutput) -> dict:
    out: dict = {}
    if "commit_id" in value:
        out["commitId"] = value["commit_id"]
    if "tree_id" in value:
        out["treeId"] = value["tree_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> MergeBranchesByThreeWayOutput:
    out: MergeBranchesByThreeWayOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    return out
