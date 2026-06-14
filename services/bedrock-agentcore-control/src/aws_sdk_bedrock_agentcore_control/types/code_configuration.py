"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.agent_managed_runtime_type
    import aws_sdk_bedrock_agentcore_control.types.code
    import aws_sdk_bedrock_agentcore_control.types.entry_points


class CodeConfiguration(TypedDict):
    code: "aws_sdk_bedrock_agentcore_control.types.code.Code"
    """<p>The source code location and configuration details.</p>"""
    runtime: "aws_sdk_bedrock_agentcore_control.types.agent_managed_runtime_type.AgentManagedRuntimeType"
    """<p>The runtime environment for executing the agent code. Specify the programming language and version to use for the agent runtime. For valid values, see the list of supported runtimes.</p>"""
    entry_point: "aws_sdk_bedrock_agentcore_control.types.entry_points.EntryPoints"
    """<p>The entry point for the code execution, specifying the function or method that should be invoked when the code runs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.code

    out["code"] = aws_sdk_bedrock_agentcore_control.types.code.serialize_json(
        value["code"]
    )
    import aws_sdk_bedrock_agentcore_control.types.agent_managed_runtime_type

    out["runtime"] = (
        aws_sdk_bedrock_agentcore_control.types.agent_managed_runtime_type.serialize_json(
            value["runtime"]
        )
    )
    import aws_sdk_bedrock_agentcore_control.types.entry_points

    out["entryPoint"] = (
        aws_sdk_bedrock_agentcore_control.types.entry_points.serialize_json(
            value["entry_point"]
        )
    )
    return out


def deserialize_json(data: dict) -> CodeConfiguration:
    out: CodeConfiguration = {}  # type: ignore[typeddict-item]
    if "code" in data:
        import aws_sdk_bedrock_agentcore_control.types.code

        out["code"] = aws_sdk_bedrock_agentcore_control.types.code.deserialize_json(
            data["code"]
        )
    else:
        raise DeserializationError("CodeConfiguration.code required")
    if "runtime" in data:
        import aws_sdk_bedrock_agentcore_control.types.agent_managed_runtime_type

        out["runtime"] = (
            aws_sdk_bedrock_agentcore_control.types.agent_managed_runtime_type.deserialize_json(
                data["runtime"]
            )
        )
    else:
        raise DeserializationError("CodeConfiguration.runtime required")
    if "entryPoint" in data:
        import aws_sdk_bedrock_agentcore_control.types.entry_points

        out["entry_point"] = (
            aws_sdk_bedrock_agentcore_control.types.entry_points.deserialize_json(
                data["entryPoint"]
            )
        )
    else:
        raise DeserializationError("CodeConfiguration.entry_point required")
    return out
