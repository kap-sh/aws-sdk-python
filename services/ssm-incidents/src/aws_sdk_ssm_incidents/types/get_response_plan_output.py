"""Generated from Smithy shape ``com.amazonaws.ssmincidents#GetResponsePlanOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_ssm_incidents.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_ssm_incidents.types.actions_list
    import aws_sdk_ssm_incidents.types.arn
    import aws_sdk_ssm_incidents.types.chat_channel
    import aws_sdk_ssm_incidents.types.engagement_set
    import aws_sdk_ssm_incidents.types.incident_template
    import aws_sdk_ssm_incidents.types.integrations
    import aws_sdk_ssm_incidents.types.response_plan_display_name
    import aws_sdk_ssm_incidents.types.response_plan_name


class GetResponsePlanOutput(TypedDict):
    arn: "aws_sdk_ssm_incidents.types.arn.Arn"
    """<p>The ARN of the response plan.</p>"""
    name: "aws_sdk_ssm_incidents.types.response_plan_name.ResponsePlanName"
    """<p>The short format name of the response plan. The name can't contain spaces.</p>"""
    display_name: NotRequired[
        "aws_sdk_ssm_incidents.types.response_plan_display_name.ResponsePlanDisplayName"
    ]
    """<p>The long format name of the response plan. Can contain spaces.</p>"""
    incident_template: "aws_sdk_ssm_incidents.types.incident_template.IncidentTemplate"
    """<p>Details used to create the incident when using this response plan.</p>"""
    chat_channel: NotRequired["aws_sdk_ssm_incidents.types.chat_channel.ChatChannel"]
    """<p>The Chatbot chat channel used for collaboration during an incident.</p>"""
    engagements: NotRequired["aws_sdk_ssm_incidents.types.engagement_set.EngagementSet"]
    """<p>The Amazon Resource Name (ARN) for the contacts and escalation plans that the response plan engages during an incident.</p>"""
    actions: NotRequired["aws_sdk_ssm_incidents.types.actions_list.ActionsList"]
    """<p>The actions that this response plan takes at the beginning of the incident.</p>"""
    integrations: NotRequired["aws_sdk_ssm_incidents.types.integrations.Integrations"]
    """<p>Information about third-party services integrated into the Incident Manager response plan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetResponsePlanOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    if "display_name" in value:
        out["displayName"] = value["display_name"]
    import aws_sdk_ssm_incidents.types.incident_template

    out["incidentTemplate"] = (
        aws_sdk_ssm_incidents.types.incident_template.serialize_json(
            value["incident_template"]
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
    if "integrations" in value:
        import aws_sdk_ssm_incidents.types.integrations

        out["integrations"] = aws_sdk_ssm_incidents.types.integrations.serialize_json(
            value["integrations"]
        )
    return out


def deserialize_json(data: dict) -> GetResponsePlanOutput:
    out: GetResponsePlanOutput = {}  # type: ignore[typeddict-item]
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("GetResponsePlanOutput.arn required")
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetResponsePlanOutput.name required")
    if "displayName" in data:
        out["display_name"] = data["displayName"]
    if "incidentTemplate" in data:
        import aws_sdk_ssm_incidents.types.incident_template

        out["incident_template"] = (
            aws_sdk_ssm_incidents.types.incident_template.deserialize_json(
                data["incidentTemplate"]
            )
        )
    else:
        raise DeserializationError("GetResponsePlanOutput.incident_template required")
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
    if "integrations" in data:
        import aws_sdk_ssm_incidents.types.integrations

        out["integrations"] = aws_sdk_ssm_incidents.types.integrations.deserialize_json(
            data["integrations"]
        )
    return out
