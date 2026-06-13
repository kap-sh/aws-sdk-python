"""Generated from Smithy shape ``com.amazonaws.proton#ResourceSyncAttempt``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_proton.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_proton.types.resource_sync_events
    import aws_sdk_proton.types.resource_sync_status
    import aws_sdk_proton.types.revision


class ResourceSyncAttempt(TypedDict):
    initial_revision: "aws_sdk_proton.types.revision.Revision"
    """<p>Detail data for the initial repository commit, path and push.</p>"""
    target_revision: "aws_sdk_proton.types.revision.Revision"
    """<p>Detail data for the target revision.</p>"""
    target: "str"
    """<p>The resource that is synced to.</p>"""
    started_at: "datetime.datetime"
    """<p>The time when the sync attempt started.</p>"""
    status: "aws_sdk_proton.types.resource_sync_status.ResourceSyncStatus"
    """<p>The status of the sync attempt.</p>"""
    events: "aws_sdk_proton.types.resource_sync_events.ResourceSyncEvents"
    """<p>An array of events with detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ResourceSyncAttempt) -> dict:
    out: dict = {}
    import aws_sdk_proton.types.revision

    out["initialRevision"] = aws_sdk_proton.types.revision.serialize_aws_json_1_0(
        value["initial_revision"]
    )
    import aws_sdk_proton.types.revision

    out["targetRevision"] = aws_sdk_proton.types.revision.serialize_aws_json_1_0(
        value["target_revision"]
    )
    out["target"] = value["target"]
    import aws_sdk_proton.types._prelude.timestamp

    out["startedAt"] = aws_sdk_proton.types._prelude.timestamp.serialize_aws_json_1_0(
        value["started_at"]
    )
    out["status"] = value["status"]
    import aws_sdk_proton.types.resource_sync_events

    out["events"] = aws_sdk_proton.types.resource_sync_events.serialize_aws_json_1_0(
        value["events"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ResourceSyncAttempt:
    out: ResourceSyncAttempt = {}  # type: ignore[typeddict-item]
    if "initialRevision" in data:
        import aws_sdk_proton.types.revision

        out["initial_revision"] = (
            aws_sdk_proton.types.revision.deserialize_aws_json_1_0(
                data["initialRevision"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.initial_revision required")
    if "targetRevision" in data:
        import aws_sdk_proton.types.revision

        out["target_revision"] = aws_sdk_proton.types.revision.deserialize_aws_json_1_0(
            data["targetRevision"]
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.target_revision required")
    if "target" in data:
        out["target"] = data["target"]
    else:
        raise DeserializationError("ResourceSyncAttempt.target required")
    if "startedAt" in data:
        import aws_sdk_proton.types._prelude.timestamp

        out["started_at"] = (
            aws_sdk_proton.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["startedAt"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.started_at required")
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("ResourceSyncAttempt.status required")
    if "events" in data:
        import aws_sdk_proton.types.resource_sync_events

        out["events"] = (
            aws_sdk_proton.types.resource_sync_events.deserialize_aws_json_1_0(
                data["events"]
            )
        )
    else:
        raise DeserializationError("ResourceSyncAttempt.events required")
    return out
