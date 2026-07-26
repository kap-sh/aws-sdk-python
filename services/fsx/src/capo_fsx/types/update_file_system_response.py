"""Generated from Smithy shape ``com.amazonaws.fsx#UpdateFileSystemResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fsx.types.file_system


class UpdateFileSystemResponse(TypedDict, closed=True):
    file_system: NotRequired["capo_fsx.types.file_system.FileSystem"]
    """<p>A description of the file system that was updated.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateFileSystemResponse) -> dict:
    out: dict = {}
    if "file_system" in value:
        import capo_fsx.types.file_system

        out["FileSystem"] = capo_fsx.types.file_system.serialize_aws_json_1_1(
            value["file_system"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateFileSystemResponse:
    out: UpdateFileSystemResponse = {}  # type: ignore[typeddict-item]
    if "FileSystem" in data:
        import capo_fsx.types.file_system

        out["file_system"] = capo_fsx.types.file_system.deserialize_aws_json_1_1(
            data["FileSystem"]
        )
    return out
