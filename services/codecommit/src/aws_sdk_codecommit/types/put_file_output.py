"""Generated from Smithy shape ``com.amazonaws.codecommit#PutFileOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id


class PutFileOutput(TypedDict, closed=True):
    commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The full SHA ID of the commit that contains this file change.</p>"""
    blob_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The ID of the blob, which is its SHA-1 pointer.</p>"""
    tree_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The full SHA-1 pointer of the tree information for the commit that contains this file change.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFileOutput) -> dict:
    out: dict = {}
    out["commitId"] = value["commit_id"]
    out["blobId"] = value["blob_id"]
    out["treeId"] = value["tree_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFileOutput:
    out: PutFileOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    else:
        raise DeserializationError("PutFileOutput.commit_id required")
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    else:
        raise DeserializationError("PutFileOutput.blob_id required")
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    else:
        raise DeserializationError("PutFileOutput.tree_id required")
    return out
