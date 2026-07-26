"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#BedrockModelConfigurations``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.performance_configuration


class BedrockModelConfigurations(TypedDict, closed=True):
    performance_config: NotRequired[
        "capo_bedrock_agent_runtime.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>The performance configuration for the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BedrockModelConfigurations) -> dict:
    out: dict = {}
    if "performance_config" in value:
        import capo_bedrock_agent_runtime.types.performance_configuration

        out["performanceConfig"] = (
            capo_bedrock_agent_runtime.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> BedrockModelConfigurations:
    out: BedrockModelConfigurations = {}  # type: ignore[typeddict-item]
    if "performanceConfig" in data:
        import capo_bedrock_agent_runtime.types.performance_configuration

        out["performance_config"] = (
            capo_bedrock_agent_runtime.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    return out
