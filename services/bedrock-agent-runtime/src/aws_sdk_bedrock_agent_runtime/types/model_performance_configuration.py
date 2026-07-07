"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#ModelPerformanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent_runtime.types.performance_configuration


class ModelPerformanceConfiguration(TypedDict, closed=True):
    performance_config: NotRequired[
        "aws_sdk_bedrock_agent_runtime.types.performance_configuration.PerformanceConfiguration"
    ]
    """<p>The latency configuration for the model.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ModelPerformanceConfiguration) -> dict:
    out: dict = {}
    if "performance_config" in value:
        import aws_sdk_bedrock_agent_runtime.types.performance_configuration

        out["performanceConfig"] = (
            aws_sdk_bedrock_agent_runtime.types.performance_configuration.serialize_json(
                value["performance_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> ModelPerformanceConfiguration:
    out: ModelPerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if "performanceConfig" in data:
        import aws_sdk_bedrock_agent_runtime.types.performance_configuration

        out["performance_config"] = (
            aws_sdk_bedrock_agent_runtime.types.performance_configuration.deserialize_json(
                data["performanceConfig"]
            )
        )
    return out
