"""Generated from Smithy shape ``com.amazonaws.connectcases#FileContent``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connectcases.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connectcases.types.file_arn


class FileContent(TypedDict, closed=True):
    file_arn: "capo_connectcases.types.file_arn.FileArn"
    """<p>The Amazon Resource Name (ARN) of a File in Amazon Connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FileContent) -> dict:
    out: dict = {}
    out["fileArn"] = value["file_arn"]
    return out


def deserialize_json(data: dict) -> FileContent:
    out: FileContent = {}  # type: ignore[typeddict-item]
    if "fileArn" in data:
        out["file_arn"] = data["fileArn"]
    else:
        raise DeserializationError("FileContent.file_arn required")
    return out
