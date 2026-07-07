"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeHarnessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore.types.harness_allowed_tools
    import aws_sdk_bedrock_agentcore.types.harness_arn
    import aws_sdk_bedrock_agentcore.types.harness_messages
    import aws_sdk_bedrock_agentcore.types.harness_model_configuration
    import aws_sdk_bedrock_agentcore.types.harness_skills
    import aws_sdk_bedrock_agentcore.types.harness_system_prompt
    import aws_sdk_bedrock_agentcore.types.harness_tools
    import aws_sdk_bedrock_agentcore.types.session_id


class InvokeHarnessRequest(TypedDict, closed=True):
    harness_arn: "aws_sdk_bedrock_agentcore.types.harness_arn.HarnessArn"
    """<p>The ARN of the harness to invoke.</p>"""
    runtime_session_id: "aws_sdk_bedrock_agentcore.types.session_id.SessionId"
    """<p>The session ID for the invocation. Use the same session ID across requests to continue a conversation.</p>"""
    runtime_user_id: NotRequired["str"]
    """<p>An identifier for the end user making the request. This value is passed through to the runtime container.</p>"""
    messages: "aws_sdk_bedrock_agentcore.types.harness_messages.HarnessMessages"
    """<p>The messages to send to the agent.</p>"""
    model: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_model_configuration.HarnessModelConfiguration"
    ]
    """<p>The model configuration to use for this invocation. If specified, overrides the harness default.</p>"""
    system_prompt: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_system_prompt.HarnessSystemPrompt"
    ]
    """<p>The system prompt to use for this invocation. If specified, overrides the harness default.</p>"""
    tools: NotRequired["aws_sdk_bedrock_agentcore.types.harness_tools.HarnessTools"]
    """<p>The tools available to the agent for this invocation. If specified, overrides the harness default.</p>"""
    skills: NotRequired["aws_sdk_bedrock_agentcore.types.harness_skills.HarnessSkills"]
    """<p>The skills available to the agent for this invocation. If specified, overrides the harness default.</p>"""
    allowed_tools: NotRequired[
        "aws_sdk_bedrock_agentcore.types.harness_allowed_tools.HarnessAllowedTools"
    ]
    """<p>The tools that the agent is allowed to use for this invocation. If specified, overrides the harness default.</p>"""
    max_iterations: NotRequired["int"]
    """<p>The maximum number of iterations the agent loop can execute. If specified, overrides the harness default.</p>"""
    max_tokens: NotRequired["int"]
    """<p>The maximum number of tokens the agent can generate per iteration. If specified, overrides the harness default.</p>"""
    timeout_seconds: NotRequired["int"]
    """<p>The maximum duration in seconds for the agent loop execution. If specified, overrides the harness default.</p>"""
    actor_id: NotRequired["str"]
    """<p>The actor ID for memory operations. Overrides the actor ID configured on the harness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeHarnessRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore.types.harness_messages

    out["messages"] = aws_sdk_bedrock_agentcore.types.harness_messages.serialize_json(
        value["messages"]
    )
    if "model" in value:
        import aws_sdk_bedrock_agentcore.types.harness_model_configuration

        out["model"] = (
            aws_sdk_bedrock_agentcore.types.harness_model_configuration.serialize_json(
                value["model"]
            )
        )
    if "system_prompt" in value:
        import aws_sdk_bedrock_agentcore.types.harness_system_prompt

        out["systemPrompt"] = (
            aws_sdk_bedrock_agentcore.types.harness_system_prompt.serialize_json(
                value["system_prompt"]
            )
        )
    if "tools" in value:
        import aws_sdk_bedrock_agentcore.types.harness_tools

        out["tools"] = aws_sdk_bedrock_agentcore.types.harness_tools.serialize_json(
            value["tools"]
        )
    if "skills" in value:
        import aws_sdk_bedrock_agentcore.types.harness_skills

        out["skills"] = aws_sdk_bedrock_agentcore.types.harness_skills.serialize_json(
            value["skills"]
        )
    if "allowed_tools" in value:
        import aws_sdk_bedrock_agentcore.types.harness_allowed_tools

        out["allowedTools"] = (
            aws_sdk_bedrock_agentcore.types.harness_allowed_tools.serialize_json(
                value["allowed_tools"]
            )
        )
    if "max_iterations" in value:
        out["maxIterations"] = value["max_iterations"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "actor_id" in value:
        out["actorId"] = value["actor_id"]
    return out


def deserialize_json(data: dict) -> InvokeHarnessRequest:
    out: InvokeHarnessRequest = {}  # type: ignore[typeddict-item]
    if "messages" in data:
        import aws_sdk_bedrock_agentcore.types.harness_messages

        out["messages"] = (
            aws_sdk_bedrock_agentcore.types.harness_messages.deserialize_json(
                data["messages"]
            )
        )
    else:
        raise DeserializationError("InvokeHarnessRequest.messages required")
    if "model" in data:
        import aws_sdk_bedrock_agentcore.types.harness_model_configuration

        out["model"] = (
            aws_sdk_bedrock_agentcore.types.harness_model_configuration.deserialize_json(
                data["model"]
            )
        )
    if "systemPrompt" in data:
        import aws_sdk_bedrock_agentcore.types.harness_system_prompt

        out["system_prompt"] = (
            aws_sdk_bedrock_agentcore.types.harness_system_prompt.deserialize_json(
                data["systemPrompt"]
            )
        )
    if "tools" in data:
        import aws_sdk_bedrock_agentcore.types.harness_tools

        out["tools"] = aws_sdk_bedrock_agentcore.types.harness_tools.deserialize_json(
            data["tools"]
        )
    if "skills" in data:
        import aws_sdk_bedrock_agentcore.types.harness_skills

        out["skills"] = aws_sdk_bedrock_agentcore.types.harness_skills.deserialize_json(
            data["skills"]
        )
    if "allowedTools" in data:
        import aws_sdk_bedrock_agentcore.types.harness_allowed_tools

        out["allowed_tools"] = (
            aws_sdk_bedrock_agentcore.types.harness_allowed_tools.deserialize_json(
                data["allowedTools"]
            )
        )
    if "maxIterations" in data:
        out["max_iterations"] = data["maxIterations"]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "timeoutSeconds" in data:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if "actorId" in data:
        out["actor_id"] = data["actorId"]
    return out
