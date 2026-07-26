"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#Archive``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.archive_name
    import capo_cloudwatch_events.types.archive_state
    import capo_cloudwatch_events.types.archive_state_reason
    import capo_cloudwatch_events.types.arn
    import capo_cloudwatch_events.types.long
    import capo_cloudwatch_events.types.retention_days
    import capo_cloudwatch_events.types.timestamp


class Archive(TypedDict, closed=True):
    archive_name: NotRequired["capo_cloudwatch_events.types.archive_name.ArchiveName"]
    """<p>The name of the archive.</p>"""
    event_source_arn: NotRequired["capo_cloudwatch_events.types.arn.Arn"]
    """<p>The ARN of the event bus associated with the archive. Only events from this event bus are sent to the archive.</p>"""
    state: NotRequired["capo_cloudwatch_events.types.archive_state.ArchiveState"]
    """<p>The current state of the archive.</p>"""
    state_reason: NotRequired[
        "capo_cloudwatch_events.types.archive_state_reason.ArchiveStateReason"
    ]
    """<p>A description for the reason that the archive is in the current state.</p>"""
    retention_days: NotRequired[
        "capo_cloudwatch_events.types.retention_days.RetentionDays"
    ]
    """<p>The number of days to retain events in the archive before they are deleted.</p>"""
    size_bytes: "capo_cloudwatch_events.types.long.Long"
    """<p>The size of the archive, in bytes.</p>"""
    event_count: "capo_cloudwatch_events.types.long.Long"
    """<p>The number of events in the archive.</p>"""
    creation_time: NotRequired["capo_cloudwatch_events.types.timestamp.Timestamp"]
    """<p>The time stamp for the time that the archive was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Archive) -> dict:
    out: dict = {}
    if "archive_name" in value:
        out["ArchiveName"] = value["archive_name"]
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    if "state" in value:
        import capo_cloudwatch_events.types.archive_state

        out["State"] = (
            capo_cloudwatch_events.types.archive_state.serialize_aws_json_1_1(
                value["state"]
            )
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "retention_days" in value:
        out["RetentionDays"] = value["retention_days"]
    out["SizeBytes"] = value.get("size_bytes", 0)
    out["EventCount"] = value.get("event_count", 0)
    if "creation_time" in value:
        import capo_cloudwatch_events.types.timestamp

        out["CreationTime"] = (
            capo_cloudwatch_events.types.timestamp.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Archive:
    out: Archive = {}  # type: ignore[typeddict-item]
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    if "State" in data:
        import capo_cloudwatch_events.types.archive_state

        out["state"] = (
            capo_cloudwatch_events.types.archive_state.deserialize_aws_json_1_1(
                data["State"]
            )
        )
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    if "RetentionDays" in data:
        out["retention_days"] = data["RetentionDays"]
    if "SizeBytes" in data:
        out["size_bytes"] = data["SizeBytes"]
    else:
        out["size_bytes"] = 0
    if "EventCount" in data:
        out["event_count"] = data["EventCount"]
    else:
        out["event_count"] = 0
    if "CreationTime" in data:
        import capo_cloudwatch_events.types.timestamp

        out["creation_time"] = (
            capo_cloudwatch_events.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
