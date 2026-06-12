"""Generated from Smithy shape ``com.amazonaws.codestarconnections#ResourceSyncAttempt``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.resource_sync_event_list
    import aws_sdk_codestar_connections.types.resource_sync_status
    import aws_sdk_codestar_connections.types.revision
    import aws_sdk_codestar_connections.types.target
    import aws_sdk_codestar_connections.types.timestamp


class ResourceSyncAttempt(TypedDict):
    events: "aws_sdk_codestar_connections.types.resource_sync_event_list.ResourceSyncEventList"
    """<p>The events related to a resource sync attempt.</p>"""
    initial_revision: "aws_sdk_codestar_connections.types.revision.Revision"
    """<p>The current state of the resource as defined in the resource's <code>config-file</code> in the linked repository.</p>"""
    started_at: "aws_sdk_codestar_connections.types.timestamp.Timestamp"
    """<p>The start time for a resource sync attempt.</p>"""
    status: "aws_sdk_codestar_connections.types.resource_sync_status.ResourceSyncStatus"
    """<p>The status for a resource sync attempt. The follow are valid statuses:</p> <ul> <li> <p>SYNC-INITIATED - A resource sync attempt has been created and will begin soon.</p> </li> <li> <p>SYNCING - Syncing has started and work is being done to reconcile state.</p> </li> <li> <p>SYNCED - Syncing has completed successfully.</p> </li> <li> <p>SYNC_FAILED - A resource sync attempt has failed.</p> </li> </ul>"""
    target_revision: "aws_sdk_codestar_connections.types.revision.Revision"
    """<p>The desired state of the resource as defined in the resource's <code>config-file</code> in the linked repository. Git sync attempts to update the resource to this state.</p>"""
    target: "aws_sdk_codestar_connections.types.target.Target"
    """<p>The name of the Amazon Web Services resource that is attempted to be synchronized.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncAttempt) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.resource_sync_event_list

    out["Events"] = (
        aws_sdk_codestar_connections.types.resource_sync_event_list.serialize_aws_json_1_0(
            value["events"]
        )
    )
    import aws_sdk_codestar_connections.types.revision

    out["InitialRevision"] = (
        aws_sdk_codestar_connections.types.revision.serialize_aws_json_1_0(
            value["initial_revision"]
        )
    )
    import aws_sdk_codestar_connections.types.timestamp

    out["StartedAt"] = (
        aws_sdk_codestar_connections.types.timestamp.serialize_aws_json_1_0(
            value["started_at"]
        )
    )
    import aws_sdk_codestar_connections.types.resource_sync_status

    out["Status"] = (
        aws_sdk_codestar_connections.types.resource_sync_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import aws_sdk_codestar_connections.types.revision

    out["TargetRevision"] = (
        aws_sdk_codestar_connections.types.revision.serialize_aws_json_1_0(
            value["target_revision"]
        )
    )
    out["Target"] = value["target"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSyncAttempt:
    out: ResourceSyncAttempt = {}  # type: ignore[typeddict-item]
    if "Events" in data:
        import aws_sdk_codestar_connections.types.resource_sync_event_list

        out["events"] = (
            aws_sdk_codestar_connections.types.resource_sync_event_list.deserialize_aws_json_1_0(
                data["Events"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.events required")
    if "InitialRevision" in data:
        import aws_sdk_codestar_connections.types.revision

        out["initial_revision"] = (
            aws_sdk_codestar_connections.types.revision.deserialize_aws_json_1_0(
                data["InitialRevision"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.initial_revision required")
    if "StartedAt" in data:
        import aws_sdk_codestar_connections.types.timestamp

        out["started_at"] = (
            aws_sdk_codestar_connections.types.timestamp.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.started_at required")
    if "Status" in data:
        import aws_sdk_codestar_connections.types.resource_sync_status

        out["status"] = (
            aws_sdk_codestar_connections.types.resource_sync_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.status required")
    if "TargetRevision" in data:
        import aws_sdk_codestar_connections.types.revision

        out["target_revision"] = (
            aws_sdk_codestar_connections.types.revision.deserialize_aws_json_1_0(
                data["TargetRevision"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.target_revision required")
    if "Target" in data:
        out["target"] = data["Target"]
    else:
        raise DeserializationError("ResourceSyncAttempt.target required")
    return out
