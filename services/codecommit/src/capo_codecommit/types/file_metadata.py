"""Generated from Smithy shape ``com.amazonaws.codecommit#FileMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_mode_type_enum
    import capo_codecommit.types.object_id
    import capo_codecommit.types.path


class FileMetadata(TypedDict, closed=True):
    absolute_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The full path to the file to be added or updated, including the name of the file.</p>"""
    blob_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The blob ID that contains the file information.</p>"""
    file_mode: NotRequired["capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileMetadata) -> dict:
    out: dict = {}
    if "absolute_path" in value:
        out["absolutePath"] = value["absolute_path"]
    if "blob_id" in value:
        out["blobId"] = value["blob_id"]
    if "file_mode" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FileMetadata:
    out: FileMetadata = {}  # type: ignore[typeddict-item]
    if "absolutePath" in data:
        out["absolute_path"] = data["absolutePath"]
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    if "fileMode" in data:
        import capo_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    return out
