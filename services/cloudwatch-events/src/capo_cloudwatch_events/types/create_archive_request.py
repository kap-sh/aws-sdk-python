"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#CreateArchiveRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch_events.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.archive_description
    import capo_cloudwatch_events.types.archive_name
    import capo_cloudwatch_events.types.arn
    import capo_cloudwatch_events.types.event_pattern
    import capo_cloudwatch_events.types.retention_days


class CreateArchiveRequest(TypedDict, closed=True):
    archive_name: "capo_cloudwatch_events.types.archive_name.ArchiveName"
    """<p>The name for the archive to create.</p>"""
    event_source_arn: "capo_cloudwatch_events.types.arn.Arn"
    """<p>The ARN of the event bus that sends events to the archive.</p>"""
    description: NotRequired[
        "capo_cloudwatch_events.types.archive_description.ArchiveDescription"
    ]
    """<p>A description for the archive.</p>"""
    event_pattern: NotRequired[
        "capo_cloudwatch_events.types.event_pattern.EventPattern"
    ]
    """<p>An event pattern to use to filter events sent to the archive.</p>"""
    retention_days: NotRequired[
        "capo_cloudwatch_events.types.retention_days.RetentionDays"
    ]
    """<p>The number of days to retain events for. Default value is 0. If set to 0, events are retained indefinitely</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateArchiveRequest) -> dict:
    out: dict = {}
    out["ArchiveName"] = value["archive_name"]
    out["EventSourceArn"] = value["event_source_arn"]
    if "description" in value:
        out["Description"] = value["description"]
    if "event_pattern" in value:
        out["EventPattern"] = value["event_pattern"]
    if "retention_days" in value:
        out["RetentionDays"] = value["retention_days"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateArchiveRequest:
    out: CreateArchiveRequest = {}  # type: ignore[typeddict-item]
    if "ArchiveName" in data:
        out["archive_name"] = data["ArchiveName"]
    else:
        raise DeserializationError("CreateArchiveRequest.archive_name required")
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    else:
        raise DeserializationError("CreateArchiveRequest.event_source_arn required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "EventPattern" in data:
        out["event_pattern"] = data["EventPattern"]
    if "RetentionDays" in data:
        out["retention_days"] = data["RetentionDays"]
    return out
