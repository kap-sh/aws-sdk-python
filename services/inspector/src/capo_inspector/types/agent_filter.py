"""Generated from Smithy shape ``com.amazonaws.inspector#AgentFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector.types.agent_health_code_list
    import capo_inspector.types.agent_health_list


class AgentFilter(TypedDict, closed=True):
    agent_healths: "capo_inspector.types.agent_health_list.AgentHealthList"
    """<p>The current health state of the agent. Values can be set to <b>HEALTHY</b> or <b>UNHEALTHY</b>.</p>"""
    agent_health_codes: (
        "capo_inspector.types.agent_health_code_list.AgentHealthCodeList"
    )
    """<p>The detailed health state of the agent. Values can be set to <b>IDLE</b>, <b>RUNNING</b>, <b>SHUTDOWN</b>, <b>UNHEALTHY</b>, <b>THROTTLED</b>, and <b>UNKNOWN</b>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentFilter) -> dict:
    out: dict = {}
    import capo_inspector.types.agent_health_list

    out["agentHealths"] = capo_inspector.types.agent_health_list.serialize_aws_json_1_1(
        value["agent_healths"]
    )
    import capo_inspector.types.agent_health_code_list

    out["agentHealthCodes"] = (
        capo_inspector.types.agent_health_code_list.serialize_aws_json_1_1(
            value["agent_health_codes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentFilter:
    out: AgentFilter = {}  # type: ignore[typeddict-item]
    if "agentHealths" in data:
        import capo_inspector.types.agent_health_list

        out["agent_healths"] = (
            capo_inspector.types.agent_health_list.deserialize_aws_json_1_1(
                data["agentHealths"]
            )
        )
    else:
        raise DeserializationError("AgentFilter.agent_healths required")
    if "agentHealthCodes" in data:
        import capo_inspector.types.agent_health_code_list

        out["agent_health_codes"] = (
            capo_inspector.types.agent_health_code_list.deserialize_aws_json_1_1(
                data["agentHealthCodes"]
            )
        )
    else:
        raise DeserializationError("AgentFilter.agent_health_codes required")
    return out
