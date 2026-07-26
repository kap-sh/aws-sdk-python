"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourceMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.document_version_id_type
    import capo_workdocs.types.resource_id_type
    import capo_workdocs.types.resource_name_type
    import capo_workdocs.types.resource_type
    import capo_workdocs.types.user_metadata


class ResourceMetadata(TypedDict, closed=True):
    type: NotRequired["capo_workdocs.types.resource_type.ResourceType"]
    """<p>The type of resource.</p>"""
    name: NotRequired["capo_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the resource.</p>"""
    original_name: NotRequired[
        "capo_workdocs.types.resource_name_type.ResourceNameType"
    ]
    """<p>The original name of the resource before a rename operation.</p>"""
    id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The ID of the resource.</p>"""
    version_id: NotRequired[
        "capo_workdocs.types.document_version_id_type.DocumentVersionIdType"
    ]
    """<p>The version ID of the resource. This is an optional field and is filled for action on document version.</p>"""
    owner: NotRequired["capo_workdocs.types.user_metadata.UserMetadata"]
    """<p>The owner of the resource.</p>"""
    parent_id: NotRequired["capo_workdocs.types.resource_id_type.ResourceIdType"]
    """<p>The parent ID of the resource before a rename operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourceMetadata) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_workdocs.types.resource_type

        out["Type"] = capo_workdocs.types.resource_type.serialize_json(value["type"])
    if "name" in value:
        out["Name"] = value["name"]
    if "original_name" in value:
        out["OriginalName"] = value["original_name"]
    if "id" in value:
        out["Id"] = value["id"]
    if "version_id" in value:
        out["VersionId"] = value["version_id"]
    if "owner" in value:
        import capo_workdocs.types.user_metadata

        out["Owner"] = capo_workdocs.types.user_metadata.serialize_json(value["owner"])
    if "parent_id" in value:
        out["ParentId"] = value["parent_id"]
    return out


def deserialize_json(data: dict) -> ResourceMetadata:
    out: ResourceMetadata = {}  # type: ignore[typeddict-item]
    if "Type" in data:
        import capo_workdocs.types.resource_type

        out["type"] = capo_workdocs.types.resource_type.deserialize_json(data["Type"])
    if "Name" in data:
        out["name"] = data["Name"]
    if "OriginalName" in data:
        out["original_name"] = data["OriginalName"]
    if "Id" in data:
        out["id"] = data["Id"]
    if "VersionId" in data:
        out["version_id"] = data["VersionId"]
    if "Owner" in data:
        import capo_workdocs.types.user_metadata

        out["owner"] = capo_workdocs.types.user_metadata.deserialize_json(data["Owner"])
    if "ParentId" in data:
        out["parent_id"] = data["ParentId"]
    return out
