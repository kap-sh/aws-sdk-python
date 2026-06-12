"""Generated from Smithy shape ``com.amazonaws.codecommit#File``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_mode_type_enum
    import aws_sdk_codecommit.types.object_id
    import aws_sdk_codecommit.types.path


class File(TypedDict):
    blob_id: NotRequired["aws_sdk_codecommit.types.object_id.ObjectId"]
    """<p>The blob ID that contains the file information.</p>"""
    absolute_path: NotRequired["aws_sdk_codecommit.types.path.Path"]
    """<p>The fully qualified path to the file in the repository.</p>"""
    relative_path: NotRequired["aws_sdk_codecommit.types.path.Path"]
    """<p>The relative path of the file from the folder where the query originated.</p>"""
    file_mode: NotRequired[
        "aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    ]
    """<p>The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: File) -> dict:
    out: dict = {}
    if "blob_id" in value:
        out["blobId"] = value["blob_id"]
    if "absolute_path" in value:
        out["absolutePath"] = value["absolute_path"]
    if "relative_path" in value:
        out["relativePath"] = value["relative_path"]
    if "file_mode" in value:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> File:
    out: File = {}  # type: ignore[typeddict-item]
    if "blobId" in data:
        out["blob_id"] = data["blobId"]
    if "absolutePath" in data:
        out["absolute_path"] = data["absolutePath"]
    if "relativePath" in data:
        out["relative_path"] = data["relativePath"]
    if "fileMode" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    return out
