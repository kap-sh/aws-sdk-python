"""Generated from Smithy shape ``com.amazonaws.codecatalyst#CreateSourceRepositoryBranchResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecatalyst.types.source_repository_branch_ref_string
    import capo_codecatalyst.types.source_repository_branch_string
    import capo_codecatalyst.types.timestamp


class CreateSourceRepositoryBranchResponse(TypedDict, closed=True):
    ref: NotRequired[
        "capo_codecatalyst.types.source_repository_branch_ref_string.SourceRepositoryBranchRefString"
    ]
    """<p>The Git reference name of the branch.</p>"""
    name: NotRequired[
        "capo_codecatalyst.types.source_repository_branch_string.SourceRepositoryBranchString"
    ]
    """<p>The name of the newly created branch.</p>"""
    last_updated_time: NotRequired["capo_codecatalyst.types.timestamp.Timestamp"]
    r"""<p>The time the branch was last updated, in coordinated universal time (UTC) timestamp format as specified in <a href=\"https://www.rfc-editor.org/rfc/rfc3339#section-5.6\">RFC 3339</a>.</p>"""
    head_commit_id: NotRequired["str"]
    """<p>The commit ID of the tip of the newly created branch.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateSourceRepositoryBranchResponse) -> dict:
    out: dict = {}
    if "ref" in value:
        out["ref"] = value["ref"]
    if "name" in value:
        out["name"] = value["name"]
    if "last_updated_time" in value:
        import capo_codecatalyst.types.timestamp

        out["lastUpdatedTime"] = capo_codecatalyst.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "head_commit_id" in value:
        out["headCommitId"] = value["head_commit_id"]
    return out


def deserialize_json(data: dict) -> CreateSourceRepositoryBranchResponse:
    out: CreateSourceRepositoryBranchResponse = {}  # type: ignore[typeddict-item]
    if "ref" in data:
        out["ref"] = data["ref"]
    if "name" in data:
        out["name"] = data["name"]
    if "lastUpdatedTime" in data:
        import capo_codecatalyst.types.timestamp

        out["last_updated_time"] = capo_codecatalyst.types.timestamp.deserialize_json(
            data["lastUpdatedTime"]
        )
    if "headCommitId" in data:
        out["head_commit_id"] = data["headCommitId"]
    return out
