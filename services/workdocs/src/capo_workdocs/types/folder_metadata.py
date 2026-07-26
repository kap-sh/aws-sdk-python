"""Generated from Smithy shape ``com.amazonaws.workdocs#FolderMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.hash_type
    import capo_workdocs.types.id_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.resource_name_type
    import capo_workdocs.types.resource_state_type
    import capo_workdocs.types.shared_labels
    import capo_workdocs.types.size_type
    import capo_workdocs.types.timestamp_type


class FolderMetadata(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the folder.</p>"""
    name: NotRequired["capo_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the folder.</p>"""
    creator_id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the creator.</p>"""
    parent_folder_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the parent folder.</p>"""
    created_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the folder was created.</p>"""
    modified_timestamp: NotRequired["capo_workdocs.types.timestamp_type.TimestampType"]
    """<p>The time when the folder was updated.</p>"""
    resource_state: NotRequired[
        "capo_workdocs.types.resource_state_type.ResourceStateType"
    ]
    """<p>The resource state of the folder.</p>"""
    signature: NotRequired["capo_workdocs.types.hash_type.HashType"]
    """<p>The unique identifier created from the subfolders and documents of the folder.</p>"""
    labels: NotRequired["capo_workdocs.types.shared_labels.SharedLabels"]
    """<p>List of labels on the folder.</p>"""
    size: NotRequired["capo_workdocs.types.size_type.SizeType"]
    """<p>The size of the folder metadata.</p>"""
    latest_version_size: NotRequired["capo_workdocs.types.size_type.SizeType"]
    """<p>The size of the latest version of the folder metadata.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FolderMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "creator_id" in value:
        out["CreatorId"] = value["creator_id"]
    if "parent_folder_id" in value:
        out["ParentFolderId"] = value["parent_folder_id"]
    if "created_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["CreatedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["created_timestamp"]
        )
    if "modified_timestamp" in value:
        import capo_workdocs.types.timestamp_type

        out["ModifiedTimestamp"] = capo_workdocs.types.timestamp_type.serialize_json(
            value["modified_timestamp"]
        )
    if "resource_state" in value:
        import capo_workdocs.types.resource_state_type

        out["ResourceState"] = capo_workdocs.types.resource_state_type.serialize_json(
            value["resource_state"]
        )
    if "signature" in value:
        out["Signature"] = value["signature"]
    if "labels" in value:
        import capo_workdocs.types.shared_labels

        out["Labels"] = capo_workdocs.types.shared_labels.serialize_json(
            value["labels"]
        )
    if "size" in value:
        out["Size"] = value["size"]
    if "latest_version_size" in value:
        out["LatestVersionSize"] = value["latest_version_size"]
    return out


def deserialize_json(data: dict) -> FolderMetadata:
    out: FolderMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "CreatorId" in data:
        out["creator_id"] = data["CreatorId"]
    if "ParentFolderId" in data:
        out["parent_folder_id"] = data["ParentFolderId"]
    if "CreatedTimestamp" in data:
        import capo_workdocs.types.timestamp_type

        out["created_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["CreatedTimestamp"]
        )
    if "ModifiedTimestamp" in data:
        import capo_workdocs.types.timestamp_type

        out["modified_timestamp"] = capo_workdocs.types.timestamp_type.deserialize_json(
            data["ModifiedTimestamp"]
        )
    if "ResourceState" in data:
        import capo_workdocs.types.resource_state_type

        out["resource_state"] = (
            capo_workdocs.types.resource_state_type.deserialize_json(
                data["ResourceState"]
            )
        )
    if "Signature" in data:
        out["signature"] = data["Signature"]
    if "Labels" in data:
        import capo_workdocs.types.shared_labels

        out["labels"] = capo_workdocs.types.shared_labels.deserialize_json(
            data["Labels"]
        )
    if "Size" in data:
        out["size"] = data["Size"]
    if "LatestVersionSize" in data:
        out["latest_version_size"] = data["LatestVersionSize"]
    return out
