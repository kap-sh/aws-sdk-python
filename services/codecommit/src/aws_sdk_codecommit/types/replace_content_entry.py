"""Generated from Smithy shape ``com.amazonaws.codecommit#ReplaceContentEntry``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_codecommit.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.file_content
    import aws_sdk_codecommit.types.file_mode_type_enum
    import aws_sdk_codecommit.types.path
    import aws_sdk_codecommit.types.replacement_type_enum


class ReplaceContentEntry(TypedDict):
    file_path: "aws_sdk_codecommit.types.path.Path"
    """<p>The path of the conflicting file.</p>"""
    replacement_type: (
        "aws_sdk_codecommit.types.replacement_type_enum.ReplacementTypeEnum"
    )
    """<p>The replacement type to use when determining how to resolve the conflict.</p>"""
    content: NotRequired["aws_sdk_codecommit.types.file_content.FileContent"]
    """<p>The base-64 encoded content to use when the replacement type is USE_NEW_CONTENT.</p>"""
    file_mode: NotRequired[
        "aws_sdk_codecommit.types.file_mode_type_enum.FileModeTypeEnum"
    ]
    """<p>The file mode to apply during conflict resoltion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ReplaceContentEntry) -> dict:
    out: dict = {}
    out["filePath"] = value["file_path"]
    import aws_sdk_codecommit.types.replacement_type_enum

    out["replacementType"] = (
        aws_sdk_codecommit.types.replacement_type_enum.serialize_aws_json_1_1(
            value["replacement_type"]
        )
    )
    if "content" in value:
        import aws_sdk_codecommit.types.file_content

        out["content"] = aws_sdk_codecommit.types.file_content.serialize_aws_json_1_1(
            value["content"]
        )
    if "file_mode" in value:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["fileMode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.serialize_aws_json_1_1(
                value["file_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ReplaceContentEntry:
    out: ReplaceContentEntry = {}  # type: ignore[typeddict-item]
    if "filePath" in data:
        out["file_path"] = data["filePath"]
    else:
        raise DeserializationError("ReplaceContentEntry.file_path required")
    if "replacementType" in data:
        import aws_sdk_codecommit.types.replacement_type_enum

        out["replacement_type"] = (
            aws_sdk_codecommit.types.replacement_type_enum.deserialize_aws_json_1_1(
                data["replacementType"]
            )
        )
    else:
        raise DeserializationError("ReplaceContentEntry.replacement_type required")
    if "content" in data:
        import aws_sdk_codecommit.types.file_content

        out["content"] = aws_sdk_codecommit.types.file_content.deserialize_aws_json_1_1(
            data["content"]
        )
    if "fileMode" in data:
        import aws_sdk_codecommit.types.file_mode_type_enum

        out["file_mode"] = (
            aws_sdk_codecommit.types.file_mode_type_enum.deserialize_aws_json_1_1(
                data["fileMode"]
            )
        )
    return out
