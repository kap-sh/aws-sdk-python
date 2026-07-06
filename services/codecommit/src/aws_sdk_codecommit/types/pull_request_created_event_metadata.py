"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestCreatedEventMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.repository_name


class PullRequestCreatedEventMetadata(TypedDict, closed=True):
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository where the pull request was created.</p>"""
    source_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The commit ID on the source branch used when the pull request was created.</p>"""
    destination_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The commit ID of the tip of the branch specified as the destination branch when the pull request was created.</p>"""
    merge_base: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The commit ID of the most recent commit that the source branch and the destination branch have in common.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestCreatedEventMetadata) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "source_commit_id" in value:
        out["sourceCommitId"] = value["source_commit_id"]
    if "destination_commit_id" in value:
        out["destinationCommitId"] = value["destination_commit_id"]
    if "merge_base" in value:
        out["mergeBase"] = value["merge_base"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequestCreatedEventMetadata:
    out: PullRequestCreatedEventMetadata = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "sourceCommitId" in data:
        out["source_commit_id"] = data["sourceCommitId"]
    if "destinationCommitId" in data:
        out["destination_commit_id"] = data["destinationCommitId"]
    if "mergeBase" in data:
        out["merge_base"] = data["mergeBase"]
    return out
