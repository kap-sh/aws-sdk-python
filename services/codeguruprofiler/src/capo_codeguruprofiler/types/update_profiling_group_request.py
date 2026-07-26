"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UpdateProfilingGroupRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.agent_orchestration_config
    import capo_codeguruprofiler.types.profiling_group_name


class UpdateProfilingGroupRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group to update.</p>"""
    agent_orchestration_config: "capo_codeguruprofiler.types.agent_orchestration_config.AgentOrchestrationConfig"
    """<p> Specifies whether profiling is enabled or disabled for a profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfilingGroupRequest) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.agent_orchestration_config

    out["agentOrchestrationConfig"] = (
        capo_codeguruprofiler.types.agent_orchestration_config.serialize_json(
            value["agent_orchestration_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateProfilingGroupRequest:
    out: UpdateProfilingGroupRequest = {}  # type: ignore[typeddict-item]
    if "agentOrchestrationConfig" in data:
        import capo_codeguruprofiler.types.agent_orchestration_config

        out["agent_orchestration_config"] = (
            capo_codeguruprofiler.types.agent_orchestration_config.deserialize_json(
                data["agentOrchestrationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProfilingGroupRequest.agent_orchestration_config required"
        )
    return out
