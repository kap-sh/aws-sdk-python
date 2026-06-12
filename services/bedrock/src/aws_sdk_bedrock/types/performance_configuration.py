"""Generated from Smithy shape ``com.amazonaws.bedrock#PerformanceConfiguration``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock.types.performance_config_latency


class PerformanceConfiguration(TypedDict):
    latency: NotRequired[
        "aws_sdk_bedrock.types.performance_config_latency.PerformanceConfigLatency"
    ]
    """<p>Specifies whether to use the latency-optimized or standard version of a model or inference profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceConfiguration) -> dict:
    out: dict = {}
    if "latency" in value:
        import aws_sdk_bedrock.types.performance_config_latency

        out["latency"] = (
            aws_sdk_bedrock.types.performance_config_latency.serialize_json(
                value["latency"]
            )
        )
    return out


def deserialize_json(data: dict) -> PerformanceConfiguration:
    out: PerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if "latency" in data:
        import aws_sdk_bedrock.types.performance_config_latency

        out["latency"] = (
            aws_sdk_bedrock.types.performance_config_latency.deserialize_json(
                data["latency"]
            )
        )
    return out
