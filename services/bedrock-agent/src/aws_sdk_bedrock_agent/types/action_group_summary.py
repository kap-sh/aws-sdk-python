"""Generated from Smithy shape ``com.amazonaws.bedrockagent#ActionGroupSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.action_group_state
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name


class ActionGroupSummary(TypedDict, closed=True):
    action_group_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the action group.</p>"""
    action_group_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the action group.</p>"""
    action_group_state: (
        "aws_sdk_bedrock_agent.types.action_group_state.ActionGroupState"
    )
    r"""<p>Specifies whether the action group is available for the agent to invoke or not when sending an <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeAgent.html\">InvokeAgent</a> request.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the action group.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the action group was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ActionGroupSummary) -> dict:
    out: dict = {}
    out["actionGroupId"] = value["action_group_id"]
    out["actionGroupName"] = value["action_group_name"]
    import aws_sdk_bedrock_agent.types.action_group_state

    out["actionGroupState"] = (
        aws_sdk_bedrock_agent.types.action_group_state.serialize_json(
            value["action_group_state"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> ActionGroupSummary:
    out: ActionGroupSummary = {}  # type: ignore[typeddict-item]
    if "actionGroupId" in data:
        out["action_group_id"] = data["actionGroupId"]
    else:
        raise DeserializationError("ActionGroupSummary.action_group_id required")
    if "actionGroupName" in data:
        out["action_group_name"] = data["actionGroupName"]
    else:
        raise DeserializationError("ActionGroupSummary.action_group_name required")
    if "actionGroupState" in data:
        import aws_sdk_bedrock_agent.types.action_group_state

        out["action_group_state"] = (
            aws_sdk_bedrock_agent.types.action_group_state.deserialize_json(
                data["actionGroupState"]
            )
        )
    else:
        raise DeserializationError("ActionGroupSummary.action_group_state required")
    if "description" in data:
        out["description"] = data["description"]
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("ActionGroupSummary.updated_at required")
    return out
