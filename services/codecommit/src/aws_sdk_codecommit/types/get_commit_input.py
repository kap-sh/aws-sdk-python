"""Generated from Smithy shape ``com.amazonaws.codecommit#GetCommitInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.repository_name


class GetCommitInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository to which the commit was made.</p>"""
    commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The commit ID. Commit IDs are the full SHA ID of the commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetCommitInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["commitId"] = value["commit_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetCommitInput:
    out: GetCommitInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("GetCommitInput.repository_name required")
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    else:
        raise DeserializationError("GetCommitInput.commit_id required")
    return out
