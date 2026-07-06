"""Generated from Smithy shape ``com.amazonaws.bedrockagent#PerformanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_agent.types.performance_config_latency


class PerformanceConfiguration(TypedDict, closed=True):
    latency: "aws_sdk_bedrock_agent.types.performance_config_latency.PerformanceConfigLatency"
    """<p>The latency optimization setting.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceConfiguration) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_agent.types.performance_config_latency

    out["latency"] = (
        aws_sdk_bedrock_agent.types.performance_config_latency.serialize_json(
            value.get("latency", "standard")
        )
    )
    return out


def deserialize_json(data: dict) -> PerformanceConfiguration:
    out: PerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if "latency" in data:
        import aws_sdk_bedrock_agent.types.performance_config_latency

        out["latency"] = (
            aws_sdk_bedrock_agent.types.performance_config_latency.deserialize_json(
                data["latency"]
            )
        )
    else:
        out["latency"] = "standard"
    return out
