"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceSearchSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.tag_map
    import capo_connect.types.timestamp
    import capo_connect.types.visibility
    import capo_connect.types.workspace_description
    import capo_connect.types.workspace_id
    import capo_connect.types.workspace_name
    import capo_connect.types.workspace_title


class WorkspaceSearchSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.workspace_id.WorkspaceId"]
    """<p>The unique identifier of the workspace.</p>"""
    name: NotRequired["capo_connect.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    visibility: NotRequired["capo_connect.types.visibility.Visibility"]
    """<p>The visibility setting of the workspace.</p>"""
    description: NotRequired[
        "capo_connect.types.workspace_description.WorkspaceDescription"
    ]
    """<p>The description of the workspace.</p>"""
    title: NotRequired["capo_connect.types.workspace_title.WorkspaceTitle"]
    """<p>The title displayed for the workspace.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""
    created_at: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the workspace was created.</p>"""
    tags: NotRequired["capo_connect.types.tag_map.TagMap"]
    """<p>The tags associated with the workspace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSearchSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "visibility" in value:
        import capo_connect.types.visibility

        out["Visibility"] = capo_connect.types.visibility.serialize_json(
            value["visibility"]
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "title" in value:
        out["Title"] = value["title"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "created_at" in value:
        import capo_connect.types.timestamp

        out["CreatedAt"] = capo_connect.types.timestamp.serialize_json(
            value["created_at"]
        )
    if "tags" in value:
        import capo_connect.types.tag_map

        out["Tags"] = capo_connect.types.tag_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> WorkspaceSearchSummary:
    out: WorkspaceSearchSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Visibility" in data:
        import capo_connect.types.visibility

        out["visibility"] = capo_connect.types.visibility.deserialize_json(
            data["Visibility"]
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "Title" in data:
        out["title"] = data["Title"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "CreatedAt" in data:
        import capo_connect.types.timestamp

        out["created_at"] = capo_connect.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    if "Tags" in data:
        import capo_connect.types.tag_map

        out["tags"] = capo_connect.types.tag_map.deserialize_json(data["Tags"])
    return out
