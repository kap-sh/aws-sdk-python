"""Generated from Smithy shape ``com.amazonaws.quicksight#FolderSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.arn
    import capo_quicksight.types.folder_name
    import capo_quicksight.types.folder_type
    import capo_quicksight.types.restrictive_resource_id
    import capo_quicksight.types.sharing_model
    import capo_quicksight.types.timestamp


class FolderSummary(TypedDict, closed=True):
    arn: NotRequired["capo_quicksight.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the folder.</p>"""
    folder_id: NotRequired[
        "capo_quicksight.types.restrictive_resource_id.RestrictiveResourceId"
    ]
    """<p>The ID of the folder.</p>"""
    name: NotRequired["capo_quicksight.types.folder_name.FolderName"]
    """<p>The display name of the folder.</p>"""
    folder_type: NotRequired["capo_quicksight.types.folder_type.FolderType"]
    """<p>The type of folder.</p>"""
    created_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the folder was created.</p>"""
    last_updated_time: NotRequired["capo_quicksight.types.timestamp.Timestamp"]
    """<p>The time that the folder was last updated.</p>"""
    sharing_model: NotRequired["capo_quicksight.types.sharing_model.SharingModel"]
    """<p>The sharing scope of the folder.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FolderSummary) -> dict:
    out: dict = {}
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "folder_id" in value:
        out["FolderId"] = value["folder_id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "folder_type" in value:
        import capo_quicksight.types.folder_type

        out["FolderType"] = capo_quicksight.types.folder_type.serialize_json(
            value["folder_type"]
        )
    if "created_time" in value:
        import capo_quicksight.types.timestamp

        out["CreatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["created_time"]
        )
    if "last_updated_time" in value:
        import capo_quicksight.types.timestamp

        out["LastUpdatedTime"] = capo_quicksight.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "sharing_model" in value:
        import capo_quicksight.types.sharing_model

        out["SharingModel"] = capo_quicksight.types.sharing_model.serialize_json(
            value["sharing_model"]
        )
    return out


def deserialize_json(data: dict) -> FolderSummary:
    out: FolderSummary = {}  # type: ignore[typeddict-item]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "FolderId" in data:
        out["folder_id"] = data["FolderId"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "FolderType" in data:
        import capo_quicksight.types.folder_type

        out["folder_type"] = capo_quicksight.types.folder_type.deserialize_json(
            data["FolderType"]
        )
    if "CreatedTime" in data:
        import capo_quicksight.types.timestamp

        out["created_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["CreatedTime"]
        )
    if "LastUpdatedTime" in data:
        import capo_quicksight.types.timestamp

        out["last_updated_time"] = capo_quicksight.types.timestamp.deserialize_json(
            data["LastUpdatedTime"]
        )
    if "SharingModel" in data:
        import capo_quicksight.types.sharing_model

        out["sharing_model"] = capo_quicksight.types.sharing_model.deserialize_json(
            data["SharingModel"]
        )
    return out
