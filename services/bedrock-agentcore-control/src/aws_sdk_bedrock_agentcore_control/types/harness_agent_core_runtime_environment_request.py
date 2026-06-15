"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessAgentCoreRuntimeEnvironmentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations
    import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration
    import aws_sdk_bedrock_agentcore_control.types.network_configuration


class HarnessAgentCoreRuntimeEnvironmentRequest(TypedDict):
    lifecycle_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.LifecycleConfiguration"
    ]
    network_configuration: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.network_configuration.NetworkConfiguration"
    ]
    filesystem_configurations: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.FilesystemConfigurations"
    ]
    """<p>The filesystem configurations for the runtime environment.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessAgentCoreRuntimeEnvironmentRequest) -> dict:
    out: dict = {}
    if "lifecycle_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycleConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.serialize_json(
                value["lifecycle_configuration"]
            )
        )
    if "network_configuration" in value:
        import aws_sdk_bedrock_agentcore_control.types.network_configuration

        out["networkConfiguration"] = (
            aws_sdk_bedrock_agentcore_control.types.network_configuration.serialize_json(
                value["network_configuration"]
            )
        )
    if "filesystem_configurations" in value:
        import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystemConfigurations"] = (
            aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.serialize_json(
                value["filesystem_configurations"]
            )
        )
    return out


def deserialize_json(data: dict) -> HarnessAgentCoreRuntimeEnvironmentRequest:
    out: HarnessAgentCoreRuntimeEnvironmentRequest = {}  # type: ignore[typeddict-item]
    if "lifecycleConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration

        out["lifecycle_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.lifecycle_configuration.deserialize_json(
                data["lifecycleConfiguration"]
            )
        )
    if "networkConfiguration" in data:
        import aws_sdk_bedrock_agentcore_control.types.network_configuration

        out["network_configuration"] = (
            aws_sdk_bedrock_agentcore_control.types.network_configuration.deserialize_json(
                data["networkConfiguration"]
            )
        )
    if "filesystemConfigurations" in data:
        import aws_sdk_bedrock_agentcore_control.types.filesystem_configurations

        out["filesystem_configurations"] = (
            aws_sdk_bedrock_agentcore_control.types.filesystem_configurations.deserialize_json(
                data["filesystemConfigurations"]
            )
        )
    return out
