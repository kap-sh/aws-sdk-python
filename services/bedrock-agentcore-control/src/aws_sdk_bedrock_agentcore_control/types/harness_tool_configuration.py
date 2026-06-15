"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessToolConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias, TypedDict

from aws_sdk_bedrock_agentcore_control.errors import (
    DeserializationError,
    SerializationError,
)

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_browser_config
    import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config
    import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_gateway_config
    import aws_sdk_bedrock_agentcore_control.types.harness_inline_function_config
    import aws_sdk_bedrock_agentcore_control.types.harness_remote_mcp_config


class _HarnessToolConfiguration_remoteMcp(TypedDict):
    remoteMcp: "aws_sdk_bedrock_agentcore_control.types.harness_remote_mcp_config.HarnessRemoteMcpConfig"


class _HarnessToolConfiguration_agentCoreBrowser(TypedDict):
    agentCoreBrowser: "aws_sdk_bedrock_agentcore_control.types.harness_agent_core_browser_config.HarnessAgentCoreBrowserConfig"


class _HarnessToolConfiguration_agentCoreGateway(TypedDict):
    agentCoreGateway: "aws_sdk_bedrock_agentcore_control.types.harness_agent_core_gateway_config.HarnessAgentCoreGatewayConfig"


class _HarnessToolConfiguration_inlineFunction(TypedDict):
    inlineFunction: "aws_sdk_bedrock_agentcore_control.types.harness_inline_function_config.HarnessInlineFunctionConfig"


class _HarnessToolConfiguration_agentCoreCodeInterpreter(TypedDict):
    agentCoreCodeInterpreter: "aws_sdk_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config.HarnessAgentCoreCodeInterpreterConfig"


HarnessToolConfiguration: TypeAlias = (
    _HarnessToolConfiguration_remoteMcp
    | _HarnessToolConfiguration_agentCoreBrowser
    | _HarnessToolConfiguration_agentCoreGateway
    | _HarnessToolConfiguration_inlineFunction
    | _HarnessToolConfiguration_agentCoreCodeInterpreter
)


# --- restJson1 ser/de ---
def serialize_json(value: HarnessToolConfiguration) -> dict:
    if "remoteMcp" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_remote_mcp_config

        return {
            "remoteMcp": aws_sdk_bedrock_agentcore_control.types.harness_remote_mcp_config.serialize_json(
                value["remoteMcp"]
            )
        }
    elif "agentCoreBrowser" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_browser_config

        return {
            "agentCoreBrowser": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_browser_config.serialize_json(
                value["agentCoreBrowser"]
            )
        }
    elif "agentCoreGateway" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_gateway_config

        return {
            "agentCoreGateway": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_gateway_config.serialize_json(
                value["agentCoreGateway"]
            )
        }
    elif "inlineFunction" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_inline_function_config

        return {
            "inlineFunction": aws_sdk_bedrock_agentcore_control.types.harness_inline_function_config.serialize_json(
                value["inlineFunction"]
            )
        }
    elif "agentCoreCodeInterpreter" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config

        return {
            "agentCoreCodeInterpreter": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config.serialize_json(
                value["agentCoreCodeInterpreter"]
            )
        }
    else:
        raise SerializationError("HarnessToolConfiguration: no variant present")


def deserialize_json(data: dict) -> HarnessToolConfiguration:
    if "remoteMcp" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_remote_mcp_config

        return {
            "remoteMcp": aws_sdk_bedrock_agentcore_control.types.harness_remote_mcp_config.deserialize_json(
                data["remoteMcp"]
            )
        }
    elif "agentCoreBrowser" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_browser_config

        return {
            "agentCoreBrowser": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_browser_config.deserialize_json(
                data["agentCoreBrowser"]
            )
        }
    elif "agentCoreGateway" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_gateway_config

        return {
            "agentCoreGateway": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_gateway_config.deserialize_json(
                data["agentCoreGateway"]
            )
        }
    elif "inlineFunction" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_inline_function_config

        return {
            "inlineFunction": aws_sdk_bedrock_agentcore_control.types.harness_inline_function_config.deserialize_json(
                data["inlineFunction"]
            )
        }
    elif "agentCoreCodeInterpreter" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config

        return {
            "agentCoreCodeInterpreter": aws_sdk_bedrock_agentcore_control.types.harness_agent_core_code_interpreter_config.deserialize_json(
                data["agentCoreCodeInterpreter"]
            )
        }
    else:
        raise DeserializationError(
            "HarnessToolConfiguration: no recognized variant key"
        )
