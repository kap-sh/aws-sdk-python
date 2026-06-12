"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentForPullRequestOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comment
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.location
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.repository_name


class PostCommentForPullRequestOutput(TypedDict):
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository where you posted a comment on a pull request.</p>"""
    pull_request_id: NotRequired[
        "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    ]
    """<p>The system-generated ID of the pull request. </p>"""
    before_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit in the source branch used to create the pull request, or in the case of an updated pull request, the full commit ID of the commit used to update the pull request.</p>"""
    after_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit in the destination branch where the pull request is merged.</p>"""
    before_blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>In the directionality of the pull request, the blob ID of the before blob.</p>"""
    after_blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>In the directionality of the pull request, the blob ID of the after blob.</p>"""
    location: NotRequired["aws_sdk_codecommit.types.location.Location"]
    """<p>The location of the change where you posted your comment.</p>"""
    comment: NotRequired["aws_sdk_codecommit.types.comment.Comment"]
    """<p>The content of the comment you posted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostCommentForPullRequestOutput) -> dict:
    out: dict = {}
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
    if "pull_request_id" in value:
        out["pullRequestId"] = value["pull_request_id"]
    if "before_commit_id" in value:
        out["beforeCommitId"] = value["before_commit_id"]
    if "after_commit_id" in value:
        out["afterCommitId"] = value["after_commit_id"]
    if "before_blob_id" in value:
        out["beforeBlobId"] = value["before_blob_id"]
    if "after_blob_id" in value:
        out["afterBlobId"] = value["after_blob_id"]
    if "location" in value:
        import aws_sdk_codecommit.types.location

        out["location"] = aws_sdk_codecommit.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    if "comment" in value:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.serialize_aws_json_1_1(
            value["comment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PostCommentForPullRequestOutput:
    out: PostCommentForPullRequestOutput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    if "beforeCommitId" in data:
        out["before_commit_id"] = data["beforeCommitId"]
    if "afterCommitId" in data:
        out["after_commit_id"] = data["afterCommitId"]
    if "beforeBlobId" in data:
        out["before_blob_id"] = data["beforeBlobId"]
    if "afterBlobId" in data:
        out["after_blob_id"] = data["afterBlobId"]
    if "location" in data:
        import aws_sdk_codecommit.types.location

        out["location"] = aws_sdk_codecommit.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if "comment" in data:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.deserialize_aws_json_1_1(
            data["comment"]
        )
    return out
