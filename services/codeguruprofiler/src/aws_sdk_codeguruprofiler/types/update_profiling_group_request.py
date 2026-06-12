"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#UpdateProfilingGroupRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_codeguruprofiler.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_codeguruprofiler.types.agent_orchestration_config
    import aws_sdk_codeguruprofiler.types.profiling_group_name


class UpdateProfilingGroupRequest(TypedDict):
    profiling_group_name: (
        "aws_sdk_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group to update.</p>"""
    agent_orchestration_config: "aws_sdk_codeguruprofiler.types.agent_orchestration_config.AgentOrchestrationConfig"
    """<p> Specifies whether profiling is enabled or disabled for a profiling group. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateProfilingGroupRequest) -> dict:
    out: dict = {}
    import aws_sdk_codeguruprofiler.types.agent_orchestration_config

    out["agentOrchestrationConfig"] = (
        aws_sdk_codeguruprofiler.types.agent_orchestration_config.serialize_json(
            value["agent_orchestration_config"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateProfilingGroupRequest:
    out: UpdateProfilingGroupRequest = {}  # type: ignore[typeddict-item]
    if "agentOrchestrationConfig" in data:
        import aws_sdk_codeguruprofiler.types.agent_orchestration_config

        out["agent_orchestration_config"] = (
            aws_sdk_codeguruprofiler.types.agent_orchestration_config.deserialize_json(
                data["agentOrchestrationConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateProfilingGroupRequest.agent_orchestration_config required"
        )
    return out
