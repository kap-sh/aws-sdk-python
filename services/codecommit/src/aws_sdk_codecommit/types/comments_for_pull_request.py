"""Generated from Smithy shape ``com.amazonaws.codecommit#CommentsForPullRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comments
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.location
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.repository_name


class CommentsForPullRequest(TypedDict, closed=True):
    pull_request_id: NotRequired[
        "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    ]
    """<p>The system-generated ID of the pull request.</p>"""
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository that contains the pull request.</p>"""
    before_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit that was the tip of the destination branch when the pull request was created. This commit is superceded by the after commit in the source branch when and if you merge the source branch into the destination branch.</p>"""
    after_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit that was the tip of the source branch at the time the comment was made. </p>"""
    before_blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The full blob ID of the file on which you want to comment on the destination commit.</p>"""
    after_blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The full blob ID of the file on which you want to comment on the source commit.</p>"""
    location: NotRequired["aws_sdk_codecommit.types.location.Location"]
    """<p>Location information about the comment on the pull request, including the file name, line number, and whether the version of the file where the comment was made is BEFORE (destination branch) or AFTER (source branch).</p>"""
    comments: NotRequired["aws_sdk_codecommit.types.comments.Comments"]
    """<p>An array of comment objects. Each comment object contains information about a comment on the pull request.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommentsForPullRequest) -> dict:
    out: dict = {}
    if "pull_request_id" in value:
        out["pullRequestId"] = value["pull_request_id"]
    if "repository_name" in value:
        out["repositoryName"] = value["repository_name"]
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
    if "comments" in value:
        import aws_sdk_codecommit.types.comments

        out["comments"] = aws_sdk_codecommit.types.comments.serialize_aws_json_1_1(
            value["comments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CommentsForPullRequest:
    out: CommentsForPullRequest = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
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
    if "comments" in data:
        import aws_sdk_codecommit.types.comments

        out["comments"] = aws_sdk_codecommit.types.comments.deserialize_aws_json_1_1(
            data["comments"]
        )
    return out
