"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateAgentAliasRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.tags_map


class CreateAgentAliasRequest(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_alias_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>A description of the alias of the agent.</p>"""
    routing_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.AgentAliasRoutingConfiguration"
    ]
    """<p>Contains details about the routing configuration of the alias.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agent.types.tags_map.TagsMap"]
    """<p>Any tags that you want to attach to the alias of the agent.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAgentAliasRequest) -> dict:
    out: dict = {}
    out["agentAliasName"] = value["agent_alias_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "description" in value:
        out["description"] = value["description"]
    if "routing_configuration" in value:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routingConfiguration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.serialize_json(
                value["routing_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock_agent.types.tags_map

        out["tags"] = aws_sdk_bedrock_agent.types.tags_map.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAgentAliasRequest:
    out: CreateAgentAliasRequest = {}  # type: ignore[typeddict-item]
    if "agentAliasName" in data:
        out["agent_alias_name"] = data["agentAliasName"]
    else:
        raise DeserializationError("CreateAgentAliasRequest.agent_alias_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.agent_alias_routing_configuration

        out["routing_configuration"] = (
            aws_sdk_bedrock_agent.types.agent_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock_agent.types.tags_map

        out["tags"] = aws_sdk_bedrock_agent.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
