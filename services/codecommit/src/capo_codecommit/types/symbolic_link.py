"""Generated from Smithy shape ``com.amazonaws.codecommit#SymbolicLink``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codecommit.types.file_mode_type_enum
    import capo_codecommit.types.object_id
    import capo_codecommit.types.path


class SymbolicLink(TypedDict, closed=True):
    blob_id: NotRequired["capo_codecommit.types.object_id.ObjectId"]
    """<p>The blob ID that contains the information about the symbolic link.</p>"""
    absolute_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The fully qualified path to the folder that contains the symbolic link.</p>"""
    relative_path: NotRequired["capo_codecommit.types.path.Path"]
    """<p>The relative path of the symbolic link from the folder where the query originated.</p>"""
    file_mode: NotRequired["capo_codecommit.types.file_mode_type_enum.FileModeTypeEnum"]
    """<p>The file mode permissions of the blob that cotains information about the symbolic link.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SymbolicLink) -> dict:
    out: dict = {}
    if "blob_id" in value:
        out["blobId"] = value["blob_id"]
    if "absolute_path" in value:
        out["absolutePath"] = value["absolute_path"]
    if "relative_path" in value:
        out["relativePath"] = value["relative_path"]
    if "file_mode" in value:
        import capo_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            capo_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SymbolicLink:
    out: SymbolicLink = {}  # type: ignore[typeddict-item]
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    if "absolutePath" in data:
        out["absolute_path"] = data["absolutePath"]
    if "relativePath" in data:
        out["relative_path"] = data["relativePath"]
    if "fileMode" in data:
        import capo_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            capo_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    return out
