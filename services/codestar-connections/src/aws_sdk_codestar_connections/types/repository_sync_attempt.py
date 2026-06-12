"""Generated from Smithy shape ``com.amazonaws.codestarconnections#RepositorySyncAttempt``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codestar_connections.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codestar_connections.types.repository_sync_event_list
    import aws_sdk_codestar_connections.types.repository_sync_status
    import aws_sdk_codestar_connections.types.timestamp


class RepositorySyncAttempt(TypedDict):
    started_at: "aws_sdk_codestar_connections.types.timestamp.Timestamp"
    """<p>The start time of a specific sync attempt.</p>"""
    status: (
        "aws_sdk_codestar_connections.types.repository_sync_status.RepositorySyncStatus"
    )
    """<p>The status of a specific sync attempt. The following are valid statuses:</p> <ul> <li> <p>INITIATED - A repository sync attempt has been created and will begin soon.</p> </li> <li> <p>IN_PROGRESS - A repository sync attempt has started and work is being done to reconcile the branch.</p> </li> <li> <p>SUCCEEDED - The repository sync attempt has completed successfully.</p> </li> <li> <p>FAILED - The repository sync attempt has failed.</p> </li> <li> <p>QUEUED - The repository sync attempt didn't execute and was queued.</p> </li> </ul>"""
    events: "aws_sdk_codestar_connections.types.repository_sync_event_list.RepositorySyncEventList"
    """<p>The events associated with a specific sync attempt.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RepositorySyncAttempt) -> dict:
    out: dict = {}
    import aws_sdk_codestar_connections.types.timestamp

    out["StartedAt"] = (
        aws_sdk_codestar_connections.types.timestamp.serialize_aws_json_1_0(
            value["started_at"]
        )
    )
    import aws_sdk_codestar_connections.types.repository_sync_status

    out["Status"] = (
        aws_sdk_codestar_connections.types.repository_sync_status.serialize_aws_json_1_0(
            value["status"]
        )
    )
    import aws_sdk_codestar_connections.types.repository_sync_event_list

    out["Events"] = (
        aws_sdk_codestar_connections.types.repository_sync_event_list.serialize_aws_json_1_0(
            value["events"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> RepositorySyncAttempt:
    out: RepositorySyncAttempt = {}  # type: ignore[typeddict-item]
    if "StartedAt" in data:
        import aws_sdk_codestar_connections.types.timestamp

        out["started_at"] = (
            aws_sdk_codestar_connections.types.timestamp.deserialize_aws_json_1_0(
                data["StartedAt"]
            )
        )
    else:
        raise DeserializationError("RepositorySyncAttempt.started_at required")
    if "Status" in data:
        import aws_sdk_codestar_connections.types.repository_sync_status

        out["status"] = (
            aws_sdk_codestar_connections.types.repository_sync_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    else:
        raise DeserializationError("RepositorySyncAttempt.status required")
    if "Events" in data:
        import aws_sdk_codestar_connections.types.repository_sync_event_list

        out["events"] = (
            aws_sdk_codestar_connections.types.repository_sync_event_list.deserialize_aws_json_1_0(
                data["Events"]
            )
        )
    else:
        raise DeserializationError("RepositorySyncAttempt.events required")
    return out
