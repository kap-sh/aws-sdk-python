"""Generated from Smithy shape ``com.amazonaws.ssmincidents#IncidentRecord``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.automation_execution_set
    import aws_sdk_ssm_incidents.types.chat_channel
    import aws_sdk_ssm_incidents.types.dedupe_string
    import aws_sdk_ssm_incidents.types.impact
    import aws_sdk_ssm_incidents.types.incident_record_source
    import aws_sdk_ssm_incidents.types.incident_record_status
    import aws_sdk_ssm_incidents.types.incident_summary
    import aws_sdk_ssm_incidents.types.incident_title
    import aws_sdk_ssm_incidents.types.notification_target_set


class IncidentRecord(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record.</p>"""
    title: "aws_sdk_ssm_incidents.types.incident_title.IncidentTitle"
    """<p>The title of the incident.</p>"""
    summary: NotRequired["aws_sdk_ssm_incidents.types.incident_summary.IncidentSummary"]
    """<p>The summary of the incident. The summary is a brief synopsis of what occurred, what's currently happening, and context of the incident.</p>"""
    status: "aws_sdk_ssm_incidents.types.incident_record_status.IncidentRecordStatus"
    """<p>The current status of the incident.</p>"""
    impact: "aws_sdk_ssm_incidents.types.impact.Impact"
    """<p>The impact of the incident on customers and applications.</p> <p class=\"title\"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    creation_time: "datetime.datetime"
    """<p>The timestamp for when Incident Manager created the incident record.</p>"""
    resolved_time: NotRequired["datetime.datetime"]
    """<p>The timestamp for when the incident was resolved. This appears as a timeline event.</p>"""
    last_modified_time: "datetime.datetime"
    """<p>The timestamp for when the incident was most recently modified.</p>"""
    last_modified_by: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>Who modified the incident most recently.</p>"""
    automation_executions: NotRequired[
        "aws_sdk_ssm_incidents.types.automation_execution_set.AutomationExecutionSet"
    ]
    """<p>The runbook, or automation document, that's run at the beginning of the incident.</p>"""
    incident_record_source: (
        "aws_sdk_ssm_incidents.types.incident_record_source.IncidentRecordSource"
    )
    """<p>Details about the action that started the incident.</p>"""
    dedupe_string: "aws_sdk_ssm_incidents.types.dedupe_string.DedupeString"
    """<p>The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.</p>"""
    chat_channel: NotRequired["aws_sdk_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The chat channel used for collaboration during an incident.</p>"""
    notification_targets: NotRequired[
        "aws_sdk_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that are notified when updates are made to an incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IncidentRecord) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["title"] = value["title"]
    if "summary" in value:
        out["summary"] = value["summary"]
    out["status"] = value["status"]
    out["impact"] = value["impact"]
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["creationTime"] = aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
        value["creation_time"]
    )
    if "resolved_time" in value:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["resolvedTime"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
                value["resolved_time"]
            )
        )
    import aws_sdk_ssm_incidents.types._prelude.timestamp

    out["lastModifiedTime"] = (
        aws_sdk_ssm_incidents.types._prelude.timestamp.serialize_json(
            value["last_modified_time"]
        )
    )
    out["lastModifiedBy"] = value["last_modified_by"]
    if "automation_executions" in value:
        import aws_sdk_ssm_incidents.types.automation_execution_set

        out["automationExecutions"] = (
            aws_sdk_ssm_incidents.types.automation_execution_set.serialize_json(
                value["automation_executions"]
            )
        )
    import aws_sdk_ssm_incidents.types.incident_record_source

    out["incidentRecordSource"] = (
        aws_sdk_ssm_incidents.types.incident_record_source.serialize_json(
            value["incident_record_source"]
        )
    )
    out["dedupeString"] = value["dedupe_string"]
    if "chat_channel" in value:
        import aws_sdk_ssm_incidents.types.chat_channel

        out["chatChannel"] = aws_sdk_ssm_incidents.types.chat_channel.serialize_json(
            value["chat_channel"]
        )
    if "notification_targets" in value:
        import aws_sdk_ssm_incidents.types.notification_target_set

        out["notificationTargets"] = (
            aws_sdk_ssm_incidents.types.notification_target_set.serialize_json(
                value["notification_targets"]
            )
        )
    return out


def deserialize_json(data: dict) -> IncidentRecord:
    out: IncidentRecord = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("IncidentRecord.arn required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("IncidentRecord.title required")
    if "summary" in data:
        out["summary"] = data["summary"]
    if "status" in data:
        out["status"] = data["status"]
    else:
        raise DeserializationError("IncidentRecord.status required")
    if "impact" in data:
        out["impact"] = data["impact"]
    else:
        raise DeserializationError("IncidentRecord.impact required")
    if "creationTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["creation_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("IncidentRecord.creation_time required")
    if "resolvedTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["resolved_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["resolvedTime"]
            )
        )
    if "lastModifiedTime" in data:
        import aws_sdk_ssm_incidents.types._prelude.timestamp

        out["last_modified_time"] = (
            aws_sdk_ssm_incidents.types._prelude.timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    else:
        raise DeserializationError("IncidentRecord.last_modified_time required")
    if "lastModifiedBy" in data:
        out["last_modified_by"] = data["lastModifiedBy"]
    else:
        raise DeserializationError("IncidentRecord.last_modified_by required")
    if "automationExecutions" in data:
        import aws_sdk_ssm_incidents.types.automation_execution_set

        out["automation_executions"] = (
            aws_sdk_ssm_incidents.types.automation_execution_set.deserialize_json(
                data["automationExecutions"]
            )
        )
    if "incidentRecordSource" in data:
        import aws_sdk_ssm_incidents.types.incident_record_source

        out["incident_record_source"] = (
            aws_sdk_ssm_incidents.types.incident_record_source.deserialize_json(
                data["incidentRecordSource"]
            )
        )
    else:
        raise DeserializationError("IncidentRecord.incident_record_source required")
    if "dedupeString" in data:
        out["dedupe_string"] = data["dedupeString"]
    else:
        raise DeserializationError("IncidentRecord.dedupe_string required")
    if "chatChannel" in data:
        import aws_sdk_ssm_incidents.types.chat_channel

        out["chat_channel"] = aws_sdk_ssm_incidents.types.chat_channel.deserialize_json(
            data["chatChannel"]
        )
    if "notificationTargets" in data:
        import aws_sdk_ssm_incidents.types.notification_target_set

        out["notification_targets"] = (
            aws_sdk_ssm_incidents.types.notification_target_set.deserialize_json(
                data["notificationTargets"]
            )
        )
    return out
