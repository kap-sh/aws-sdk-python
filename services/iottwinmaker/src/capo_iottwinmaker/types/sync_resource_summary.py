"""Generated from Smithy shape ``com.amazonaws.iottwinmaker#SyncResourceSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iottwinmaker.types.id
    import capo_iottwinmaker.types.sync_resource_status
    import capo_iottwinmaker.types.sync_resource_type
    import capo_iottwinmaker.types.timestamp


class SyncResourceSummary(TypedDict, closed=True):
    resource_type: NotRequired[
        "capo_iottwinmaker.types.sync_resource_type.SyncResourceType"
    ]
    """<p>The resource type.</p>"""
    external_id: NotRequired["capo_iottwinmaker.types.id.Id"]
    """<p>The external ID.</p>"""
    resource_id: NotRequired["capo_iottwinmaker.types.id.Id"]
    """<p>The resource ID.</p>"""
    status: NotRequired[
        "capo_iottwinmaker.types.sync_resource_status.SyncResourceStatus"
    ]
    """<p>The sync resource summary status.</p>"""
    update_date_time: NotRequired["capo_iottwinmaker.types.timestamp.Timestamp"]
    """<p>The update date and time.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncResourceSummary) -> dict:
    out: dict = {}
    if "resource_type" in value:
        out["resourceType"] = value["resource_type"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    if "resource_id" in value:
        out["resourceId"] = value["resource_id"]
    if "status" in value:
        import capo_iottwinmaker.types.sync_resource_status

        out["status"] = capo_iottwinmaker.types.sync_resource_status.serialize_json(
            value["status"]
        )
    if "update_date_time" in value:
        import capo_iottwinmaker.types.timestamp

        out["updateDateTime"] = capo_iottwinmaker.types.timestamp.serialize_json(
            value["update_date_time"]
        )
    return out


def deserialize_json(data: dict) -> SyncResourceSummary:
    out: SyncResourceSummary = {}  # type: ignore[typeddict-item]
    if "resourceType" in data:
        out["resource_type"] = data["resourceType"]
    if "externalId" in data:
        out["external_id"] = data["externalId"]
    if "resourceId" in data:
        out["resource_id"] = data["resourceId"]
    if "status" in data:
        import capo_iottwinmaker.types.sync_resource_status

        out["status"] = capo_iottwinmaker.types.sync_resource_status.deserialize_json(
            data["status"]
        )
    if "updateDateTime" in data:
        import capo_iottwinmaker.types.timestamp

        out["update_date_time"] = capo_iottwinmaker.types.timestamp.deserialize_json(
            data["updateDateTime"]
        )
    return out
