"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#UpdatedHarnessMemoryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.harness_memory_configuration


class UpdatedHarnessMemoryConfiguration(TypedDict, closed=True):
    optional_value: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_memory_configuration.HarnessMemoryConfiguration"
    ]
    """<p>The updated memory configuration value, or null to clear the existing configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatedHarnessMemoryConfiguration) -> dict:
    out: dict = {}
    if "optional_value" in value:
        import capo_bedrock_agentcore_control.types.harness_memory_configuration

        out["optionalValue"] = (
            capo_bedrock_agentcore_control.types.harness_memory_configuration.serialize_json(
                value["optional_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatedHarnessMemoryConfiguration:
    out: UpdatedHarnessMemoryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("optionalValue") is not None:
        import capo_bedrock_agentcore_control.types.harness_memory_configuration

        out["optional_value"] = (
            capo_bedrock_agentcore_control.types.harness_memory_configuration.deserialize_json(
                data["optionalValue"]
            )
        )
    return out
