"""Generated from Smithy shape ``com.amazonaws.quicksight#Agent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_quicksight.types.agent_action_connectors_list
    import aws_sdk_quicksight.types.agent_arn
    import aws_sdk_quicksight.types.agent_description
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.agent_lifecycle
    import aws_sdk_quicksight.types.agent_name
    import aws_sdk_quicksight.types.agent_spaces_list
    import aws_sdk_quicksight.types.agent_status
    import aws_sdk_quicksight.types.custom_prompt_interface
    import aws_sdk_quicksight.types.icon_id
    import aws_sdk_quicksight.types.starter_prompt_list
    import aws_sdk_quicksight.types.welcome_message


class Agent(TypedDict):
    spaces: NotRequired["aws_sdk_quicksight.types.agent_spaces_list.AgentSpacesList"]
    """<p>The Amazon Resource Names (ARNs) of the spaces attached to the agent.</p>"""
    action_connectors: NotRequired[
        "aws_sdk_quicksight.types.agent_action_connectors_list.AgentActionConnectorsList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the action connectors attached to the agent.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.agent_description.AgentDescription"
    ]
    """<p>A description of the agent.</p>"""
    icon_id: NotRequired["aws_sdk_quicksight.types.icon_id.IconId"]
    """<p>The icon identifier for the agent.</p>"""
    name: "aws_sdk_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    starter_prompts: NotRequired[
        "aws_sdk_quicksight.types.starter_prompt_list.StarterPromptList"
    ]
    """<p>A list of starter prompts that are displayed to users when they begin interacting with the agent.</p>"""
    welcome_message: NotRequired[
        "aws_sdk_quicksight.types.welcome_message.WelcomeMessage"
    ]
    """<p>The welcome message that is displayed when a user starts a conversation with the agent.</p>"""
    arn: "aws_sdk_quicksight.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent.</p>"""
    agent_lifecycle: "aws_sdk_quicksight.types.agent_lifecycle.AgentLifecycle"
    """<p>The lifecycle state of the agent. Valid values are <code>PREVIEW</code> and <code>PUBLISHED</code>.</p>"""
    agent_status: "aws_sdk_quicksight.types.agent_status.AgentStatus"
    """<p>The status of the agent.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the agent was created.</p>"""
    creator: "str"
    """<p>The identity of the user who created the agent.</p>"""
    custom_prompt_interface: NotRequired[
        "aws_sdk_quicksight.types.custom_prompt_interface.CustomPromptInterface"
    ]
    """<p>The custom prompt interface configuration for the agent.</p>"""
    error_message: NotRequired["str"]
    """<p>An error message associated with the agent, if applicable.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date and time that the agent was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Agent) -> dict:
    out: dict = {}
    if "spaces" in value:
        import aws_sdk_quicksight.types.agent_spaces_list

        out["Spaces"] = aws_sdk_quicksight.types.agent_spaces_list.serialize_json(
            value["spaces"]
        )
    if "action_connectors" in value:
        import aws_sdk_quicksight.types.agent_action_connectors_list

        out["ActionConnectors"] = (
            aws_sdk_quicksight.types.agent_action_connectors_list.serialize_json(
                value["action_connectors"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    if "icon_id" in value:
        out["IconId"] = value["icon_id"]
    out["Name"] = value["name"]
    if "starter_prompts" in value:
        import aws_sdk_quicksight.types.starter_prompt_list

        out["StarterPrompts"] = (
            aws_sdk_quicksight.types.starter_prompt_list.serialize_json(
                value["starter_prompts"]
            )
        )
    if "welcome_message" in value:
        out["WelcomeMessage"] = value["welcome_message"]
    out["Arn"] = value["arn"]
    out["AgentId"] = value["agent_id"]
    import aws_sdk_quicksight.types.agent_lifecycle

    out["AgentLifecycle"] = aws_sdk_quicksight.types.agent_lifecycle.serialize_json(
        value["agent_lifecycle"]
    )
    import aws_sdk_quicksight.types.agent_status

    out["AgentStatus"] = aws_sdk_quicksight.types.agent_status.serialize_json(
        value["agent_status"]
    )
    import aws_sdk_quicksight.types._prelude.timestamp

    out["CreatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    out["Creator"] = value["creator"]
    if "custom_prompt_interface" in value:
        import aws_sdk_quicksight.types.custom_prompt_interface

        out["CustomPromptInterface"] = (
            aws_sdk_quicksight.types.custom_prompt_interface.serialize_json(
                value["custom_prompt_interface"]
            )
        )
    if "error_message" in value:
        out["ErrorMessage"] = value["error_message"]
    import aws_sdk_quicksight.types._prelude.timestamp

    out["UpdatedAt"] = aws_sdk_quicksight.types._prelude.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> Agent:
    out: Agent = {}  # type: ignore[typeddict-item]
    if "Spaces" in data:
        import aws_sdk_quicksight.types.agent_spaces_list

        out["spaces"] = aws_sdk_quicksight.types.agent_spaces_list.deserialize_json(
            data["Spaces"]
        )
    if "ActionConnectors" in data:
        import aws_sdk_quicksight.types.agent_action_connectors_list

        out["action_connectors"] = (
            aws_sdk_quicksight.types.agent_action_connectors_list.deserialize_json(
                data["ActionConnectors"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    if "IconId" in data:
        out["icon_id"] = data["IconId"]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("Agent.name required")
    if "StarterPrompts" in data:
        import aws_sdk_quicksight.types.starter_prompt_list

        out["starter_prompts"] = (
            aws_sdk_quicksight.types.starter_prompt_list.deserialize_json(
                data["StarterPrompts"]
            )
        )
    if "WelcomeMessage" in data:
        out["welcome_message"] = data["WelcomeMessage"]
    if "Arn" in data:
        out["arn"] = data["Arn"]
    else:
        raise DeserializationError("Agent.arn required")
    if "AgentId" in data:
        out["agent_id"] = data["AgentId"]
    else:
        raise DeserializationError("Agent.agent_id required")
    if "AgentLifecycle" in data:
        import aws_sdk_quicksight.types.agent_lifecycle

        out["agent_lifecycle"] = (
            aws_sdk_quicksight.types.agent_lifecycle.deserialize_json(
                data["AgentLifecycle"]
            )
        )
    else:
        raise DeserializationError("Agent.agent_lifecycle required")
    if "AgentStatus" in data:
        import aws_sdk_quicksight.types.agent_status

        out["agent_status"] = aws_sdk_quicksight.types.agent_status.deserialize_json(
            data["AgentStatus"]
        )
    else:
        raise DeserializationError("Agent.agent_status required")
    if "CreatedAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["created_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["CreatedAt"]
            )
        )
    else:
        raise DeserializationError("Agent.created_at required")
    if "Creator" in data:
        out["creator"] = data["Creator"]
    else:
        raise DeserializationError("Agent.creator required")
    if "CustomPromptInterface" in data:
        import aws_sdk_quicksight.types.custom_prompt_interface

        out["custom_prompt_interface"] = (
            aws_sdk_quicksight.types.custom_prompt_interface.deserialize_json(
                data["CustomPromptInterface"]
            )
        )
    if "ErrorMessage" in data:
        out["error_message"] = data["ErrorMessage"]
    if "UpdatedAt" in data:
        import aws_sdk_quicksight.types._prelude.timestamp

        out["updated_at"] = (
            aws_sdk_quicksight.types._prelude.timestamp.deserialize_json(
                data["UpdatedAt"]
            )
        )
    else:
        raise DeserializationError("Agent.updated_at required")
    return out
