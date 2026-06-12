"""Generated from Smithy shape ``com.amazonaws.codecommit#GetBlobInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.repository_name


class GetBlobInput(TypedDict):
    repository_name: "aws_sdk_codecommit.types.repository_name.RepositoryName"
    """<p>The name of the repository that contains the blob.</p>"""
    blob_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The ID of the blob, which is its SHA-1 pointer.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetBlobInput) -> dict:
    out: dict = {}
    out["repositoryName"] = value["repository_name"]
    out["blobId"] = value["blob_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetBlobInput:
    out: GetBlobInput = {}  # type: ignore[typeddict-item]
    if "repositoryName" in data:
        out["repository_name"] = data["repositoryName"]
    else:
        raise DeserializationError("GetBlobInput.repository_name required")
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    else:
        raise DeserializationError("GetBlobInput.blob_id required")
    return out
