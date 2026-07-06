"""Generated from Smithy shape ``com.amazonaws.codecommit#SetFileModeEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_mode_type_enum
    import aws_sdk_codecommit.types.path


class SetFileModeEntry(TypedDict, closed=True):
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The full path to the file, including the name of the file.</p>"""
    file_mode: "aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    """<p>The file mode for the file.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SetFileModeEntry) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    import aws_sdk_codecommit.types.file_mode_type_enum

    out["fileMode"] = (
        aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
            value["file_mode"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SetFileModeEntry:
    out: SetFileModeEntry = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("SetFileModeEntry.file_path required")
    if "fileMode" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    else:
        raise DeserializationError("SetFileModeEntry.file_mode required")
    return out
