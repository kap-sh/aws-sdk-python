"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentForComparedCommitInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codecommit.types.client_request_token
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.content
    import capo_codecommit.types.location
    import capo_codecommit.types.repository_name


class PostCommentForComparedCommitInput(TypedDict, closed=True):
    repository_name: "capo_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository where you want to post a comment on the comparison between commits.</p>"""
    before_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>To establish the directionality of the comparison, the full commit ID of the before commit. Required for commenting on any commit unless that commit is the initial commit.</p>"""
    after_commit_id: "capo_codecommit.types.commit_id.CommitId"
    """<p>To establish the directionality of the comparison, the full commit ID of the after commit.</p>"""
    location: NotRequired["capo_codecommit.types.location.Location"]
    """<p>The location of the comparison where you want to comment.</p>"""
    content: "capo_codecommit.types.content.Content"
    """<p>The content of the comment you want to make.</p>"""
    client_request_token: NotRequired[
        "capo_codecommit.types.client_request_token.ClientRequestToken"
    ]
    """<p>A unique, client-generated idempotency token that, when provided in a request, ensures the request cannot be repeated with a changed parameter. If a request is received with the same parameters and a token is included, the request returns information about the initial request that used that token.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostCommentForComparedCommitInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    if "before_commit_id" in value:
        out["beforeCommitId"] = value["before_commit_id"]
    out["afterCommitId"] = value["after_commit_id"]
    if "location" in value:
        import capo_codecommit.types.location

        out["location"] = capo_codecommit.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    out["content"] = value["content"]
    if "client_request_token" in value:
        out["clientRequestToken"] = value["client_request_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PostCommentForComparedCommitInput:
    out: PostCommentForComparedCommitInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError(
            "PostCommentForComparedCommitInput.repository_name required"
        )
    if "beforeCommitId" in data:
        out["before_commit_id"] = data["beforeCommitId"]
    if "afterCommitId" in data:
        out["after_commit_id"] = data["afterCommitId"]
    else:
        raise DeserializationError(
            "PostCommentForComparedCommitInput.after_commit_id required"
        )
    if "location" in data:
        import capo_codecommit.types.location

        out["location"] = capo_codecommit.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("PostCommentForComparedCommitInput.content required")
    if "clientRequestToken" in data:
        out["client_request_token"] = data["clientRequestToken"]
    return out
