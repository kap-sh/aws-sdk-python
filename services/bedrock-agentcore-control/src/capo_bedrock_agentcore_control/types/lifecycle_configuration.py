"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LifecycleConfiguration``."""

from typing_extensions import NotRequired, TypedDict


class LifecycleConfiguration(TypedDict, closed=True):
    idle_runtime_session_timeout: NotRequired["int"]
    """<p>Timeout in seconds for idle runtime sessions. When a session remains idle for this duration, it will be automatically terminated. Default: 900 seconds (15 minutes).</p>"""
    max_lifetime: NotRequired["int"]
    """<p>Maximum lifetime for the instance in seconds. Once reached, instances will be automatically terminated and replaced. Default: 28800 seconds (8 hours).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LifecycleConfiguration) -> dict:
    out: dict = {}
    if "idle_runtime_session_timeout" in value:
        out["idleRuntimeSessionTimeout"] = value["idle_runtime_session_timeout"]
    if "max_lifetime" in value:
        out["maxLifetime"] = value["max_lifetime"]
    return out


def deserialize_json(data: dict) -> LifecycleConfiguration:
    out: LifecycleConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("idleRuntimeSessionTimeout") is not None:
        out["idle_runtime_session_timeout"] = data["idleRuntimeSessionTimeout"]
    if data.get("maxLifetime") is not None:
        out["max_lifetime"] = data["maxLifetime"]
    return out
