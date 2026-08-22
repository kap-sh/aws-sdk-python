"""Generated from Smithy shape ``com.amazonaws.bedrockagentruntime#PerformanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent_runtime.types.performance_config_latency


class PerformanceConfiguration(TypedDict, closed=True):
    latency: "capo_bedrock_agent_runtime.types.performance_config_latency.PerformanceConfigLatency"
    """<p>To use a latency-optimized version of the model, set to <code>optimized</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceConfiguration) -> dict:
    out: dict = {}
    import capo_bedrock_agent_runtime.types.performance_config_latency

    out["latency"] = (
        capo_bedrock_agent_runtime.types.performance_config_latency.serialize_json(
            value.get("latency", "standard")
        )
    )
    return out


def deserialize_json(data: dict) -> PerformanceConfiguration:
    out: PerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("latency") is not None:
        import capo_bedrock_agent_runtime.types.performance_config_latency

        out["latency"] = (
            capo_bedrock_agent_runtime.types.performance_config_latency.deserialize_json(
                data["latency"]
            )
        )
    else:
        out["latency"] = "standard"
    return out
