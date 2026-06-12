"""Generated from Smithy shape ``com.amazonaws.codecommit#ConflictResolution``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_codecommit.types.delete_file_entries
    import aws_sdk_codecommit.types.replace_content_entries
    import aws_sdk_codecommit.types.set_file_mode_entries


class ConflictResolution(TypedDict):
    replace_contents: NotRequired[
        "aws_sdk_codecommit.types.replace_content_entries.ReplaceContentEntries"
    ]
    """<p>Files to have content replaced as part of the merge conflict resolution.</p>"""
    delete_files: NotRequired[
        "aws_sdk_codecommit.types.delete_file_entries.DeleteFileEntries"
    ]
    """<p>Files to be deleted as part of the merge conflict resolution.</p>"""
    set_file_modes: NotRequired[
        "aws_sdk_codecommit.types.set_file_mode_entries.SetFileModeEntries"
    ]
    """<p>File modes that are set as part of the merge conflict resolution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConflictResolution) -> dict:
    out: dict = {}
    if "replace_contents" in value:
        import aws_sdk_codecommit.types.replace_content_entries

        out["replaceContents"] = (
            aws_sdk_codecommit.types.replace_content_entries.serialize_aws_json_1_1(
                value["replace_contents"]
            )
        )
    if "delete_files" in value:
        import aws_sdk_codecommit.types.delete_file_entries

        out["deleteFiles"] = (
            aws_sdk_codecommit.types.delete_file_entries.serialize_aws_json_1_1(
                value["delete_files"]
            )
        )
    if "set_file_modes" in value:
        import aws_sdk_codecommit.types.set_file_mode_entries

        out["setFileModes"] = (
            aws_sdk_codecommit.types.set_file_mode_entries.serialize_aws_json_1_1(
                value["set_file_modes"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConflictResolution:
    out: ConflictResolution = {}  # type: ignore[typeddict-item]
    if "replaceContents" in data:
        import aws_sdk_codecommit.types.replace_content_entries

        out["replace_contents"] = (
            aws_sdk_codecommit.types.replace_content_entries.deserialize_aws_json_1_1(
                data["replaceContents"]
            )
        )
    if "deleteFiles" in data:
        import aws_sdk_codecommit.types.delete_file_entries

        out["delete_files"] = (
            aws_sdk_codecommit.types.delete_file_entries.deserialize_aws_json_1_1(
                data["deleteFiles"]
            )
        )
    if "setFileModes" in data:
        import aws_sdk_codecommit.types.set_file_mode_entries

        out["set_file_modes"] = (
            aws_sdk_codecommit.types.set_file_mode_entries.deserialize_aws_json_1_1(
                data["setFileModes"]
            )
        )
    return out
