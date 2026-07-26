"""Generated from Smithy shape ``com.amazonaws.codecommit#CommentsForComparedCommit``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.comments
    import capo_codecommit.types.commit_id
    import capo_codecommit.types.location
    import capo_codecommit.types.object_id
    import capo_codecommit.types.repository_name


class CommentsForComparedCommit(TypedDict, closed=True):
    repository_name: NotRequired["capo_codecommit.types.repository_name.RepositoryName"]
    """<p>The name of the repository that contains the compared commits.</p>"""
    before_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit used to establish the before of the comparison.</p>"""
    after_commit_id: NotRequired["capo_codecommit.types.commit_id.CommitId"]
    """<p>The full commit ID of the commit used to establish the after of the comparison.</p>"""
    before_blob_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full blob ID of the commit used to establish the before of the comparison.</p>"""
    after_blob_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The full blob ID of the commit used to establish the after of the comparison.</p>"""
    location: NotRequired["capo_codecommit.types.location.Location"]
    """<p>Location information about the comment on the comparison, including the file name, line number, and whether the version of the file where the comment was made is BEFORE or AFTER.</p>"""
    comments: NotRequired["capo_codecommit.types.comments.Comments"]
    """<p>An array of comment objects. Each comment object contains information about a comment on the comparison between commits.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CommentsForComparedCommit) -> dict:
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
        import capo_codecommit.types.location

        out["location"] = capo_codecommit.types.location.serialize_aws_json_1_1(
            value["location"]
        )
    if "comments" in value:
        import capo_codecommit.types.comments

        out["comments"] = capo_codecommit.types.comments.serialize_aws_json_1_1(
            value["comments"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CommentsForComparedCommit:
    out: CommentsForComparedCommit = {}  # type: ignore[typeddict-item]
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
        import capo_codecommit.types.location

        out["location"] = capo_codecommit.types.location.deserialize_aws_json_1_1(
            data["location"]
        )
    if "comments" in data:
        import capo_codecommit.types.comments

        out["comments"] = capo_codecommit.types.comments.deserialize_aws_json_1_1(
            data["comments"]
        )
    return out
