"""Generated from Smithy shape ``com.amazonaws.codecommit#SourceFileSpecifier``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.is_move
    import aws_sdk_codecommit.types.path


class SourceFileSpecifier(TypedDict):
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The full path to the file, including the name of the file.</p>"""
    is_move: "aws_sdk_codecommit.types.is_move.IsMove"
    """<p>Whether to remove the source file from the parent commit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SourceFileSpecifier) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    out["isMove"] = value.get("is_move", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> SourceFileSpecifier:
    out: SourceFileSpecifier = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("SourceFileSpecifier.file_path required")
    if "isMove" in data:
        out["is_move"] = data["isMove"]
    else:
        out["is_move"] = False
    return out
