"""Generated from Smithy shape ``com.amazonaws.workdocs#CreateFolderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.folder_metadata


class CreateFolderResponse(TypedDict):
    metadata: NotRequired["aws_sdk_workdocs.types.folder_metadata.FolderMetadata"]
    """<p>The metadata of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFolderResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_workdocs.types.folder_metadata

        out["Metadata"] = aws_sdk_workdocs.types.folder_metadata.serialize_json(
            value["metadata"]
        )
    return out


def deserialize_json(data: dict) -> CreateFolderResponse:
    out: CreateFolderResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import aws_sdk_workdocs.types.folder_metadata

        out["metadata"] = aws_sdk_workdocs.types.folder_metadata.deserialize_json(
            data["Metadata"]
        )
    return out
