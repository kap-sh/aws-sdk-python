"""Generated from Smithy shape ``com.amazonaws.workdocs#GetFolderResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.custom_metadata_map
    import aws_sdk_workdocs.types.folder_metadata


class GetFolderResponse(TypedDict):
    metadata: NotRequired["aws_sdk_workdocs.types.folder_metadata.FolderMetadata"]
    """<p>The metadata of the folder.</p>"""
    custom_metadata: NotRequired[
        "aws_sdk_workdocs.types.custom_metadata_map.CustomMetadataMap"
    ]
    """<p>The custom metadata on the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetFolderResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_workdocs.types.folder_metadata

        out["Metadata"] = aws_sdk_workdocs.types.folder_metadata.serialize_json(
            value["metadata"]
        )
    if "custom_metadata" in value:
        import aws_sdk_workdocs.types.custom_metadata_map

        out["CustomMetadata"] = (
            aws_sdk_workdocs.types.custom_metadata_map.serialize_json(
                value["custom_metadata"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetFolderResponse:
    out: GetFolderResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import aws_sdk_workdocs.types.folder_metadata

        out["metadata"] = aws_sdk_workdocs.types.folder_metadata.deserialize_json(
            data["Metadata"]
        )
    if "CustomMetadata" in data:
        import aws_sdk_workdocs.types.custom_metadata_map

        out["custom_metadata"] = (
            aws_sdk_workdocs.types.custom_metadata_map.deserialize_json(
                data["CustomMetadata"]
            )
        )
    return out
