"""Generated from Smithy shape ``com.amazonaws.codecommit#PullRequestTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.merge_metadata
    import aws_sdk_codecommit.types.reference_name
    import aws_sdk_codecommit.types.repository_name


class PullRequestTarget(TypedDict, closed=True):
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository that contains the pull request source and destination branches.</p>"""
    source_reference: NotRequired[
        "aws_sdk_codecommit.types.reference_name.ReferenceName"
    ]
    """<p>The branch of the repository that contains the changes for the pull request. Also known as the source branch.</p>"""
    destination_reference: NotRequired[
        "aws_sdk_codecommit.types.reference_name.ReferenceName"
    ]
    """<p>The branch of the repository where the pull request changes are merged. Also known as the destination branch. </p>"""
    destination_commit: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID that is the tip of the destination branch. This is the commit where the pull request was or will be merged.</p>"""
    source_commit: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the tip of the source branch used to create the pull request. If the pull request branch is updated by a push while the pull request is open, the commit ID changes to reflect the new tip of the branch.</p>"""
    merge_base: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The commit ID of the most recent commit that the source branch and the destination branch have in common.</p>"""
    merge_metadata: NotRequired["aws_sdk_codecommit.types.merge_metadata.MergeMetadata"]
    """<p>Returns metadata about the state of the merge, including whether the merge has been made.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PullRequestTarget) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "source_reference" in value:
        out["sourceReference"] = value["source_reference"]
    if "destination_reference" in value:
        out["destinationReference"] = value["destination_reference"]
    if "destination_commit" in value:
        out["destinationCommit"] = value["destination_commit"]
    if "source_commit" in value:
        out["sourceCommit"] = value["source_commit"]
    if "merge_base" in value:
        out["mergeBase"] = value["merge_base"]
    if "merge_metadata" in value:
        import aws_sdk_codecommit.types.merge_metadata

        out["mergeMetadata"] = (
            aws_sdk_codecommit.types.merge_metadata.serialize_aws_json_1_1(
                value["merge_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PullRequestTarget:
    out: PullRequestTarget = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "sourceReference" in data:
        out["source_reference"] = data["sourceReference"]
    if "destinationReference" in data:
        out["destination_reference"] = data["destinationReference"]
    if "destinationCommit" in data:
        out["destination_commit"] = data["destinationCommit"]
    if "sourceCommit" in data:
        out["source_commit"] = data["sourceCommit"]
    if "mergeBase" in data:
        out["merge_base"] = data["mergeBase"]
    if "mergeMetadata" in data:
        import aws_sdk_codecommit.types.merge_metadata

        out["merge_metadata"] = (
            aws_sdk_codecommit.types.merge_metadata.deserialize_aws_json_1_1(
                data["mergeMetadata"]
            )
        )
    return out
