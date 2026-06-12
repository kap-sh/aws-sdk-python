"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentForPullRequestInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.client_request_token
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.content
    import aws_sdk_codecommit.types.location
    import aws_sdk_codecommit.types.pull_request_id
    import aws_sdk_codecommit.types.repository_name


class PostCommentForPullRequestInput(TypedDict):
    pull_request_id: "aws_sdk_codecommit.types.pull_request_id.PullRequestId"
    """<p>The system-generated ID of the pull request. To get this ID, use <a>ListPullRequests</a>.</p>"""
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to post a comment on a pull request.</p>"""
    before_commit_id: "aws_sdk_codecommit.types.commit_id.CommitId"
    """<p>The full commit ID of the commit in the destination branch that was the tip of the branch at the time the pull request was created.</p>"""
    after_commit_id: "aws_sdk_codecommit.types.commit_id.CommitId"
    """<p>The full commit ID of the commit in the source branch that is the current tip of the branch for the pull request when you post the comment.</p>"""
    location: NotRequired["aws_sdk_codecommit.types.location.Location"]
    """<p>The location of the change where you want to post your comment. If no location is provided, the comment is posted as a general comment on the pull request difference between the before commit ID and the after commit ID.</p>"""
    content: "aws_sdk_codecommit.types.content.Content"
    """<p>The content of your comment on the change.</p>"""
    client_request_token: NotRequired[
        "aws_sdk_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostCommentForPullRequestInput) -> dict:
    out: dict = {}
    out["pullRequestId"] = value["pull_request_id"]
    out["repositoryName"] = value["repository_name"]
    out["beforeCommitId"] = value["before_commit_id"]
    out["afterCommitId"] = value["after_commit_id"]
    if "location" in value:
        import aws_sdk_codecommit.types.location

        out["location"] = aws_sdk_codecommit.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    out["content"] = value["content"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PostCommentForPullRequestInput:
    out: PostCommentForPullRequestInput = {}  # type: ignore[typeddict-item]
    if "pullRequestId" in data:
        out["pull_request_id"] = data["pullRequestId"]
    else:
        raise DeserializationError(
            "PostCommentForPullRequestInput.pull_request_id required"
        )
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "PostCommentForPullRequestInput.repository_name required"
        )
    if "beforeCommitId" in data:
        out["before_commit_id"] = data["beforeCommitId"]
    else:
        raise DeserializationError(
            "PostCommentForPullRequestInput.before_commit_id required"
        )
    if "afterCommitId" in data:
        out["after_commit_id"] = data["afterCommitId"]
    else:
        raise DeserializationError(
            "PostCommentForPullRequestInput.after_commit_id required"
        )
    if "location" in data:
        import aws_sdk_codecommit.types.location

        out["location"] = aws_sdk_codecommit.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("PostCommentForPullRequestInput.content required")
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
