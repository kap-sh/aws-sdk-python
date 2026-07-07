"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#Harness``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.authorizer_configuration
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp
    import aws_sdk_bedrock_agentcore_control.types.environment_variables_map
    import aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools
    import aws_sdk_bedrock_agentcore_control.types.harness_arn
    import aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact
    import aws_sdk_bedrock_agentcore_control.types.harness_environment_provider
    import aws_sdk_bedrock_agentcore_control.types.harness_id
    import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration
    import aws_sdk_bedrock_agentcore_control.types.harness_model_configuration
    import aws_sdk_bedrock_agentcore_control.types.harness_name
    import aws_sdk_bedrock_agentcore_control.types.harness_skills
    import aws_sdk_bedrock_agentcore_control.types.harness_status
    import aws_sdk_bedrock_agentcore_control.types.harness_system_prompt
    import aws_sdk_bedrock_agentcore_control.types.harness_tools
    import aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration
    import aws_sdk_bedrock_agentcore_control.types.role_arn


class Harness(TypedDict, closed=True):
    harness_id: "aws_sdk_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the Harness.</p>"""
    harness_name: "aws_sdk_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the Harness.</p>"""
    arn: "aws_sdk_bedrock_agentcore_control.types.harness_arn.HarnessArn"
    """<p>The ARN of the Harness.</p>"""
    status: "aws_sdk_bedrock_agentcore_control.types.harness_status.HarnessStatus"
    """<p>The status of the Harness.</p>"""
    execution_role_arn: "aws_sdk_bedrock_agentcore_control.types.role_arn.RoleArn"
    """<p>IAM role the Harness assumes when running.</p>"""
    created_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The createdAt time of the Harness.</p>"""
    updated_at: "aws_sdk_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The updatedAt time of the Harness.</p>"""
    model: "aws_sdk_bedrock_agentcore_control.types.harness_model_configuration.HarnessModelConfiguration"
    """<p>The configuration of the default model used by the Harness.</p>"""
    system_prompt: "aws_sdk_bedrock_agentcore_control.types.harness_system_prompt.HarnessSystemPrompt"
    """<p>The system prompt of the Harness.</p>"""
    tools: "aws_sdk_bedrock_agentcore_control.types.harness_tools.HarnessTools"
    """<p>The tools of the Harness.</p>"""
    skills: "aws_sdk_bedrock_agentcore_control.types.harness_skills.HarnessSkills"
    """<p>The skills of the Harness.</p>"""
    allowed_tools: "aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools.HarnessAllowedTools"
    """<p>The allowed tools of the Harness. All tools are allowed by default.</p>"""
    truncation: "aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration.HarnessTruncationConfiguration"
    """<p>Configuration for truncating model context.</p>"""
    environment: "aws_sdk_bedrock_agentcore_control.types.harness_environment_provider.HarnessEnvironmentProvider"
    """<p>The compute environment on which the Harness runs.</p>"""
    environment_artifact: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_environment_artifact.HarnessEnvironmentArtifact"
    ]
    """<p>The environment artifact (e.g., container) in which the Harness operates.</p>"""
    environment_variables: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.environment_variables_map.EnvironmentVariablesMap"
    ]
    """<p>Environment variables exposed in the environment in which the Harness operates.</p>"""
    authorizer_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.authorizer_configuration.AuthorizerConfiguration"
    ]
    memory: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
    ]
    """<p>AgentCore Memory instance configuration for short and long term memory.</p>"""
    max_iterations: NotRequired["int"]
    """<p>The maximum number of iterations in the agent loop allowed before exiting per invocation.</p>"""
    max_tokens: NotRequired["int"]
    """<p>The maximum total number of output tokens the agent can generate across all model calls within a single invocation.</p>"""
    timeout_seconds: NotRequired["int"]
    """<p>The maximum duration per invocation.</p>"""
    failure_reason: NotRequired["str"]
    """<p>Reason why create or update operations fail.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Harness) -> dict:
    out: dict = {}
    out["harnessId"] = value["harness_id"]
    out["harnessName"] = value["harness_name"]
    out["arn"] = value["arn"]
    import aws_sdk_bedrock_agentcore_control.types.harness_status

    out["status"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_status.serialize_json(
            value["status"]
        )
    )
    out["executionRoleArn"] = value["execution_role_arn"]
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        aws_sdk_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.harness_model_configuration

    out["model"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_model_configuration.serialize_json(
            value["model"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.harness_system_prompt

    out["systemPrompt"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_system_prompt.serialize_json(
            value["system_prompt"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.harness_tools

    out["tools"] = aws_sdk_bedrock_agentcore_control.types.harness_tools.serialize_json(
        value["tools"]
    )
    import aws_sdk_bedrock_agentcore_control.types.harness_skills

    out["skills"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_skills.serialize_json(
            value["skills"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools

    out["allowedTools"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools.serialize_json(
            value["allowed_tools"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration

    out["truncation"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration.serialize_json(
            value["truncation"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.harness_environment_provider

    out["environment"] = (
        aws_sdk_bedrock_agentcore_control.types.harness_environment_provider.serialize_json(
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
    if "memory" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.serialize_json(
                value["memory"]
            )
        )
    if "max_iterations" in value:
        out["maxIterations"] = value["max_iterations"]
    if "max_tokens" in value:
        out["maxTokens"] = value["max_tokens"]
    if "timeout_seconds" in value:
        out["timeoutSeconds"] = value["timeout_seconds"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> Harness:
    out: Harness = {}  # type: ignore[typeddict-item]
    if "harnessId" in data:
        out["harness_id"] = data["harnessId"]
    else:
        raise DeserializationError("Harness.harness_id required")
    if "harnessName" in data:
        out["harness_name"] = data["harnessName"]
    else:
        raise DeserializationError("Harness.harness_name required")
    if "arn" in data:
        out["arn"] = data["arn"]
    else:
        raise DeserializationError("Harness.arn required")
    if "status" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_status

        out["status"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_status.deserialize_json(
                data["status"]
            )
        )
    else:
        raise DeserializationError("Harness.status required")
    if "executionRoleArn" in data:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        raise DeserializationError("Harness.execution_role_arn required")
    if "createdAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        raise DeserializationError("Harness.created_at required")
    if "updatedAt" in data:
        import aws_sdk_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            aws_sdk_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        raise DeserializationError("Harness.updated_at required")
    if "model" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_model_configuration

        out["model"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_model_configuration.deserialize_json(
                data["model"]
            )
        )
    else:
        raise DeserializationError("Harness.model required")
    if "systemPrompt" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_system_prompt

        out["system_prompt"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_system_prompt.deserialize_json(
                data["systemPrompt"]
            )
        )
    else:
        raise DeserializationError("Harness.system_prompt required")
    if "tools" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_tools

        out["tools"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_tools.deserialize_json(
                data["tools"]
            )
        )
    else:
        raise DeserializationError("Harness.tools required")
    if "skills" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_skills

        out["skills"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_skills.deserialize_json(
                data["skills"]
            )
        )
    else:
        raise DeserializationError("Harness.skills required")
    if "allowedTools" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools

        out["allowed_tools"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_allowed_tools.deserialize_json(
                data["allowedTools"]
            )
        )
    else:
        raise DeserializationError("Harness.allowed_tools required")
    if "truncation" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration

        out["truncation"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_truncation_configuration.deserialize_json(
                data["truncation"]
            )
        )
    else:
        raise DeserializationError("Harness.truncation required")
    if "environment" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_environment_provider

        out["environment"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_environment_provider.deserialize_json(
                data["environment"]
            )
        )
    else:
        raise DeserializationError("Harness.environment required")
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
    if "memory" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration

        out["memory"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.deserialize_json(
                data["memory"]
            )
        )
    if "maxIterations" in data:
        out["max_iterations"] = data["maxIterations"]
    if "maxTokens" in data:
        out["max_tokens"] = data["maxTokens"]
    if "timeoutSeconds" in data:
        out["timeout_seconds"] = data["timeoutSeconds"]
    if "failureReason" in data:
        out["failure_reason"] = data["failureReason"]
    return out
