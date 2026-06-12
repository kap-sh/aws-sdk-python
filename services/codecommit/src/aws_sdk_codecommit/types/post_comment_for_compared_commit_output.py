"""Generated from Smithy shape ``com.amazonaws.codecommit#PostCommentForComparedCommitOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.comment
    import aws_sdk_codecommit.types.commit_id
    import aws_sdk_codecommit.types.location
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.repository_name


class PostCommentForComparedCommitOutput(TypedDict):
    repository_name: NotRequired[
        "aws_sdk_codecommit.types.repository_name.RepositoryName"
    ]
    """<p>The name of the repository where you posted a comment on the comparison between commits.</p>"""
    before_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>In the directionality you established, the full commit ID of the before commit.</p>"""
    after_commit_id: NotRequired["aws_sdk_codecommit.types.commit_id.CommitId"]
    """<p>In the directionality you established, the full commit ID of the after commit.</p>"""
    before_blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>In the directionality you established, the blob ID of the before blob.</p>"""
    after_blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>In the directionality you established, the blob ID of the after blob.</p>"""
    location: NotRequired["aws_sdk_codecommit.types.location.Location"]
    """<p>The location of the comment in the comparison between the two commits.</p>"""
    comment: NotRequired["aws_sdk_codecommit.types.comment.Comment"]
    """<p>The content of the comment you posted.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PostCommentForComparedCommitOutput) -> dict:
    out: dict = {}
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
    if "comment" in value:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.serialize_aws_json_1_1(
            value["comment"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PostCommentForComparedCommitOutput:
    out: PostCommentForComparedCommitOutput = {}  # type: ignore[typeddict-item]
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
    if "comment" in data:
        import aws_sdk_codecommit.types.comment

        out["comment"] = aws_sdk_codecommit.types.comment.deserialize_aws_json_1_1(
            data["comment"]
        )
    return out
