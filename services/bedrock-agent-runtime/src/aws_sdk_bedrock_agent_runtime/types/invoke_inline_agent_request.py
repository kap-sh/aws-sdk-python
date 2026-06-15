"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#InvokeInlineAgentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agent_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.agent_action_groups
    import aws_sdk_bedrock_agent_runtime.types.agent_collaboration
    import aws_sdk_bedrock_agent_runtime.types.collaborator_configurations
    import aws_sdk_bedrock_agent_runtime.types.collaborators
    import aws_sdk_bedrock_agent_runtime.types.custom_orchestration
    import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration_with_arn
    import aws_sdk_bedrock_agent_runtime.types.inline_bedrock_model_configurations
    import aws_sdk_bedrock_agent_runtime.types.inline_session_state
    import aws_sdk_bedrock_agent_runtime.types.input_text
    import aws_sdk_bedrock_agent_runtime.types.instruction
    import aws_sdk_bedrock_agent_runtime.types.kms_key_arn
    import aws_sdk_bedrock_agent_runtime.types.knowledge_bases
    import aws_sdk_bedrock_agent_runtime.types.model_identifier
    import aws_sdk_bedrock_agent_runtime.types.name
    import aws_sdk_bedrock_agent_runtime.types.orchestration_type
    import aws_sdk_bedrock_agent_runtime.types.prompt_creation_configurations
    import aws_sdk_bedrock_agent_runtime.types.prompt_override_configuration
    import aws_sdk_bedrock_agent_runtime.types.session_id
    import aws_sdk_bedrock_agent_runtime.types.session_ttl
    import aws_sdk_bedrock_agent_runtime.types.streaming_configurations


class InvokeInlineAgentRequest(TypedDict):
    customer_encryption_key_arn: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.kms_key_arn.KmsKeyArn"
    ]
    """<p> The Amazon Resource Name (ARN) of the Amazon Web Services KMS key to use to encrypt your inline agent. </p>"""
    foundation_model: (
        "aws_sdk_bedrock_agent_runtime.types.model_identifier.ModelIdentifier"
    )
    r"""<p> The <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html#model-ids-arns\">model identifier (ID)</a> of the model to use for orchestration by the inline agent. For example, <code>meta.llama3-1-70b-instruct-v1:0</code>. </p>"""
    instruction: "aws_sdk_bedrock_agent_runtime.types.instruction.Instruction"
    """<p> The instructions that tell the inline agent what it should do and how it should interact with users. </p>"""
    idle_session_ttl_in_seconds: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.session_ttl.SessionTTL"
    ]
    """<p> The number of seconds for which the inline agent should maintain session information. After this time expires, the subsequent <code>InvokeInlineAgent</code> request begins a new session. </p> <p>A user interaction remains active for the amount of time specified. If no conversation occurs during this time, the session expires and the data provided before the timeout is deleted.</p>"""
    action_groups: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_action_groups.AgentActionGroups"
    ]
    """<p> A list of action groups with each action group defining the action the inline agent needs to carry out. </p>"""
    knowledge_bases: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.knowledge_bases.KnowledgeBases"
    ]
    """<p> Contains information of the knowledge bases to associate with. </p>"""
    guardrail_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.guardrail_configuration_with_arn.GuardrailConfigurationWithArn"
    ]
    r"""<p> The <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html\">guardrails</a> to assign to the inline agent. </p>"""
    prompt_override_configuration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.prompt_override_configuration.PromptOverrideConfiguration"
    ]
    """<p> Configurations for advanced prompts used to override the default prompts to enhance the accuracy of the inline agent. </p>"""
    agent_collaboration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.agent_collaboration.AgentCollaboration"
    ]
    """<p> Defines how the inline collaborator agent handles information across multiple collaborator agents to coordinate a final response. The inline collaborator agent can also be the supervisor. </p>"""
    collaborator_configurations: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.collaborator_configurations.CollaboratorConfigurations"
    ]
    r"""<p> Settings for an inline agent collaborator called with <a href=\"https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_InvokeInlineAgent.html\">InvokeInlineAgent</a>. </p>"""
    agent_name: NotRequired["aws_sdk_bedrock_agent_runtime.types.name.Name"]
    """<p>The name for the agent.</p>"""
    session_id: "aws_sdk_bedrock_agent_runtime.types.session_id.SessionId"
    """<p> The unique identifier of the session. Use the same value across requests to continue the same conversation. </p>"""
    end_session: NotRequired["bool"]
    """<p> Specifies whether to end the session with the inline agent or not. </p>"""
    enable_trace: NotRequired["bool"]
    r"""<p> Specifies whether to turn on the trace or not to track the agent's reasoning process. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/trace-events.html\">Using trace</a>. </p>"""
    input_text: NotRequired["aws_sdk_bedrock_agent_runtime.types.input_text.InputText"]
    """<p> The prompt text to send to the agent. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>"""
    streaming_configurations: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.streaming_configurations.StreamingConfigurations"
    ]
    """<p> Specifies the configurations for streaming. </p> <note> <p>To use agent streaming, you need permissions to perform the <code>bedrock:InvokeModelWithResponseStream</code> action.</p> </note>"""
    prompt_creation_configurations: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.prompt_creation_configurations.PromptCreationConfigurations"
    ]
    """<p>Specifies parameters that control how the service populates the agent prompt for an <code>InvokeInlineAgent</code> request. You can control which aspects of previous invocations in the same agent session the service uses to populate the agent prompt. This gives you more granular control over the contextual history that is used to process the current request.</p>"""
    inline_session_state: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.inline_session_state.InlineSessionState"
    ]
    r"""<p> Parameters that specify the various attributes of a sessions. You can include attributes for the session or prompt or, if you configured an action group to return control, results from invocation of the action group. For more information, see <a href=\"https://docs.aws.amazon.com/bedrock/latest/userguide/agents-session-state.html\">Control session context</a>. </p> <note> <p>If you include <code>returnControlInvocationResults</code> in the <code>sessionState</code> field, the <code>inputText</code> field will be ignored.</p> </note>"""
    collaborators: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.collaborators.Collaborators"
    ]
    """<p> List of collaborator inline agents. </p>"""
    bedrock_model_configurations: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.inline_bedrock_model_configurations.InlineBedrockModelConfigurations"
    ]
    """<p>Model settings for the request.</p>"""
    orchestration_type: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.orchestration_type.OrchestrationType"
    ]
    """<p>Specifies the type of orchestration strategy for the agent. This is set to DEFAULT orchestration type, by default. </p>"""
    custom_orchestration: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.custom_orchestration.CustomOrchestration"
    ]
    """<p>Contains details of the custom orchestration configured for the agent. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeInlineAgentRequest) -> dict:
    out: dict = {}
    if "customer_encryption_key_arn" in value:
        out["customerEncryptionKeyArn"] = value["customer_encryption_key_arn"]
    out["foundationModel"] = value["foundation_model"]
    out["instruction"] = value["instruction"]
    if "idle_session_ttl_in_seconds" in value:
        out["idleSessionTTLInSeconds"] = value["idle_session_ttl_in_seconds"]
    if "action_groups" in value:
        import aws_sdk_bedrock_agent_runtime.types.agent_action_groups

        out["actionGroups"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_action_groups.serialize_json(
                value["action_groups"]
            )
        )
    if "knowledge_bases" in value:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_bases

        out["knowledgeBases"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_bases.serialize_json(
                value["knowledge_bases"]
            )
        )
    if "guardrail_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration_with_arn

        out["guardrailConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_configuration_with_arn.serialize_json(
                value["guardrail_configuration"]
            )
        )
    if "prompt_override_configuration" in value:
        import aws_sdk_bedrock_agent_runtime.types.prompt_override_configuration

        out["promptOverrideConfiguration"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_override_configuration.serialize_json(
                value["prompt_override_configuration"]
            )
        )
    if "agent_collaboration" in value:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaboration

        out["agentCollaboration"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaboration.serialize_json(
                value["agent_collaboration"]
            )
        )
    if "collaborator_configurations" in value:
        import aws_sdk_bedrock_agent_runtime.types.collaborator_configurations

        out["collaboratorConfigurations"] = (
            aws_sdk_bedrock_agent_runtime.types.collaborator_configurations.serialize_json(
                value["collaborator_configurations"]
            )
        )
    if "agent_name" in value:
        out["agentName"] = value["agent_name"]
    if "end_session" in value:
        out["endSession"] = value["end_session"]
    if "enable_trace" in value:
        out["enableTrace"] = value["enable_trace"]
    if "input_text" in value:
        out["inputText"] = value["input_text"]
    if "streaming_configurations" in value:
        import aws_sdk_bedrock_agent_runtime.types.streaming_configurations

        out["streamingConfigurations"] = (
            aws_sdk_bedrock_agent_runtime.types.streaming_configurations.serialize_json(
                value["streaming_configurations"]
            )
        )
    if "prompt_creation_configurations" in value:
        import aws_sdk_bedrock_agent_runtime.types.prompt_creation_configurations

        out["promptCreationConfigurations"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_creation_configurations.serialize_json(
                value["prompt_creation_configurations"]
            )
        )
    if "inline_session_state" in value:
        import aws_sdk_bedrock_agent_runtime.types.inline_session_state

        out["inlineSessionState"] = (
            aws_sdk_bedrock_agent_runtime.types.inline_session_state.serialize_json(
                value["inline_session_state"]
            )
        )
    if "collaborators" in value:
        import aws_sdk_bedrock_agent_runtime.types.collaborators

        out["collaborators"] = (
            aws_sdk_bedrock_agent_runtime.types.collaborators.serialize_json(
                value["collaborators"]
            )
        )
    if "bedrock_model_configurations" in value:
        import aws_sdk_bedrock_agent_runtime.types.inline_bedrock_model_configurations

        out["bedrockModelConfigurations"] = (
            aws_sdk_bedrock_agent_runtime.types.inline_bedrock_model_configurations.serialize_json(
                value["bedrock_model_configurations"]
            )
        )
    if "orchestration_type" in value:
        import aws_sdk_bedrock_agent_runtime.types.orchestration_type

        out["orchestrationType"] = (
            aws_sdk_bedrock_agent_runtime.types.orchestration_type.serialize_json(
                value["orchestration_type"]
            )
        )
    if "custom_orchestration" in value:
        import aws_sdk_bedrock_agent_runtime.types.custom_orchestration

        out["customOrchestration"] = (
            aws_sdk_bedrock_agent_runtime.types.custom_orchestration.serialize_json(
                value["custom_orchestration"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvokeInlineAgentRequest:
    out: InvokeInlineAgentRequest = {}  # type: ignore[typeddict-item]
    if "customerEncryptionKeyArn" in data:
        out["customer_encryption_key_arn"] = data["customerEncryptionKeyArn"]
    if "foundationModel" in data:
        out["foundation_model"] = data["foundationModel"]
    else:
        raise DeserializationError("InvokeInlineAgentRequest.foundation_model required")
    if "instruction" in data:
        out["instruction"] = data["instruction"]
    else:
        raise DeserializationError("InvokeInlineAgentRequest.instruction required")
    if "idleSessionTTLInSeconds" in data:
        out["idle_session_ttl_in_seconds"] = data["idleSessionTTLInSeconds"]
    if "actionGroups" in data:
        import aws_sdk_bedrock_agent_runtime.types.agent_action_groups

        out["action_groups"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_action_groups.deserialize_json(
                data["actionGroups"]
            )
        )
    if "knowledgeBases" in data:
        import aws_sdk_bedrock_agent_runtime.types.knowledge_bases

        out["knowledge_bases"] = (
            aws_sdk_bedrock_agent_runtime.types.knowledge_bases.deserialize_json(
                data["knowledgeBases"]
            )
        )
    if "guardrailConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.guardrail_configuration_with_arn

        out["guardrail_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.guardrail_configuration_with_arn.deserialize_json(
                data["guardrailConfiguration"]
            )
        )
    if "promptOverrideConfiguration" in data:
        import aws_sdk_bedrock_agent_runtime.types.prompt_override_configuration

        out["prompt_override_configuration"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_override_configuration.deserialize_json(
                data["promptOverrideConfiguration"]
            )
        )
    if "agentCollaboration" in data:
        import aws_sdk_bedrock_agent_runtime.types.agent_collaboration

        out["agent_collaboration"] = (
            aws_sdk_bedrock_agent_runtime.types.agent_collaboration.deserialize_json(
                data["agentCollaboration"]
            )
        )
    if "collaboratorConfigurations" in data:
        import aws_sdk_bedrock_agent_runtime.types.collaborator_configurations

        out["collaborator_configurations"] = (
            aws_sdk_bedrock_agent_runtime.types.collaborator_configurations.deserialize_json(
                data["collaboratorConfigurations"]
            )
        )
    if "agentName" in data:
        out["agent_name"] = data["agentName"]
    if "endSession" in data:
        out["end_session"] = data["endSession"]
    if "enableTrace" in data:
        out["enable_trace"] = data["enableTrace"]
    if "inputText" in data:
        out["input_text"] = data["inputText"]
    if "streamingConfigurations" in data:
        import aws_sdk_bedrock_agent_runtime.types.streaming_configurations

        out["streaming_configurations"] = (
            aws_sdk_bedrock_agent_runtime.types.streaming_configurations.deserialize_json(
                data["streamingConfigurations"]
            )
        )
    if "promptCreationConfigurations" in data:
        import aws_sdk_bedrock_agent_runtime.types.prompt_creation_configurations

        out["prompt_creation_configurations"] = (
            aws_sdk_bedrock_agent_runtime.types.prompt_creation_configurations.deserialize_json(
                data["promptCreationConfigurations"]
            )
        )
    if "inlineSessionState" in data:
        import aws_sdk_bedrock_agent_runtime.types.inline_session_state

        out["inline_session_state"] = (
            aws_sdk_bedrock_agent_runtime.types.inline_session_state.deserialize_json(
                data["inlineSessionState"]
            )
        )
    if "collaborators" in data:
        import aws_sdk_bedrock_agent_runtime.types.collaborators

        out["collaborators"] = (
            aws_sdk_bedrock_agent_runtime.types.collaborators.deserialize_json(
                data["collaborators"]
            )
        )
    if "bedrockModelConfigurations" in data:
        import aws_sdk_bedrock_agent_runtime.types.inline_bedrock_model_configurations

        out["bedrock_model_configurations"] = (
            aws_sdk_bedrock_agent_runtime.types.inline_bedrock_model_configurations.deserialize_json(
                data["bedrockModelConfigurations"]
            )
        )
    if "orchestrationType" in data:
        import aws_sdk_bedrock_agent_runtime.types.orchestration_type

        out["orchestration_type"] = (
            aws_sdk_bedrock_agent_runtime.types.orchestration_type.deserialize_json(
                data["orchestrationType"]
            )
        )
    if "customOrchestration" in data:
        import aws_sdk_bedrock_agent_runtime.types.custom_orchestration

        out["custom_orchestration"] = (
            aws_sdk_bedrock_agent_runtime.types.custom_orchestration.deserialize_json(
                data["customOrchestration"]
            )
        )
    return out
