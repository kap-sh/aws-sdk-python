"""Generated from Smithy shape ``com.amazonaws.bedrockagent#UpdateFlowAliasRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.description
    import capo_bedrock_agent.types.flow_alias_concurrency_configuration
    import capo_bedrock_agent.types.flow_alias_identifier
    import capo_bedrock_agent.types.flow_alias_routing_configuration
    import capo_bedrock_agent.types.flow_identifier
    import capo_bedrock_agent.types.name


class UpdateFlowAliasRequest(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    description: NotRequired["capo_bedrock_agent.types.description.Description"]
    """<p>A description for the alias.</p>"""
    routing_configuration: "capo_bedrock_agent.types.flow_alias_routing_configuration.FlowAliasRoutingConfiguration"
    """<p>Contains information about the version to which to map the alias.</p>"""
    concurrency_configuration: NotRequired[
        "capo_bedrock_agent.types.flow_alias_concurrency_configuration.FlowAliasConcurrencyConfiguration"
    ]
    """<p>The configuration that specifies how nodes in the flow are executed in parallel.</p>"""
    flow_identifier: "capo_bedrock_agent.types.flow_identifier.FlowIdentifier"
    """<p>The unique identifier of the flow.</p>"""
    alias_identifier: (
        "capo_bedrock_agent.types.flow_alias_identifier.FlowAliasIdentifier"
    )
    """<p>The unique identifier of the alias.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFlowAliasRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_bedrock_agent.types.flow_alias_routing_configuration

    out["routingConfiguration"] = (
        capo_bedrock_agent.types.flow_alias_routing_configuration.serialize_json(
            value["routing_configuration"]
        )
    )
    if "concurrency_configuration" in value:
        import capo_bedrock_agent.types.flow_alias_concurrency_configuration

        out["concurrencyConfiguration"] = (
            capo_bedrock_agent.types.flow_alias_concurrency_configuration.serialize_json(
                value["concurrency_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateFlowAliasRequest:
    out: UpdateFlowAliasRequest = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("UpdateFlowAliasRequest.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import capo_bedrock_agent.types.flow_alias_routing_configuration

        out["routing_configuration"] = (
            capo_bedrock_agent.types.flow_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateFlowAliasRequest.routing_configuration required"
        )
    if "concurrencyConfiguration" in data:
        import capo_bedrock_agent.types.flow_alias_concurrency_configuration

        out["concurrency_configuration"] = (
            capo_bedrock_agent.types.flow_alias_concurrency_configuration.deserialize_json(
                data["concurrencyConfiguration"]
            )
        )
    return out
