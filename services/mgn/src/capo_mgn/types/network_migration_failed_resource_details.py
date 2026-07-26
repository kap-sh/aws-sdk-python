"""Generated from Smithy shape ``com.amazonaws.mgn#NetworkMigrationFailedResourceDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.large_bounded_string
    import capo_mgn.types.logical_id
    import capo_mgn.types.network_migration_failed_resource_status


class NetworkMigrationFailedResourceDetails(TypedDict, closed=True):
    logical_id: NotRequired["capo_mgn.types.logical_id.LogicalID"]
    """<p>The logical ID of the failed resource.</p>"""
    status: NotRequired[
        "capo_mgn.types.network_migration_failed_resource_status.NetworkMigrationFailedResourceStatus"
    ]
    """<p>The status of the failed resource.</p>"""
    status_reason: NotRequired["capo_mgn.types.large_bounded_string.LargeBoundedString"]
    """<p>The reason why the resource failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkMigrationFailedResourceDetails) -> dict:
    out: dict = {}
    if "logical_id" in value:
        out["logicalID"] = value["logical_id"]
    if "status" in value:
        out["status"] = value["status"]
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    return out


def deserialize_json(data: dict) -> NetworkMigrationFailedResourceDetails:
    out: NetworkMigrationFailedResourceDetails = {}  # type: ignore[typeddict-item]
    if "logicalID" in data:
        out["logical_id"] = data["logicalID"]
    if "status" in data:
        out["status"] = data["status"]
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    return out
