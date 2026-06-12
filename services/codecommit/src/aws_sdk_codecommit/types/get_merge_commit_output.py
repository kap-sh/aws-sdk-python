"""Generated from Smithy shape ``com.amazonaws.codecommit#GetMergeCommitOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id


class GetMergeCommitOutput(TypedDict):
    source_commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the source commit specifier that was used in the merge evaluation.</p>"""
    destination_commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the destination commit specifier that was used in the merge evaluation.</p>"""
    base_commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID of the merge base.</p>"""
    merged_commit_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The commit ID for the merge commit created when the source branch was merged into the destination branch. If the fast-forward merge strategy was used, there is no merge commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetMergeCommitOutput) -> dict:
    out: dict = {}
    if "source_commit_id" in value:
        out["sourceCommitId"] = value["source_commit_id"]
    if "destination_commit_id" in value:
        out["destinationCommitId"] = value["destination_commit_id"]
    if "base_commit_id" in value:
        out["baseCommitId"] = value["base_commit_id"]
    if "merged_commit_id" in value:
        out["mergedCommitId"] = value["merged_commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetMergeCommitOutput:
    out: GetMergeCommitOutput = {}  # type: ignore[typeddict-item]
    if "sourceCommitId" in data:
        out["source_commit_id"] = data["sourceCommitId"]
    if "destinationCommitId" in data:
        out["destination_commit_id"] = data["destinationCommitId"]
    if "baseCommitId" in data:
        out["base_commit_id"] = data["baseCommitId"]
    if "mergedCommitId" in data:
        out["merged_commit_id"] = data["mergedCommitId"]
    return out
