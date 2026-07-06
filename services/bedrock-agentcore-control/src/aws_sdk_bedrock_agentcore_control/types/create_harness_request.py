"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CreateHarnessRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.client_token
    import aws_sdk_bedrock_agentcore_control.types.environment_variables_map
    import aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools
    import aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact
    import aws_sdk_bedrock_agentcore_control.types.harness_environment_provider_request
    import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration
    import aws_sdk_bedrock_agentcore_control.types.harness_model_configuration
    import aws_sdk_bedrock_agentcore_control.types.harness_name
    import aws_sdk_bedrock_agentcore_control.types.harness_skills
    import aws_sdk_bedrock_agentcore_control.types.harness_system_prompt
    import aws_sdk_bedrock_agentcore_control.types.harness_tools
    import aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration
    import aws_sdk_bedrock_agentcore_control.types.role_arn
    import aws_sdk_bedrock_agentcore_control.types.tags_map


class CreateHarnessRequest(TypedDict, closed=True):
    harness_name: "aws_sdk_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the harness. Must start with a letter and contain only alphanumeric characters and underscores.</p>"""
    client_token: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier to ensure idempotency of the request.</p>"""
    execution_role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>The ARN of the IAM role that the harness assumes when running. This role must have permissions for the services the agent needs to access, such as Amazon Bedrock for model invocation.</p>"""
    environment: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_environment_provider_request.HarnessEnvironmentProviderRequest"
    ]
    """<p>The compute environment configuration for the harness, including network and lifecycle settings.</p>"""
    environment_artifact: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
    ]
    """<p>The environment artifact for the harness, such as a custom container image containing additional dependencies.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables to set in the harness runtime environment.</p>"""
    authorizer_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    model: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
    ]
    """<p>The model configuration for the harness. Supports Amazon Bedrock, OpenAI, and Google Gemini model providers.</p>"""
    system_prompt: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
    ]
    """<p>The system prompt that defines the agent's behavior and instructions.</p>"""
    tools: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_tools.HarnessTools"
    ]
    """<p>The tools available to the agent, such as remote MCP servers, AgentCore Gateway, AgentCore Browser, Code Interpreter, or inline functions.</p>"""
    skills: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
    ]
    """<p>The skills available to the agent. Skills are bundles of files that the agent can pull into its context on demand.</p>"""
    allowed_tools: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
    ]
    """<p>The tools that the agent is allowed to use. Supports glob patterns such as * for all tools, @builtin for all built-in tools, or @serverName/toolName for specific MCP server tools.</p>"""
    memory: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
    ]
    """<p>The AgentCore Memory configuration for persisting conversation context across sessions.</p>"""
    truncation: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
    ]
    """<p>The truncation configuration for managing conversation context when it exceeds model limits.</p>"""
    max_iterations: NotRequired["int"]
    """<p>The maximum number of iterations the agent loop can execute per invocation.</p>"""
    max_tokens: NotRequired["int"]
    """<p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation.</p>"""
    timeout_seconds: NotRequired["int"]
    """<p>The maximum duration in seconds for the agent loop execution per invocation.</p>"""
    tags: NotRequired["aws_sdk_bedrock_agentcore_control.types.tags_map.TagsMap"]
    """<p>Tags to apply to the harness resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateHarnessRequest) -> dict:
    out: dict = {}
    out["harnessName"] = value["harness_name"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    out["executionRoleArn"] = value["execution_role_arn"]
    if "environment" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_environment_provider_request

        out["environment"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_environment_provider_request.serialize_json(
                value["environment"]
            )
        )
    if "environment_artifact" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact

        out["environmentArtifact"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact.serialize_json(
                value["environment_artifact"]
            )
        )
    if "environment_variables" in value:
        import aws_sdk_bedrock_agentcore_control.types.environment_variables_map

        out["environmentVariables"] = (
            aws_sdk_bedrock_agentcore_control.types.environment_variables_map.serialize_json(
                value["environment_variables"]
            )
        )
    if "authorizer_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizerConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.serialize_json(
                value["authorizer_configuration"]
            )
        )
    if "model" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_model_configuration

        out["model"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_model_configuration.serialize_json(
                value["model"]
            )
        )
    if "system_prompt" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_system_prompt

        out["systemPrompt"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_system_prompt.serialize_json(
                value["system_prompt"]
            )
        )
    if "tools" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_tools

        out["tools"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_tools.serialize_json(
                value["tools"]
            )
        )
    if "skills" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_skills

        out["skills"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_skills.serialize_json(
                value["skills"]
            )
        )
    if "allowed_tools" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools

        out["allowedTools"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools.serialize_json(
                value["allowed_tools"]
            )
        )
    if "memory" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.serialize_json(
                value["memory"]
            )
        )
    if "truncation" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration

        out["truncation"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration.serialize_json(
                value["truncation"]
            )
        )
    if "max_iterations" in value:
        out["maxIterations"] = value["max_iterations"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "tags" in value:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateHarnessRequest:
    out: CreateHarnessRequest = {}  # type: ignore[typeddict-item]
    if "harnessName" in data:
        out["harness_name"] = data["harnessName"]
    else:
        raise DeserializationError("CreateHarnessRequest.harness_name required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("CreateHarnessRequest.execution_role_arn required")
    if "environment" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_environment_provider_request

        out["environment"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_environment_provider_request.deserialize_json(
                data["environment"]
            )
        )
    if "environmentArtifact" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact

        out["environment_artifact"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact.deserialize_json(
                data["environmentArtifact"]
            )
        )
    if "environmentVariables" in data:
        import aws_sdk_bedrock_agentcore_control.types.environment_variables_map

        out["environment_variables"] = (
            aws_sdk_bedrock_agentcore_control.types.environment_variables_map.deserialize_json(
                data["environmentVariables"]
            )
        )
    if "authorizerConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration

        out["authorizer_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.deserialize_json(
                data["authorizerConfiguration"]
            )
        )
    if "model" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_model_configuration

        out["model"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_model_configuration.deserialize_json(
                data["model"]
            )
        )
    if "systemPrompt" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_system_prompt

        out["system_prompt"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_system_prompt.deserialize_json(
                data["systemPrompt"]
            )
        )
    if "tools" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_tools

        out["tools"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_tools.deserialize_json(
                data["tools"]
            )
        )
    if "skills" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_skills

        out["skills"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_skills.deserialize_json(
                data["skills"]
            )
        )
    if "allowedTools" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools

        out["allowed_tools"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools.deserialize_json(
                data["allowedTools"]
            )
        )
    if "memory" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.deserialize_json(
                data["memory"]
            )
        )
    if "truncation" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration

        out["truncation"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration.deserialize_json(
                data["truncation"]
            )
        )
    if "maxIterations" in data:
        out["max_iterations"] = data["maxIterations"]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "timeoutSeconds" in data:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if "tags" in data:
        import aws_sdk_bedrock_agentcore_control.types.tags_map

        out["tags"] = aws_sdk_bedrock_agentcore_control.types.tags_map.deserialize_json(
            data["tags"]
        )
    return out
