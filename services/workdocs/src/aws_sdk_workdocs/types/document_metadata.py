"""Generated from Smithy shape ``com.amazonaws.workdocs#DocumentMetadata``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.document_version_metadata
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.resource_id_type
    import aws_sdk_workdocs.types.resource_state_type
    import aws_sdk_workdocs.types.shared_labels
    import aws_sdk_workdocs.types.timestamp_type


class DocumentMetadata(TypedDict):
    id: NotRequired["aws_sdk_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the document.</p>"""
    creator_id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the creator.</p>"""
    parent_folder_id: NotRequired[
        "aws_sdk_workdocs.types.resource_id_type.ResourceIdType"
    ]
    """<p>The ID of the parent folder.</p>"""
    created_timestamp: NotRequired[
        "aws_sdk_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The time when the document was created.</p>"""
    modified_timestamp: NotRequired[
        "aws_sdk_workdocs.types.timestamp_type.TimestampType"
    ]
    """<p>The time when the document was updated.</p>"""
    latest_version_metadata: NotRequired[
        "aws_sdk_workdocs.types.document_version_metadata.DocumentVersionMetadata"
    ]
    """<p>The latest version of the document.</p>"""
    resource_state: NotRequired[
        "aws_sdk_workdocs.types.resource_state_type.ResourceStateType"
    ]
    """<p>The resource state.</p>"""
    labels: NotRequired["aws_sdk_workdocs.types.shared_labels.SharedLabels"]
    """<p>List of labels on the document.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "creator_id" in value:
        out["CreatorId"] = value["creator_id"]
    if "parent_folder_id" in value:
        out["ParentFolderId"] = value["parent_folder_id"]
    if "created_timestamp" in value:
        import aws_sdk_workdocs.types.timestamp_type

        out["CreatedTimestamp"] = aws_sdk_workdocs.types.timestamp_type.serialize_json(
            value["created_timestamp"]
        )
    if "modified_timestamp" in value:
        import aws_sdk_workdocs.types.timestamp_type

        out["ModifiedTimestamp"] = aws_sdk_workdocs.types.timestamp_type.serialize_json(
            value["modified_timestamp"]
        )
    if "latest_version_metadata" in value:
        import aws_sdk_workdocs.types.document_version_metadata

        out["LatestVersionMetadata"] = (
            aws_sdk_workdocs.types.document_version_metadata.serialize_json(
                value["latest_version_metadata"]
            )
        )
    if "resource_state" in value:
        import aws_sdk_workdocs.types.resource_state_type

        out["ResourceState"] = (
            aws_sdk_workdocs.types.resource_state_type.serialize_json(
                value["resource_state"]
            )
        )
    if "labels" in value:
        import aws_sdk_workdocs.types.shared_labels

        out["Labels"] = aws_sdk_workdocs.types.shared_labels.serialize_json(
            value["labels"]
        )
    return out


def deserialize_json(data: dict) -> DocumentMetadata:
    out: DocumentMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "CreatorId" in data:
        out["creator_id"] = data["CreatorId"]
    if "ParentFolderId" in data:
        out["parent_folder_id"] = data["ParentFolderId"]
    if "CreatedTimestamp" in data:
        import aws_sdk_workdocs.types.timestamp_type

        out["created_timestamp"] = (
            aws_sdk_workdocs.types.timestamp_type.deserialize_json(
                data["CreatedTimestamp"]
            )
        )
    if "ModifiedTimestamp" in data:
        import aws_sdk_workdocs.types.timestamp_type

        out["modified_timestamp"] = (
            aws_sdk_workdocs.types.timestamp_type.deserialize_json(
                data["ModifiedTimestamp"]
            )
        )
    if "LatestVersionMetadata" in data:
        import aws_sdk_workdocs.types.document_version_metadata

        out["latest_version_metadata"] = (
            aws_sdk_workdocs.types.document_version_metadata.deserialize_json(
                data["LatestVersionMetadata"]
            )
        )
    if "ResourceState" in data:
        import aws_sdk_workdocs.types.resource_state_type

        out["resource_state"] = (
            aws_sdk_workdocs.types.resource_state_type.deserialize_json(
                data["ResourceState"]
            )
        )
    if "Labels" in data:
        import aws_sdk_workdocs.types.shared_labels

        out["labels"] = aws_sdk_workdocs.types.shared_labels.deserialize_json(
            data["Labels"]
        )
    return out
