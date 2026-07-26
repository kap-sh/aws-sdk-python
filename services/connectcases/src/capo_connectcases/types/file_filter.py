"""Generated from Smithy shape ``com.amazonaws.connectcases#FileFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.file_arn


class FileFilter(TypedDict, closed=True):
    file_arn: NotRequired["capo_connectcases.types.file_arn.FileArn"]
    """<p>The Amazon Resource Name (ARN) of the file.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileFilter) -> dict:
    out: dict = {}
    if "file_arn" in value:
        out["fileArn"] = value["file_arn"]
    return out


def deserialize_json(data: dict) -> FileFilter:
    out: FileFilter = {}  # type: ignore[typeddict-item]
    if "fileArn" in data:
        out["file_arn"] = data["fileArn"]
    return out
