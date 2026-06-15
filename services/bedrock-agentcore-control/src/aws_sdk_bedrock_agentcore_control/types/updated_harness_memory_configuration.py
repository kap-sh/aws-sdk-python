"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedHarnessMemoryConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration


class UpdatedHarnessMemoryConfiguration(TypedDict):
    optional_value: NotRequired[
        "aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
    ]
    """<p>The updated memory configuration value, or null to clear the existing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedHarnessMemoryConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration

        out["optionalValue"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedHarnessMemoryConfiguration:
    out: UpdatedHarnessMemoryConfiguration = {}  # type: ignore[typeddict-item]
    if "optionalValue" in data:
        import aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration

        out["optional_value"] = (
            aws_sdk_bedrock_agentcore_control.types.harness_memory_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
