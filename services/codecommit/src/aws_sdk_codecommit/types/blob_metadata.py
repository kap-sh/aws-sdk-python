"""Generated from Smithy shape ``com.amazonaws.codecommit#BlobMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.mode
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.path


class BlobMetadata(TypedDict):
    blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The full ID of the blob.</p>"""
    path: NotRequired["aws_sdk_codecommit.types.path.Path"]
    """<p>The path to the blob and associated file name, if any.</p>"""
    mode: NotRequired["aws_sdk_codecommit.types.mode.Mode"]
    """<p>The file mode permissions of the blob. File mode permission codes include:</p> <ul> <li> <p> <code>100644</code> indicates read/write</p> </li> <li> <p> <code>100755</code> indicates read/write/execute</p> </li> <li> <p> <code>160000</code> indicates a submodule</p> </li> <li> <p> <code>120000</code> indicates a symlink</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BlobMetadata) -> dict:
    out: dict = {}
    if "blob_id" in value:
        out["blobId"] = value["blob_id"]
    if "path" in value:
        out["path"] = value["path"]
    if "mode" in value:
        out["mode"] = value["mode"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BlobMetadata:
    out: BlobMetadata = {}  # type: ignore[typeddict-item]
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    if "path" in data:
        out["path"] = data["path"]
    if "mode" in data:
        out["mode"] = data["mode"]
    return out
