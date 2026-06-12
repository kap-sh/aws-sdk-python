"""Generated from Smithy shape ``com.amazonaws.codegurureviewer#CommitDiffSourceCodeType``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codeguru_reviewer.types.commit_id


class CommitDiffSourceCodeType(TypedDict):
    source_commit: NotRequired["aws_sdk_codeguru_reviewer.types.commit_id.CommitId"]
    """<p>The SHA of the source commit used to generate a commit diff. This field is required for a pull request code review.</p>"""
    destination_commit: NotRequired[
        "aws_sdk_codeguru_reviewer.types.commit_id.CommitId"
    ]
    """<p>The SHA of the destination commit used to generate a commit diff. This field is required for a pull request code review.</p>"""
    merge_base_commit: NotRequired["aws_sdk_codeguru_reviewer.types.commit_id.CommitId"]
    """<p>The SHA of the merge base of a commit.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CommitDiffSourceCodeType) -> dict:
    out: dict = {}
    if "source_commit" in value:
        out["SourceCommit"] = value["source_commit"]
    if "destination_commit" in value:
        out["DestinationCommit"] = value["destination_commit"]
    if "merge_base_commit" in value:
        out["MergeBaseCommit"] = value["merge_base_commit"]
    return out


def deserialize_json(data: dict) -> CommitDiffSourceCodeType:
    out: CommitDiffSourceCodeType = {}  # type: ignore[typeddict-item]
    if "SourceCommit" in data:
        out["source_commit"] = data["SourceCommit"]
    if "DestinationCommit" in data:
        out["destination_commit"] = data["DestinationCommit"]
    if "MergeBaseCommit" in data:
        out["merge_base_commit"] = data["MergeBaseCommit"]
    return out
