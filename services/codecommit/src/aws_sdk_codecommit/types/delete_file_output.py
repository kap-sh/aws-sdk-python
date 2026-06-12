"""Generated from Smithy shape ``com.amazonaws.codecommit#DeleteFileOutput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.path


class DeleteFileOutput(TypedDict):
    commit_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The full commit ID of the commit that contains the change that deletes the file.</p>"""
    blob_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The blob ID removed from the tree as part of deleting the file.</p>"""
    tree_id: "aws_sdk_codecommit.types.object_id.ObjectId"
    """<p>The full SHA-1 pointer of the tree information for the commit that contains the delete file change.</p>"""
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The fully qualified path to the file to be deleted, including the full name and extension of that file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteFileOutput) -> dict:
    out: dict = {}
    out["commitId"] = value["commit_id"]
    out["blobId"] = value["blob_id"]
    out["treeId"] = value["tree_id"]
    out["filePath"] = value["file_path"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteFileOutput:
    out: DeleteFileOutput = {}  # type: ignore[typeddict-item]
    if "commitId" in data:
        out["commit_id"] = data["commitId"]
    else:
        raise DeserializationError("DeleteFileOutput.commit_id required")
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    else:
        raise DeserializationError("DeleteFileOutput.blob_id required")
    if "treeId" in data:
        out["tree_id"] = data["treeId"]
    else:
        raise DeserializationError("DeleteFileOutput.tree_id required")
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("DeleteFileOutput.file_path required")
    return out
