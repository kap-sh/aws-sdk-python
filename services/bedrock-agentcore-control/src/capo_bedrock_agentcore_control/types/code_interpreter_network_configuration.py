"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#CodeInterpreterNetworkConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.code_interpreter_network_mode
    import capo_bedrock_agentcore_control.types.vpc_config


class CodeInterpreterNetworkConfiguration(TypedDict, closed=True):
    network_mode: "capo_bedrock_agentcore_control.types.code_interpreter_network_mode.CodeInterpreterNetworkMode"
    """<p>The network mode for the code interpreter. This field specifies how the code interpreter connects to the network.</p>"""
    vpc_config: NotRequired["capo_bedrock_agentcore_control.types.vpc_config.VpcConfig"]
    """<p>The VPC configuration for the code interpreter. This configuration is required when the network mode is set to <code>VPC</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CodeInterpreterNetworkConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.code_interpreter_network_mode

    out["networkMode"] = (
        capo_bedrock_agentcore_control.types.code_interpreter_network_mode.serialize_json(
            value.get("network_mode", "SANDBOX")
        )
    )
    if "vpc_config" in value:
        import capo_bedrock_agentcore_control.types.vpc_config

        out["vpcConfig"] = (
            capo_bedrock_agentcore_control.types.vpc_config.serialize_json(
                value["vpc_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CodeInterpreterNetworkConfiguration:
    out: CodeInterpreterNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "networkMode" in data:
        import capo_bedrock_agentcore_control.types.code_interpreter_network_mode

        out["network_mode"] = (
            capo_bedrock_agentcore_control.types.code_interpreter_network_mode.deserialize_json(
                data["networkMode"]
            )
        )
    else:
        out["network_mode"] = "SANDBOX"
    if "vpcConfig" in data:
        import capo_bedrock_agentcore_control.types.vpc_config

        out["vpc_config"] = (
            capo_bedrock_agentcore_control.types.vpc_config.deserialize_json(
                data["vpcConfig"]
            )
        )
    return out
