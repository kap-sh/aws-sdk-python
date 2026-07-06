"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ConfigurationBundleReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.gateway_configuration_bundle_arn


class ConfigurationBundleReference(TypedDict, closed=True):
    bundle_arn: "aws_sdk_bedrock_agentcore_control.types.gateway_configuration_bundle_arn.GatewayConfigurationBundleArn"
    """<p>The Amazon Resource Name (ARN) of the configuration bundle.</p>"""
    bundle_version: "str"
    """<p>The version of the configuration bundle.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationBundleReference) -> dict:
    out: dict = {}
    out["bundleArn"] = value["bundle_arn"]
    out["bundleVersion"] = value["bundle_version"]
    return out


def deserialize_json(data: dict) -> ConfigurationBundleReference:
    out: ConfigurationBundleReference = {}  # type: ignore[typeddict-item]
    if "bundleArn" in data:
        out["bundle_arn"] = data["bundleArn"]
    else:
        raise DeserializationError("ConfigurationBundleReference.bundle_arn required")
    if "bundleVersion" in data:
        out["bundle_version"] = data["bundleVersion"]
    else:
        raise DeserializationError(
            "ConfigurationBundleReference.bundle_version required"
        )
    return out
