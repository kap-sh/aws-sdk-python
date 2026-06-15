"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#NetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.network_mode
    import aws_sdk_bedrock_agentcore_control.types.vpc_config


class NetworkConfiguration(TypedDict):
    network_mode: "aws_sdk_bedrock_agentcore_control.types.network_mode.NetworkMode"
    """<p>The network mode for the AgentCore Runtime.</p>"""
    network_mode_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.vpc_config.VpcConfig"
    ]
    """<p>The network mode configuration for the AgentCore Runtime.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NetworkConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.network_mode

    out["networkMode"] = (
        aws_sdk_bedrock_agentcore_control.types.network_mode.serialize_json(
            value["network_mode"]
        )
    )
    if "network_mode_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.vpc_config

        out["networkModeConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.vpc_config.serialize_json(
                value["network_mode_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> NetworkConfiguration:
    out: NetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "networkMode" in data:
        import aws_sdk_bedrock_agentcore_control.types.network_mode

        out["network_mode"] = (
            aws_sdk_bedrock_agentcore_control.types.network_mode.deserialize_json(
                data["networkMode"]
            )
        )
    else:
        raise DeserializationError("NetworkConfiguration.network_mode required")
    if "networkModeConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.vpc_config

        out["network_mode_config"] = (
            aws_sdk_bedrock_agentcore_control.types.vpc_config.deserialize_json(
                data["networkModeConfig"]
            )
        )
    return out
