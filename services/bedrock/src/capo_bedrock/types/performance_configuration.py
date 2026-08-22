"""Generated from Smithy shape ``com.amazonaws.bedrock#PerformanceConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.performance_config_latency


class PerformanceConfiguration(TypedDict, closed=True):
    latency: NotRequired[
        "capo_bedrock.types.performance_config_latency.PerformanceConfigLatency"
    ]
    """<p>Specifies whether to use the latency-optimized or standard version of a model or inference profile.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PerformanceConfiguration) -> dict:
    out: dict = {}
    if "latency" in value:
        import capo_bedrock.types.performance_config_latency

        out["latency"] = capo_bedrock.types.performance_config_latency.serialize_json(
            value["latency"]
        )
    return out


def deserialize_json(data: dict) -> PerformanceConfiguration:
    out: PerformanceConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("latency") is not None:
        import capo_bedrock.types.performance_config_latency

        out["latency"] = capo_bedrock.types.performance_config_latency.deserialize_json(
            data["latency"]
        )
    return out
