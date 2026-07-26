"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestSourceReferenceUpdatedEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.repository_name


class PullRequestSourceReferenceUpdatedEventMetadata(TypedDict, closed=True):
    repository_name: NotRequired["capo_codecommit.types.repository_name.RepositoryName"]
    """<p>The name of the repository where the pull request was updated.</p>"""
    before_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was updated.</p>"""
    after_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit in the source branch that was the tip of the branch at the time the pull request was updated.</p>"""
    merge_base: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The commit ID of the most recent commit that the source branch and the destination branch have in common.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: PullRequestSourceReferenceUpdatedEventMetadata,
) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "before_commit_id" in value:
        out["beforeCommitId"] = value["before_commit_id"]
    if "after_commit_id" in value:
        out["afterCommitId"] = value["after_commit_id"]
    if "merge_base" in value:
        out["mergeBase"] = value["merge_base"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> PullRequestSourceReferenceUpdatedEventMetadata:
    out: PullRequestSourceReferenceUpdatedEventMetadata = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "beforeCommitId" in data:
        out["before_commit_id"] = data["beforeCommitId"]
    if "afterCommitId" in data:
        out["after_commit_id"] = data["afterCommitId"]
    if "mergeBase" in data:
        out["merge_base"] = data["mergeBase"]
    return out
