"""Generated from Smithy shape ``com.amazonaws.bedrockagent#FlowAliasSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.flow_alias_arn
    import aws_sdk_bedrock_agent.types.flow_alias_concurrency_configuration
    import aws_sdk_bedrock_agent.types.flow_alias_id
    import aws_sdk_bedrock_agent.types.flow_alias_routing_configuration
    import aws_sdk_bedrock_agent.types.flow_id
    import aws_sdk_bedrock_agent.types.name


class FlowAliasSummary(TypedDict):
    name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>A description of the alias.</p>"""
    routing_configuration: "aws_sdk_bedrock_agent.types.flow_alias_routing_configuration.FlowAliasRoutingConfiguration"
    """<p>A list of configurations about the versions that the alias maps to. Currently, you can only specify one.</p>"""
    concurrency_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_alias_concurrency_configuration.FlowAliasConcurrencyConfiguration"
    ]
    """<p>The configuration that specifies how nodes in the flow are executed concurrently.</p>"""
    flow_id: "aws_sdk_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow.</p>"""
    id: "aws_sdk_bedrock_agent.types.flow_alias_id.FlowAliasId"
    """<p>The unique identifier of the alias of the flow.</p>"""
    arn: "aws_sdk_bedrock_agent.types.flow_alias_arn.FlowAliasArn"
    """<p>The Amazon Resource Name (ARN) of the alias.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FlowAliasSummary) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agent.types.flow_alias_routing_configuration

    out["routingConfiguration"] = (
        aws_sdk_bedrock_agent.types.flow_alias_routing_configuration.serialize_json(
            value["routing_configuration"]
        )
    )
    if "concurrency_configuration" in value:
        import aws_sdk_bedrock_agent.types.flow_alias_concurrency_configuration

        out["concurrencyConfiguration"] = (
            aws_sdk_bedrock_agent.types.flow_alias_concurrency_configuration.serialize_json(
                value["concurrency_configuration"]
            )
        )
    out["flowId"] = value["flow_id"]
    out["id"] = value["id"]
    out["arn"] = value["arn"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> FlowAliasSummary:
    out: FlowAliasSummary = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("FlowAliasSummary.name required")
    if "description" in data:
        out["description"] = data["description"]
    if "routingConfiguration" in data:
        import aws_sdk_bedrock_agent.types.flow_alias_routing_configuration

        out["routing_configuration"] = (
            aws_sdk_bedrock_agent.types.flow_alias_routing_configuration.deserialize_json(
                data["routingConfiguration"]
            )
        )
    else:
        raise DeserializationError("FlowAliasSummary.routing_configuration required")
    if "concurrencyConfiguration" in data:
        import aws_sdk_bedrock_agent.types.flow_alias_concurrency_configuration

        out["concurrency_configuration"] = (
            aws_sdk_bedrock_agent.types.flow_alias_concurrency_configuration.deserialize_json(
                data["concurrencyConfiguration"]
            )
        )
    if "flowId" in data:
        out["flow_id"] = data["flowId"]
    else:
        raise DeserializationError("FlowAliasSummary.flow_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("FlowAliasSummary.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("FlowAliasSummary.arn required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("FlowAliasSummary.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("FlowAliasSummary.updated_at required")
    return out
