"""Generated from Smithy shape ``com.amazonaws.chatbot#SlackWorkspace``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_chatbot.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chatbot.types.resource_state
    import aws_sdk_chatbot.types.slack_team_id
    import aws_sdk_chatbot.types.slack_team_name
    import aws_sdk_chatbot.types.string


class SlackWorkspace(TypedDict, closed=True):
    slack_team_id: "aws_sdk_chatbot.types.slack_team_id.SlackTeamId"
    """<p>The ID of the Slack workspace authorized with AWS Chatbot.</p>"""
    slack_team_name: "aws_sdk_chatbot.types.slack_team_name.SlackTeamName"
    """<p>The name of the Slack workspace.</p>"""
    state: NotRequired["aws_sdk_chatbot.types.resource_state.ResourceState"]
    """<p>Either <code>ENABLED</code> or <code>DISABLED</code>. The resource returns <code>DISABLED</code> if the organization's AWS Chatbot policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.</p>"""
    state_reason: NotRequired["aws_sdk_chatbot.types.string.String"]
    """<p>Provided if State is <code>DISABLED</code>. Provides context as to why the resource is disabled.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SlackWorkspace) -> dict:
    out: dict = {}
    out["SlackTeamId"] = value["slack_team_id"]
    out["SlackTeamName"] = value["slack_team_name"]
    if "state" in value:
        out["State"] = value["state"]
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    return out


def deserialize_json(data: dict) -> SlackWorkspace:
    out: SlackWorkspace = {}  # type: ignore[typeddict-item]
    if "SlackTeamId" in data:
        out["slack_team_id"] = data["SlackTeamId"]
    else:
        raise DeserializationError("SlackWorkspace.slack_team_id required")
    if "SlackTeamName" in data:
        out["slack_team_name"] = data["SlackTeamName"]
    else:
        raise DeserializationError("SlackWorkspace.slack_team_name required")
    if "State" in data:
        out["state"] = data["State"]
    if "StateReason" in data:
        out["state_reason"] = data["StateReason"]
    return out
