"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#AgentOrchestrationConfig``."""

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError


class AgentOrchestrationConfig(TypedDict, closed=True):
    profiling_enabled: "bool"
    """<p> A <code>Boolean</code> that specifies whether the profiling agent collects profiling data or not. Set to <code>true</code> to enable profiling. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AgentOrchestrationConfig) -> dict:
    out: dict = {}
    out["profilingEnabled"] = value["profiling_enabled"]
    return out


def deserialize_json(data: dict) -> AgentOrchestrationConfig:
    out: AgentOrchestrationConfig = {}  # type: ignore[typeddict-item]
    if "profilingEnabled" in data:
        out["profiling_enabled"] = data["profilingEnabled"]
    else:
        raise DeserializationError(
            "AgentOrchestrationConfig.profiling_enabled required"
        )
    return out
