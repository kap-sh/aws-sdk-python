"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateIncidentRecordInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.chat_channel
    import aws_sdk_ssm_incidents.types.client_token
    import aws_sdk_ssm_incidents.types.impact
    import aws_sdk_ssm_incidents.types.incident_record_status
    import aws_sdk_ssm_incidents.types.incident_summary
    import aws_sdk_ssm_incidents.types.incident_title
    import aws_sdk_ssm_incidents.types.notification_target_set


class UpdateIncidentRecordInput(TypedDict):
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token that ensures that a client calls the operation only once with the specified details.</p>"""
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the incident record you are updating.</p>"""
    title: NotRequired["aws_sdk_ssm_incidents.types.incident_title.IncidentTitle"]
    """<p>A brief description of the incident.</p>"""
    summary: NotRequired["aws_sdk_ssm_incidents.types.incident_summary.IncidentSummary"]
    """<p>A longer description of what occurred during the incident.</p>"""
    impact: NotRequired["aws_sdk_ssm_incidents.types.impact.Impact"]
    """<p>Defines the impact of the incident to customers and applications. If you provide an impact for an incident, it overwrites the impact provided by the response plan.</p> <p class=\"title\"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    status: NotRequired[
        "aws_sdk_ssm_incidents.types.incident_record_status.IncidentRecordStatus"
    ]
    """<p>The status of the incident. Possible statuses are <code>Open</code> or <code>Resolved</code>.</p>"""
    chat_channel: NotRequired["aws_sdk_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The Chatbot chat channel where responders can collaborate.</p>"""
    notification_targets: NotRequired[
        "aws_sdk_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that Incident Manager notifies when a client updates an incident.</p> <p>Using multiple SNS topics creates redundancy in the event that a Region is down during the incident.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateIncidentRecordInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["arn"] = value["arn"]
    if "title" in value:
        out["title"] = value["title"]
    if "summary" in value:
        out["summary"] = value["summary"]
    if "impact" in value:
        out["impact"] = value["impact"]
    if "status" in value:
        out["status"] = value["status"]
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


def deserialize_json(data: dict) -> UpdateIncidentRecordInput:
    out: UpdateIncidentRecordInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateIncidentRecordInput.arn required")
    if "title" in data:
        out["title"] = data["title"]
    if "summary" in data:
        out["summary"] = data["summary"]
    if "impact" in data:
        out["impact"] = data["impact"]
    if "status" in data:
        out["status"] = data["status"]
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
