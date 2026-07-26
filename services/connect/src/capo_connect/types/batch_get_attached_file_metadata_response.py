"""Generated from Smithy shape ``com.amazonaws.connect#BatchGetAttachedFileMetadataResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.attached_file_errors_list
    import capo_connect.types.attached_files_list


class BatchGetAttachedFileMetadataResponse(TypedDict, closed=True):
    files: NotRequired["capo_connect.types.attached_files_list.AttachedFilesList"]
    """<p>List of attached files that were successfully retrieved. </p>"""
    errors: NotRequired[
        "capo_connect.types.attached_file_errors_list.AttachedFileErrorsList"
    ]
    """<p>List of errors of attached files that could not be retrieved. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetAttachedFileMetadataResponse) -> dict:
    out: dict = {}
    if "files" in value:
        import capo_connect.types.attached_files_list

        out["Files"] = capo_connect.types.attached_files_list.serialize_json(
            value["files"]
        )
    if "errors" in value:
        import capo_connect.types.attached_file_errors_list

        out["Errors"] = capo_connect.types.attached_file_errors_list.serialize_json(
            value["errors"]
        )
    return out


def deserialize_json(data: dict) -> BatchGetAttachedFileMetadataResponse:
    out: BatchGetAttachedFileMetadataResponse = {}  # type: ignore[typeddict-item]
    if "Files" in data:
        import capo_connect.types.attached_files_list

        out["files"] = capo_connect.types.attached_files_list.deserialize_json(
            data["Files"]
        )
    if "Errors" in data:
        import capo_connect.types.attached_file_errors_list

        out["errors"] = capo_connect.types.attached_file_errors_list.deserialize_json(
            data["Errors"]
        )
    return out
