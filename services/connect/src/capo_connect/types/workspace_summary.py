"""Generated from Smithy shape ``com.amazonaws.connect#WorkspaceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.region_name
    import capo_connect.types.timestamp
    import capo_connect.types.workspace_id
    import capo_connect.types.workspace_name


class WorkspaceSummary(TypedDict, closed=True):
    id: NotRequired["capo_connect.types.workspace_id.WorkspaceId"]
    """<p>The unique identifier of the workspace.</p>"""
    name: NotRequired["capo_connect.types.workspace_name.WorkspaceName"]
    """<p>The name of the workspace.</p>"""
    arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the workspace.</p>"""
    last_modified_time: NotRequired["capo_connect.types.timestamp.Timestamp"]
    """<p>The timestamp when the workspace was last modified.</p>"""
    last_modified_region: NotRequired["capo_connect.types.region_name.RegionName"]
    """<p>The Amazon Web Services Region where the workspace was last modified.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkspaceSummary) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    if "arn" in value:
        out["Arn"] = value["arn"]
    if "last_modified_time" in value:
        import capo_connect.types.timestamp

        out["LastModifiedTime"] = capo_connect.types.timestamp.serialize_json(
            value["last_modified_time"]
        )
    if "last_modified_region" in value:
        out["LastModifiedRegion"] = value["last_modified_region"]
    return out


def deserialize_json(data: dict) -> WorkspaceSummary:
    out: WorkspaceSummary = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    if "LastModifiedTime" in data:
        import capo_connect.types.timestamp

        out["last_modified_time"] = capo_connect.types.timestamp.deserialize_json(
            data["LastModifiedTime"]
        )
    if "LastModifiedRegion" in data:
        out["last_modified_region"] = data["LastModifiedRegion"]
    return out
