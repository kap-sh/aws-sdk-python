"""Generated from Smithy shape ``com.amazonaws.codecommit#PutFileEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_content
    import aws_sdk_codecommit.types.file_mode_type_enum
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.source_file_specifier


class PutFileEntry(TypedDict):
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The full path to the file in the repository, including the name of the file.</p>"""
    file_mode: NotRequired[
        "aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    ]
    """<p>The extrapolated file mode permissions for the file. Valid values include EXECUTABLE and NORMAL.</p>"""
    file_content: NotRequired["aws_sdk_codecommit.types.file_content.FileContent"]
    """<p>The content of the file, if a source file is not specified.</p>"""
    source_file: NotRequired[
        "aws_sdk_codecommit.types.source_file_specifier.SourceFileSpecifier"
    ]
    """<p>The name and full path of the file that contains the changes you want to make as part of the commit, if you are not providing the file content directly.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutFileEntry) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    if "file_mode" in value:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    if "file_content" in value:
        import aws_sdk_codecommit.types.file_content

        out["fileContent"] = (
            aws_sdk_codecommit.types.file_content.serialize_aws_json_1_1(
                value["file_content"]
            )
        )
    if "source_file" in value:
        import aws_sdk_codecommit.types.source_file_specifier

        out["sourceFile"] = (
            aws_sdk_codecommit.types.source_file_specifier.serialize_aws_json_1_1(
                value["source_file"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutFileEntry:
    out: PutFileEntry = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("PutFileEntry.file_path required")
    if "fileMode" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    if "fileContent" in data:
        import aws_sdk_codecommit.types.file_content

        out["file_content"] = (
            aws_sdk_codecommit.types.file_content.deserialize_aws_json_1_1(
                data["fileContent"]
            )
        )
    if "sourceFile" in data:
        import aws_sdk_codecommit.types.source_file_specifier

        out["source_file"] = (
            aws_sdk_codecommit.types.source_file_specifier.deserialize_aws_json_1_1(
                data["sourceFile"]
            )
        )
    return out
