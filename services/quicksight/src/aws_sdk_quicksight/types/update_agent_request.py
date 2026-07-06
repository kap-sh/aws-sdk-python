"""Generated from Smithy shape ``com.amazonaws.quicksight#UpdateAgentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_quicksight.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_quicksight.types.agent_description
    import aws_sdk_quicksight.types.agent_id
    import aws_sdk_quicksight.types.agent_name
    import aws_sdk_quicksight.types.aws_account_id
    import aws_sdk_quicksight.types.custom_prompt_input
    import aws_sdk_quicksight.types.icon_id
    import aws_sdk_quicksight.types.starter_prompt_list
    import aws_sdk_quicksight.types.update_agent_request_action_connectors_to_add_list
    import aws_sdk_quicksight.types.update_agent_request_action_connectors_to_remove_list
    import aws_sdk_quicksight.types.update_agent_request_spaces_to_add_list
    import aws_sdk_quicksight.types.update_agent_request_spaces_to_remove_list
    import aws_sdk_quicksight.types.welcome_message


class UpdateAgentRequest(TypedDict, closed=True):
    agent_id: "aws_sdk_quicksight.types.agent_id.AgentId"
    """<p>The unique identifier for the agent to update.</p>"""
    aws_account_id: "aws_sdk_quicksight.types.aws_account_id.AwsAccountId"
    """<p>The ID of the Amazon Web Services account that contains the agent.</p>"""
    name: "aws_sdk_quicksight.types.agent_name.AgentName"
    """<p>The name of the agent.</p>"""
    description: NotRequired[
        "aws_sdk_quicksight.types.agent_description.AgentDescription"
    ]
    """<p>A description of the agent.</p>"""
    icon_id: NotRequired["aws_sdk_quicksight.types.icon_id.IconId"]
    """<p>The icon identifier for the agent.</p>"""
    starter_prompts: NotRequired[
        "aws_sdk_quicksight.types.starter_prompt_list.StarterPromptList"
    ]
    """<p>A list of starter prompts that are displayed to users when they begin interacting with the agent.</p>"""
    welcome_message: NotRequired[
        "aws_sdk_quicksight.types.welcome_message.WelcomeMessage"
    ]
    """<p>The welcome message that is displayed when a user starts a conversation with the agent.</p>"""
    custom_prompt_input: NotRequired[
        "aws_sdk_quicksight.types.custom_prompt_input.CustomPromptInput"
    ]
    """<p>The custom prompt configuration for the agent.</p>"""
    spaces_to_add: NotRequired[
        "aws_sdk_quicksight.types.update_agent_request_spaces_to_add_list.UpdateAgentRequestSpacesToAddList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the spaces to attach to the agent.</p>"""
    spaces_to_remove: NotRequired[
        "aws_sdk_quicksight.types.update_agent_request_spaces_to_remove_list.UpdateAgentRequestSpacesToRemoveList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the spaces to detach from the agent.</p>"""
    action_connectors_to_add: NotRequired[
        "aws_sdk_quicksight.types.update_agent_request_action_connectors_to_add_list.UpdateAgentRequestActionConnectorsToAddList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the action connectors to attach to the agent.</p>"""
    action_connectors_to_remove: NotRequired[
        "aws_sdk_quicksight.types.update_agent_request_action_connectors_to_remove_list.UpdateAgentRequestActionConnectorsToRemoveList"
    ]
    """<p>The Amazon Resource Names (ARNs) of the action connectors to detach from the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "icon_id" in value:
        out["IconId"] = value["icon_id"]
    if "starter_prompts" in value:
        import aws_sdk_quicksight.types.starter_prompt_list

        out["StarterPrompts"] = (
            aws_sdk_quicksight.types.starter_prompt_list.serialize_json(
                value["starter_prompts"]
            )
        )
    if "welcome_message" in value:
        out["WelcomeMessage"] = value["welcome_message"]
    if "custom_prompt_input" in value:
        import aws_sdk_quicksight.types.custom_prompt_input

        out["CustomPromptInput"] = (
            aws_sdk_quicksight.types.custom_prompt_input.serialize_json(
                value["custom_prompt_input"]
            )
        )
    if "spaces_to_add" in value:
        import aws_sdk_quicksight.types.update_agent_request_spaces_to_add_list

        out["SpacesToAdd"] = (
            aws_sdk_quicksight.types.update_agent_request_spaces_to_add_list.serialize_json(
                value["spaces_to_add"]
            )
        )
    if "spaces_to_remove" in value:
        import aws_sdk_quicksight.types.update_agent_request_spaces_to_remove_list

        out["SpacesToRemove"] = (
            aws_sdk_quicksight.types.update_agent_request_spaces_to_remove_list.serialize_json(
                value["spaces_to_remove"]
            )
        )
    if "action_connectors_to_add" in value:
        import aws_sdk_quicksight.types.update_agent_request_action_connectors_to_add_list

        out["ActionConnectorsToAdd"] = (
            aws_sdk_quicksight.types.update_agent_request_action_connectors_to_add_list.serialize_json(
                value["action_connectors_to_add"]
            )
        )
    if "action_connectors_to_remove" in value:
        import aws_sdk_quicksight.types.update_agent_request_action_connectors_to_remove_list

        out["ActionConnectorsToRemove"] = (
            aws_sdk_quicksight.types.update_agent_request_action_connectors_to_remove_list.serialize_json(
                value["action_connectors_to_remove"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateAgentRequest:
    out: UpdateAgentRequest = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("UpdateAgentRequest.name required")
    if "Description" in data:
        out["description"] = data["Description"]
    if "IconId" in data:
        out["icon_id"] = data["IconId"]
    if "StarterPrompts" in data:
        import aws_sdk_quicksight.types.starter_prompt_list

        out["starter_prompts"] = (
            aws_sdk_quicksight.types.starter_prompt_list.deserialize_json(
                data["StarterPrompts"]
            )
        )
    if "WelcomeMessage" in data:
        out["welcome_message"] = data["WelcomeMessage"]
    if "CustomPromptInput" in data:
        import aws_sdk_quicksight.types.custom_prompt_input

        out["custom_prompt_input"] = (
            aws_sdk_quicksight.types.custom_prompt_input.deserialize_json(
                data["CustomPromptInput"]
            )
        )
    if "SpacesToAdd" in data:
        import aws_sdk_quicksight.types.update_agent_request_spaces_to_add_list

        out["spaces_to_add"] = (
            aws_sdk_quicksight.types.update_agent_request_spaces_to_add_list.deserialize_json(
                data["SpacesToAdd"]
            )
        )
    if "SpacesToRemove" in data:
        import aws_sdk_quicksight.types.update_agent_request_spaces_to_remove_list

        out["spaces_to_remove"] = (
            aws_sdk_quicksight.types.update_agent_request_spaces_to_remove_list.deserialize_json(
                data["SpacesToRemove"]
            )
        )
    if "ActionConnectorsToAdd" in data:
        import aws_sdk_quicksight.types.update_agent_request_action_connectors_to_add_list

        out["action_connectors_to_add"] = (
            aws_sdk_quicksight.types.update_agent_request_action_connectors_to_add_list.deserialize_json(
                data["ActionConnectorsToAdd"]
            )
        )
    if "ActionConnectorsToRemove" in data:
        import aws_sdk_quicksight.types.update_agent_request_action_connectors_to_remove_list

        out["action_connectors_to_remove"] = (
            aws_sdk_quicksight.types.update_agent_request_action_connectors_to_remove_list.deserialize_json(
                data["ActionConnectorsToRemove"]
            )
        )
    return out
