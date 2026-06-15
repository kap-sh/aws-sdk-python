"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#BrowserNetworkConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.browser_network_mode
    import aws_sdk_bedrock_agentcore_control.types.vpc_config


class BrowserNetworkConfiguration(TypedDict):
    network_mode: "aws_sdk_bedrock_agentcore_control.types.browser_network_mode.BrowserNetworkMode"
    """<p>The network mode for the browser. This field specifies how the browser connects to the network.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.vpc_config.VpcConfig"
    ]
    """<p>The VPC configuration for the browser. This configuration is required when the network mode is set to <code>VPC</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BrowserNetworkConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agentcore_control.types.browser_network_mode

    out["networkMode"] = (
        aws_sdk_bedrock_agentcore_control.types.browser_network_mode.serialize_json(
            value.get("network_mode", "PUBLIC")
        )
    )
    if "vpc_config" in value:
        import aws_sdk_bedrock_agentcore_control.types.vpc_config

        out["vpcConfig"] = (
            aws_sdk_bedrock_agentcore_control.types.vpc_config.serialize_json(
                value["vpc_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> BrowserNetworkConfiguration:
    out: BrowserNetworkConfiguration = {}  # type: ignore[typeddict-item]
    if "networkMode" in data:
        import aws_sdk_bedrock_agentcore_control.types.browser_network_mode

        out["network_mode"] = (
            aws_sdk_bedrock_agentcore_control.types.browser_network_mode.deserialize_json(
                data["networkMode"]
            )
        )
    else:
        out["network_mode"] = "PUBLIC"
    if "vpcConfig" in data:
        import aws_sdk_bedrock_agentcore_control.types.vpc_config

        out["vpc_config"] = (
            aws_sdk_bedrock_agentcore_control.types.vpc_config.deserialize_json(
                data["vpcConfig"]
            )
        )
    return out
