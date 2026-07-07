"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdateAgentRuntimeResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_id
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_version
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.workload_identity_details


class UpdateAgentRuntimeResponse(TypedDict, closed=True):
    agent_runtime_arn: (
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_arn.AgentRuntimeArn"
    )
    """<p>The Amazon Resource Name (ARN) of the updated AgentCore Runtime.</p>"""
    agent_runtime_id: (
        "aws_sdk_bedrock_agentcore_control.types.agent_runtime_id.AgentRuntimeId"
    )
    """<p>The unique identifier of the updated AgentCore Runtime.</p>"""
    workload_identity_details: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.workload_identity_details.WorkloadIdentityDetails"
    ]
    """<p>The workload identity details for the updated AgentCore Runtime.</p>"""
    agent_runtime_version: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_version.AgentRuntimeVersion"
    """<p>The version of the updated AgentCore Runtime.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the AgentCore Runtime was created.</p>"""
    last_updated_at: (
        "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    )
    """<p>The timestamp when the AgentCore Runtime was last updated.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.AgentRuntimeStatus"
    """<p>The current status of the updated AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAgentRuntimeResponse) -> dict:
    out: dict = {}
    out["agentRuntimeArn"] = value["agent_runtime_arn"]
    out["agentRuntimeId"] = value["agent_runtime_id"]
    if "workload_identity_details" in value:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details

        out["workloadIdentityDetails"] = (
            aws_sdk_bedrock_agentcore_control.types.workload_identity_details.serialize_json(
                value["workload_identity_details"]
            )
        )
    out["agentRuntimeVersion"] = value["agent_runtime_version"]
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
    import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.serialize_json(
            value["status"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateAgentRuntimeResponse:
    out: UpdateAgentRuntimeResponse = {}  # type: ignore[typeddict-item]
    if "agentRuntimeArn" in data:
        out["agent_runtime_arn"] = data["agentRuntimeArn"]
    else:
        raise DeserializationError(
            "UpdateAgentRuntimeResponse.agent_runtime_arn required"
        )
    if "agentRuntimeId" in data:
        out["agent_runtime_id"] = data["agentRuntimeId"]
    else:
        raise DeserializationError(
            "UpdateAgentRuntimeResponse.agent_runtime_id required"
        )
    if "workloadIdentityDetails" in data:
        import aws_sdk_bedrock_agentcore_control.types.workload_identity_details

        out["workload_identity_details"] = (
            aws_sdk_bedrock_agentcore_control.types.workload_identity_details.deserialize_json(
                data["workloadIdentityDetails"]
            )
        )
    if "agentRuntimeVersion" in data:
        out["agent_runtime_version"] = data["agentRuntimeVersion"]
    else:
        raise DeserializationError(
            "UpdateAgentRuntimeResponse.agent_runtime_version required"
        )
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("UpdateAgentRuntimeResponse.created_at required")
    if "lastUpdatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["last_updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["lastUpdatedAt"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAgentRuntimeResponse.last_updated_at required"
        )
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_runtime_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.agent_runtime_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("UpdateAgentRuntimeResponse.status required")
    return out
