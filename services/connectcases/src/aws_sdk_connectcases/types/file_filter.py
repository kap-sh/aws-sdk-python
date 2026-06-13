"""Generated from Smithy shape ``com.amazonaws.connectcases#FileFilter``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_connectcases.types.file_arn


class FileFilter(TypedDict):
    file_arn: NotRequired["aws_sdk_connectcases.types.file_arn.FileArn"]
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
