"""Generated from Smithy shape ``com.amazonaws.bedrockagent#Agent``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.agent_arn
    import aws_sdk_bedrock_agent.types.agent_collaboration
    import aws_sdk_bedrock_agent.types.agent_role_arn
    import aws_sdk_bedrock_agent.types.agent_status
    import aws_sdk_bedrock_agent.types.client_token
    import aws_sdk_bedrock_agent.types.custom_orchestration
    import aws_sdk_bedrock_agent.types.date_timestamp
    import aws_sdk_bedrock_agent.types.description
    import aws_sdk_bedrock_agent.types.draft_version
    import aws_sdk_bedrock_agent.types.failure_reasons
    import aws_sdk_bedrock_agent.types.guardrail_configuration
    import aws_sdk_bedrock_agent.types.id
    import aws_sdk_bedrock_agent.types.instruction
    import aws_sdk_bedrock_agent.types.kms_key_arn
    import aws_sdk_bedrock_agent.types.memory_configuration
    import aws_sdk_bedrock_agent.types.model_identifier
    import aws_sdk_bedrock_agent.types.name
    import aws_sdk_bedrock_agent.types.orchestration_type
    import aws_sdk_bedrock_agent.types.prompt_override_configuration
    import aws_sdk_bedrock_agent.types.recommended_actions
    import aws_sdk_bedrock_agent.types.session_ttl


class Agent(TypedDict):
    agent_id: "aws_sdk_bedrock_agent.types.id.Id"
    """<p>The unique identifier of the agent.</p>"""
    agent_name: "aws_sdk_bedrock_agent.types.name.Name"
    """<p>The name of the agent.</p>"""
    agent_arn: "aws_sdk_bedrock_agent.types.agent_arn.AgentArn"
    """<p>The Amazon Resource Name (ARN) of the agent.</p>"""
    agent_version: "aws_sdk_bedrock_agent.types.draft_version.DraftVersion"
    """<p>The version of the agent.</p>"""
    client_token: NotRequired["aws_sdk_bedrock_agent.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see <a href=\"https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html\">Ensuring idempotency</a>.</p>"""
    instruction: NotRequired["aws_sdk_bedrock_agent.types.instruction.Instruction"]
    """<p>Instructions that tell the agent what it should do and how it should interact with users.</p>"""
    agent_status: "aws_sdk_bedrock_agent.types.agent_status.AgentStatus"
    """<p>The status of the agent and whether it is ready for use. The following statuses are possible:</p> <ul> <li> <p>CREATING – The agent is being created.</p> </li> <li> <p>PREPARING – The agent is being prepared.</p> </li> <li> <p>PREPARED – The agent is prepared and ready to be invoked.</p> </li> <li> <p>NOT_PREPARED – The agent has been created but not yet prepared.</p> </li> <li> <p>FAILED – The agent API operation failed.</p> </li> <li> <p>UPDATING – The agent is being updated.</p> </li> <li> <p>DELETING – The agent is being deleted.</p> </li> </ul>"""
    foundation_model: NotRequired[
        "aws_sdk_bedrock_agent.types.model_identifier.ModelIdentifier"
    ]
    """<p>The foundation model used for orchestration by the agent.</p>"""
    description: NotRequired["aws_sdk_bedrock_agent.types.description.Description"]
    """<p>The description of the agent.</p>"""
    orchestration_type: NotRequired[
        "aws_sdk_bedrock_agent.types.orchestration_type.OrchestrationType"
    ]
    """<p> Specifies the orchestration strategy for the agent. </p>"""
    custom_orchestration: NotRequired[
        "aws_sdk_bedrock_agent.types.custom_orchestration.CustomOrchestration"
    ]
    """<p> Contains custom orchestration configurations for the agent. </p>"""
    idle_session_ttl_in_seconds: "aws_sdk_bedrock_agent.types.session_ttl.SessionTTL"
    """<p>The number of seconds for which Amazon Bedrock keeps information about a user's conversation with the agent.</p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and Amazon Bedrock deletes any data provided before the timeout.</p>"""
    agent_resource_role_arn: "aws_sdk_bedrock_agent.types.agent_role_arn.AgentRoleArn"
    """<p>The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the agent.</p>"""
    customer_encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the KMS key that encrypts the agent.</p>"""
    created_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the agent was created.</p>"""
    updated_at: "aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"
    """<p>The time at which the agent was last updated.</p>"""
    prepared_at: NotRequired["aws_sdk_bedrock_agent.types.date_timestamp.DateTimestamp"]
    """<p>The time at which the agent was last prepared.</p>"""
    failure_reasons: NotRequired[
        "aws_sdk_bedrock_agent.types.failure_reasons.FailureReasons"
    ]
    """<p>Contains reasons that the agent-related API that you invoked failed.</p>"""
    recommended_actions: NotRequired[
        "aws_sdk_bedrock_agent.types.recommended_actions.RecommendedActions"
    ]
    """<p>Contains recommended actions to take for the agent-related API that you invoked to succeed.</p>"""
    prompt_override_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.prompt_override_configuration.PromptOverrideConfiguration"
    ]
    """<p>Contains configurations to override prompt templates in different parts of an agent sequence. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/advanced-prompts.html\">Advanced prompts</a>.</p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.guardrail_configuration.GuardrailConfiguration"
    ]
    """<p>Details about the guardrail associated with the agent.</p>"""
    memory_configuration: NotRequired[
        "aws_sdk_bedrock_agent.types.memory_configuration.MemoryConfiguration"
    ]
    """<p>Contains memory configuration for the agent.</p>"""
    agent_collaboration: NotRequired[
        "aws_sdk_bedrock_agent.types.agent_collaboration.AgentCollaboration"
    ]
    """<p>The agent's collaboration settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Agent) -> dict:
    out: dict = {}
    out["agentId"] = value["agent_id"]
    out["agentName"] = value["agent_name"]
    out["agentArn"] = value["agent_arn"]
    out["agentVersion"] = value["agent_version"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "instruction" in value:
        out["instruction"] = value["instruction"]
    import aws_sdk_bedrock_agent.types.agent_status

    out["agentStatus"] = aws_sdk_bedrock_agent.types.agent_status.serialize_json(
        value["agent_status"]
    )
    if "foundation_model" in value:
        out["foundationModel"] = value["foundation_model"]
    if "description" in value:
        out["description"] = value["description"]
    if "orchestration_type" in value:
        import aws_sdk_bedrock_agent.types.orchestration_type

        out["orchestrationType"] = (
            aws_sdk_bedrock_agent.types.orchestration_type.serialize_json(
                value["orchestration_type"]
            )
        )
    if "custom_orchestration" in value:
        import aws_sdk_bedrock_agent.types.custom_orchestration

        out["customOrchestration"] = (
            aws_sdk_bedrock_agent.types.custom_orchestration.serialize_json(
                value["custom_orchestration"]
            )
        )
    out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    out["agentResourceRoleArn"] = value["agent_resource_role_arn"]
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["createdAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["created_at"]
    )
    import aws_sdk_bedrock_agent.types.date_timestamp

    out["updatedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
        value["updated_at"]
    )
    if "prepared_at" in value:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["preparedAt"] = aws_sdk_bedrock_agent.types.date_timestamp.serialize_json(
            value["prepared_at"]
        )
    if "failure_reasons" in value:
        import aws_sdk_bedrock_agent.types.failure_reasons

        out["failureReasons"] = (
            aws_sdk_bedrock_agent.types.failure_reasons.serialize_json(
                value["failure_reasons"]
            )
        )
    if "recommended_actions" in value:
        import aws_sdk_bedrock_agent.types.recommended_actions

        out["recommendedActions"] = (
            aws_sdk_bedrock_agent.types.recommended_actions.serialize_json(
                value["recommended_actions"]
            )
        )
    if "prompt_override_configuration" in value:
        import aws_sdk_bedrock_agent.types.prompt_override_configuration

        out["promptOverrideConfiguration"] = (
            aws_sdk_bedrock_agent.types.prompt_override_configuration.serialize_json(
                value["prompt_override_configuration"]
            )
        )
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "memory_configuration" in value:
        import aws_sdk_bedrock_agent.types.memory_configuration

        out["memoryConfiguration"] = (
            aws_sdk_bedrock_agent.types.memory_configuration.serialize_json(
                value["memory_configuration"]
            )
        )
    if "agent_collaboration" in value:
        import aws_sdk_bedrock_agent.types.agent_collaboration

        out["agentCollaboration"] = (
            aws_sdk_bedrock_agent.types.agent_collaboration.serialize_json(
                value["agent_collaboration"]
            )
        )
    return out


def deserialize_json(data: dict) -> Agent:
    out: Agent = {}  # type: ignore[typeddict-item]
    if "agentId" in data:
        out["agent_id"] = data["agentId"]
    else:
        raise DeserializationError("Agent.agent_id required")
    if "agentName" in data:
        out["agent_name"] = data["agentName"]
    else:
        raise DeserializationError("Agent.agent_name required")
    if "agentArn" in data:
        out["agent_arn"] = data["agentArn"]
    else:
        raise DeserializationError("Agent.agent_arn required")
    if "agentVersion" in data:
        out["agent_version"] = data["agentVersion"]
    else:
        raise DeserializationError("Agent.agent_version required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "instruction" in data:
        out["instruction"] = data["instruction"]
    if "agentStatus" in data:
        import aws_sdk_bedrock_agent.types.agent_status

        out["agent_status"] = aws_sdk_bedrock_agent.types.agent_status.deserialize_json(
            data["agentStatus"]
        )
    else:
        raise DeserializationError("Agent.agent_status required")
    if "foundationModel" in data:
        out["foundation_model"] = data["foundationModel"]
    if "description" in data:
        out["description"] = data["description"]
    if "orchestrationType" in data:
        import aws_sdk_bedrock_agent.types.orchestration_type

        out["orchestration_type"] = (
            aws_sdk_bedrock_agent.types.orchestration_type.deserialize_json(
                data["orchestrationType"]
            )
        )
    if "customOrchestration" in data:
        import aws_sdk_bedrock_agent.types.custom_orchestration

        out["custom_orchestration"] = (
            aws_sdk_bedrock_agent.types.custom_orchestration.deserialize_json(
                data["customOrchestration"]
            )
        )
    if "idleSessionTTLInSeconds" in data:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    else:
        raise DeserializationError("Agent.idle_session_ttl_in_seconds required")
    if "agentResourceRoleArn" in data:
        out["agent_resource_role_arn"] = data["agentResourceRoleArn"]
    else:
        raise DeserializationError("Agent.agent_resource_role_arn required")
    if "customerEncryptionKeyArn" in data:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if "createdAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["created_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("Agent.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["updated_at"] = aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
            data["updatedAt"]
        )
    else:
        raise DeserializationError("Agent.updated_at required")
    if "preparedAt" in data:
        import aws_sdk_bedrock_agent.types.date_timestamp

        out["prepared_at"] = (
            aws_sdk_bedrock_agent.types.date_timestamp.deserialize_json(
                data["preparedAt"]
            )
        )
    if "failureReasons" in data:
        import aws_sdk_bedrock_agent.types.failure_reasons

        out["failure_reasons"] = (
            aws_sdk_bedrock_agent.types.failure_reasons.deserialize_json(
                data["failureReasons"]
            )
        )
    if "recommendedActions" in data:
        import aws_sdk_bedrock_agent.types.recommended_actions

        out["recommended_actions"] = (
            aws_sdk_bedrock_agent.types.recommended_actions.deserialize_json(
                data["recommendedActions"]
            )
        )
    if "promptOverrideConfiguration" in data:
        import aws_sdk_bedrock_agent.types.prompt_override_configuration

        out["prompt_override_configuration"] = (
            aws_sdk_bedrock_agent.types.prompt_override_configuration.deserialize_json(
                data["promptOverrideConfiguration"]
            )
        )
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent.types.guardrail_configuration

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent.types.guardrail_configuration.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if "memoryConfiguration" in data:
        import aws_sdk_bedrock_agent.types.memory_configuration

        out["memory_configuration"] = (
            aws_sdk_bedrock_agent.types.memory_configuration.deserialize_json(
                data["memoryConfiguration"]
            )
        )
    if "agentCollaboration" in data:
        import aws_sdk_bedrock_agent.types.agent_collaboration

        out["agent_collaboration"] = (
            aws_sdk_bedrock_agent.types.agent_collaboration.deserialize_json(
                data["agentCollaboration"]
            )
        )
    return out
