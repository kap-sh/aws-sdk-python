"""Generated from Smithy shape ``com.amazonaws.codestarconnections#SyncBlockerSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.latest_sync_blocker_list
    import aws_sdk_codestar_connections.types.resource_name


class SyncBlockerSummary(TypedDict, closed=True):
    resource_name: "aws_sdk_codestar_connections.types.resource_name.ResourceName"
    """<p>The resource name for sync blocker summary.</p>"""
    parent_resource_name: NotRequired[
        "aws_sdk_codestar_connections.types.resource_name.ResourceName"
    ]
    """<p>The parent resource name for a sync blocker summary.</p>"""
    latest_blockers: NotRequired[
        "aws_sdk_codestar_connections.types.latest_sync_blocker_list.LatestSyncBlockerList"
    ]
    """<p>The latest events for a sync blocker summary.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SyncBlockerSummary) -> dict:
    out: dict = {}
    out["ResourceName"] = value["resource_name"]
    if "parent_resource_name" in value:
        out["ParentResourceName"] = value["parent_resource_name"]
    if "latest_blockers" in value:
        import aws_sdk_codestar_connections.types.latest_sync_blocker_list

        out["LatestBlockers"] = (
            aws_sdk_codestar_connections.types.latest_sync_blocker_list.serialize_aws_json_1_0(
                value["latest_blockers"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SyncBlockerSummary:
    out: SyncBlockerSummary = {}  # type: ignore[typeddict-item]
    if "ResourceName" in data:
        out["resource_name"] = data["ResourceName"]
    else:
        raise DeserializationError("SyncBlockerSummary.resource_name required")
    if "ParentResourceName" in data:
        out["parent_resource_name"] = data["ParentResourceName"]
    if "LatestBlockers" in data:
        import aws_sdk_codestar_connections.types.latest_sync_blocker_list

        out["latest_blockers"] = (
            aws_sdk_codestar_connections.types.latest_sync_blocker_list.deserialize_aws_json_1_0(
                data["LatestBlockers"]
            )
        )
    return out
