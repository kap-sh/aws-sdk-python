"""Generated from Smithy shape ``com.amazonaws.ssmincidents#UpdateResponsePlanInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.actions_list
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.chat_channel
    import aws_sdk_ssm_incidents.types.client_token
    import aws_sdk_ssm_incidents.types.dedupe_string
    import aws_sdk_ssm_incidents.types.engagement_set
    import aws_sdk_ssm_incidents.types.impact
    import aws_sdk_ssm_incidents.types.incident_summary
    import aws_sdk_ssm_incidents.types.incident_title
    import aws_sdk_ssm_incidents.types.integrations
    import aws_sdk_ssm_incidents.types.notification_target_set
    import aws_sdk_ssm_incidents.types.response_plan_display_name
    import aws_sdk_ssm_incidents.types.tag_map_update


class UpdateResponsePlanInput(TypedDict):
    client_token: NotRequired["aws_sdk_ssm_incidents.types.client_token.ClientToken"]
    """<p>A token ensuring that the operation is called only once with the specified details.</p>"""
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the response plan.</p>"""
    display_name: NotRequired[
        "aws_sdk_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
    ]
    """<p>The long format name of the response plan. The display name can't contain spaces.</p>"""
    incident_template_title: NotRequired[
        "aws_sdk_ssm_incidents.types.incident_title.IncidentTitle"
    ]
    """<p>The short format name of the incident. The title can't contain spaces.</p>"""
    incident_template_impact: NotRequired["aws_sdk_ssm_incidents.types.impact.Impact"]
    """<p>Defines the impact to the customers. Providing an impact overwrites the impact provided by a response plan.</p> <p class=\"title\"> <b>Supported impact codes</b> </p> <ul> <li> <p> <code>1</code> - Critical</p> </li> <li> <p> <code>2</code> - High</p> </li> <li> <p> <code>3</code> - Medium</p> </li> <li> <p> <code>4</code> - Low</p> </li> <li> <p> <code>5</code> - No Impact</p> </li> </ul>"""
    incident_template_summary: NotRequired[
        "aws_sdk_ssm_incidents.types.incident_summary.IncidentSummary"
    ]
    """<p>A brief summary of the incident. This typically contains what has happened, what's currently happening, and next steps.</p>"""
    incident_template_dedupe_string: NotRequired[
        "aws_sdk_ssm_incidents.types.dedupe_string.DedupeString"
    ]
    """<p>The string Incident Manager uses to prevent duplicate incidents from being created by the same incident in the same account.</p>"""
    incident_template_notification_targets: NotRequired[
        "aws_sdk_ssm_incidents.types.notification_target_set.NotificationTargetSet"
    ]
    """<p>The Amazon SNS targets that are notified when updates are made to an incident.</p>"""
    chat_channel: NotRequired["aws_sdk_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The Chatbot chat channel used for collaboration during an incident.</p> <p>Use the empty structure to remove the chat channel from the response plan.</p>"""
    engagements: NotRequired["aws_sdk_ssm_incidents.types.engagement_set.EngagementSet"]
    """<p>The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.</p>"""
    actions: NotRequired["aws_sdk_ssm_incidents.types.actions_list.ActionsList"]
    """<p>The actions that this response plan takes at the beginning of an incident.</p>"""
    incident_template_tags: NotRequired[
        "aws_sdk_ssm_incidents.types.tag_map_update.TagMapUpdate"
    ]
    """<p>Tags to assign to the template. When the <code>StartIncident</code> API action is called, Incident Manager assigns the tags specified in the template to the incident. To call this action, you must also have permission to call the <code>TagResource</code> API action for the incident record resource.</p>"""
    integrations: NotRequired["aws_sdk_ssm_incidents.types.integrations.Integrations"]
    """<p>Information about third-party services integrated into the response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateResponsePlanInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["arn"] = value["arn"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    if "incident_template_title" in value:
        out["incidentTemplateTitle"] = value["incident_template_title"]
    if "incident_template_impact" in value:
        out["incidentTemplateImpact"] = value["incident_template_impact"]
    if "incident_template_summary" in value:
        out["incidentTemplateSummary"] = value["incident_template_summary"]
    if "incident_template_dedupe_string" in value:
        out["incidentTemplateDedupeString"] = value["incident_template_dedupe_string"]
    if "incident_template_notification_targets" in value:
        import aws_sdk_ssm_incidents.types.notification_target_set

        out["incidentTemplateNotificationTargets"] = (
            aws_sdk_ssm_incidents.types.notification_target_set.serialize_json(
                value["incident_template_notification_targets"]
            )
        )
    if "chat_channel" in value:
        import aws_sdk_ssm_incidents.types.chat_channel

        out["chatChannel"] = aws_sdk_ssm_incidents.types.chat_channel.serialize_json(
            value["chat_channel"]
        )
    if "engagements" in value:
        import aws_sdk_ssm_incidents.types.engagement_set

        out["engagements"] = aws_sdk_ssm_incidents.types.engagement_set.serialize_json(
            value["engagements"]
        )
    if "actions" in value:
        import aws_sdk_ssm_incidents.types.actions_list

        out["actions"] = aws_sdk_ssm_incidents.types.actions_list.serialize_json(
            value["actions"]
        )
    if "incident_template_tags" in value:
        import aws_sdk_ssm_incidents.types.tag_map_update

        out["incidentTemplateTags"] = (
            aws_sdk_ssm_incidents.types.tag_map_update.serialize_json(
                value["incident_template_tags"]
            )
        )
    if "integrations" in value:
        import aws_sdk_ssm_incidents.types.integrations

        out["integrations"] = aws_sdk_ssm_incidents.types.integrations.serialize_json(
            value["integrations"]
        )
    return out


def deserialize_json(data: dict) -> UpdateResponsePlanInput:
    out: UpdateResponsePlanInput = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("UpdateResponsePlanInput.arn required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "incidentTemplateTitle" in data:
        out["incident_template_title"] = data["incidentTemplateTitle"]
    if "incidentTemplateImpact" in data:
        out["incident_template_impact"] = data["incidentTemplateImpact"]
    if "incidentTemplateSummary" in data:
        out["incident_template_summary"] = data["incidentTemplateSummary"]
    if "incidentTemplateDedupeString" in data:
        out["incident_template_dedupe_string"] = data["incidentTemplateDedupeString"]
    if "incidentTemplateNotificationTargets" in data:
        import aws_sdk_ssm_incidents.types.notification_target_set

        out["incident_template_notification_targets"] = (
            aws_sdk_ssm_incidents.types.notification_target_set.deserialize_json(
                data["incidentTemplateNotificationTargets"]
            )
        )
    if "chatChannel" in data:
        import aws_sdk_ssm_incidents.types.chat_channel

        out["chat_channel"] = aws_sdk_ssm_incidents.types.chat_channel.deserialize_json(
            data["chatChannel"]
        )
    if "engagements" in data:
        import aws_sdk_ssm_incidents.types.engagement_set

        out["engagements"] = (
            aws_sdk_ssm_incidents.types.engagement_set.deserialize_json(
                data["engagements"]
            )
        )
    if "actions" in data:
        import aws_sdk_ssm_incidents.types.actions_list

        out["actions"] = aws_sdk_ssm_incidents.types.actions_list.deserialize_json(
            data["actions"]
        )
    if "incidentTemplateTags" in data:
        import aws_sdk_ssm_incidents.types.tag_map_update

        out["incident_template_tags"] = (
            aws_sdk_ssm_incidents.types.tag_map_update.deserialize_json(
                data["incidentTemplateTags"]
            )
        )
    if "integrations" in data:
        import aws_sdk_ssm_incidents.types.integrations

        out["integrations"] = aws_sdk_ssm_incidents.types.integrations.deserialize_json(
            data["integrations"]
        )
    return out
