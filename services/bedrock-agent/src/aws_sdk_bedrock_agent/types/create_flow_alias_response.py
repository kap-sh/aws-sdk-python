"""Generated from Smithy shape ``com.amazonaws.bedrockagent#CreateFlowAliasResponse``."""

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


class CreateFlowAliasResponse(TypedDict):
    name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the alias.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the alias.</p>"""
    routing_configuration: "aws_sdk_bedrock_agent.types.flow_alias_routing_configuration.FlowAliasRoutingConfiguration"
    """<p>Contains information about the version that the alias is mapped to.</p>"""
    concurrency_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.flow_alias_concurrency_configuration.FlowAliasConcurrencyConfiguration"
    ]
    """<p>The configuration that specifies how nodes in the flow are executed in parallel.</p>"""
    flow_id: "aws_sdk_bedrock_agent.types.flow_id.FlowId"
    """<p>The unique identifier of the flow that the alias belongs to.</p>"""
    id: "aws_sdk_bedrock_agent.types.flow_alias_id.FlowAliasId"
    """<p>The unique identifier of the alias.</p>"""
    arn: "aws_sdk_bedrock_agent.types.flow_alias_arn.FlowAliasArn"
    """<p>The Amazon Resource Name (ARN) of the alias.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the alias of the flow was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateFlowAliasResponse) -> dict:
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


def deserialize_json(data: dict) -> CreateFlowAliasResponse:
    out: CreateFlowAliasResponse = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateFlowAliasResponse.name required")
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
        raise DeserializationError(
            "CreateFlowAliasResponse.routing_configuration required"
        )
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
        raise DeserializationError("CreateFlowAliasResponse.flow_id required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("CreateFlowAliasResponse.id required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("CreateFlowAliasResponse.arn required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("CreateFlowAliasResponse.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("CreateFlowAliasResponse.updated_at required")
    return out
