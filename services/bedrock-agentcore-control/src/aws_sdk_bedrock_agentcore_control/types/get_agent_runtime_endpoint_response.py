"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#GetAgentRuntimeEndpointResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.endpoint_name


class GetAgentRuntimeEndpointResponse(TypedDict):
    live_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The currently deployed version of the AgentCore Runtime on the endpoint.</p>"""
    target_version: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    ]
    """<p>The target version of the AgentCore Runtime for the endpoint.</p>"""
    agent_runtime_endpoint_arn: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_arn.AgentRuntimeEndpointArn"
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime endpoint.</p>"""
    agent_runtime_arn: (
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the AgentCore Runtime.</p>"""
    description: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.agent_endpoint_description.AgentEndpointDescription"
    ]
    """<p>The description of the AgentCore Runtime endpoint.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.AgentRuntimeEndpointStatus"
    """<p>The current status of the AgentCore Runtime endpoint.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime endpoint was created.</p>"""
    last_updated_at: (
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp when the AgentCore Runtime endpoint was last updated.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for failure if the AgentCore Runtime endpoint is in a failed state.</p>"""
    name: "aws_sdk_bedrock_agentcore_control.types.endpoint_name.EndpointName"
    """<p>The name of the AgentCore Runtime endpoint.</p>"""
    id: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_id.AgentRuntimeEndpointId"
    """<p>The unique identifier of the AgentCore Runtime endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetAgentRuntimeEndpointResponse) -> dict:
    out: dict = {}
    if "live_version" in value:
        out["liveVersion"] = value["live_version"]
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    out["agentRuntimeEndpointArn"] = value["agent_runtime_endpoint_arn"]
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    if "description" in value:
        out["description"] = value["description"]
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.serialize_json(
            value["status"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["lastUpdatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["last_updated_at"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    out["name"] = value["name"]
    out["id"] = value["id"]
    return out


def deserialize_json(data: dict) -> GetAgentRuntimeEndpointResponse:
    out: GetAgentRuntimeEndpointResponse = {}  # type: ignore[typeddict-item]
    if "liveVersion" in data:
        out["live_version"] = data["liveVersion"]
    if "targetVersion" in data:
        out["target_version"] = data["targetVersion"]
    if "agentRuntimeEndpointArn" in data:
        out["agent_runtime_endpoint_arn"] = data["agentRuntimeEndpointArn"]
    else:
        raise DeserializationError(
            "GetAgentRuntimeEndpointResponse.agent_runtime_endpoint_arn required"
        )
    if "agentRuntimeArn" in data:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        raise DeserializationError(
            "GetAgentRuntimeEndpointResponse.agent_runtime_arn required"
        )
    if "description" in data:
        out["description"] = data["description"]
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.agent_runtime_endpoint_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("GetAgentRuntimeEndpointResponse.status required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentRuntimeEndpointResponse.created_at required"
        )
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "GetAgentRuntimeEndpointResponse.last_updated_at required"
        )
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    if "name" in data:
        out["name"] = data["name"]
    else:
        raise DeserializationError("GetAgentRuntimeEndpointResponse.name required")
    if "id" in data:
        out["id"] = data["id"]
    else:
        raise DeserializationError("GetAgentRuntimeEndpointResponse.id required")
    return out
