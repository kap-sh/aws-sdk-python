"""Generated from Smithy shape ``com.amazonaws.inspector#AgentFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_inspector.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_inspector.types.agent_health_code_list
    import aws_sdk_inspector.types.agent_health_list


class AgentFilter(TypedDict, closed=True):
    agent_healths: "aws_sdk_inspector.types.agent_health_list.AgentHealthList"
    """<p>The current health state of the agent. Values can be set to <b>HEALTHY</b> or <b>UNHEALTHY</b>.</p>"""
    agent_health_codes: (
        "aws_sdk_inspector.types.agent_health_code_list.AgentHealthCodeList"
    )
    """<p>The detailed health state of the agent. Values can be set to <b>IDLE</b>, <b>RUNNING</b>, <b>SHUTDOWN</b>, <b>UNHEALTHY</b>, <b>THROTTLED</b>, and <b>UNKNOWN</b>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentFilter) -> dict:
    out: dict = {}
    import aws_sdk_inspector.types.agent_health_list

    out["agentHealths"] = (
        aws_sdk_inspector.types.agent_health_list.serialize_aws_json_1_1(
            value["agent_healths"]
        )
    )
    import aws_sdk_inspector.types.agent_health_code_list

    out["agentHealthCodes"] = (
        aws_sdk_inspector.types.agent_health_code_list.serialize_aws_json_1_1(
            value["agent_health_codes"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentFilter:
    out: AgentFilter = {}  # type: ignore[typeddict-item]
    if "agentHealths" in data:
        import aws_sdk_inspector.types.agent_health_list

        out["agent_healths"] = (
            aws_sdk_inspector.types.agent_health_list.deserialize_aws_json_1_1(
                data["agentHealths"]
            )
        )
    else:
        raise DeserializationError("AgentFilter.agent_healths required")
    if "agentHealthCodes" in data:
        import aws_sdk_inspector.types.agent_health_code_list

        out["agent_health_codes"] = (
            aws_sdk_inspector.types.agent_health_code_list.deserialize_aws_json_1_1(
                data["agentHealthCodes"]
            )
        )
    else:
        raise DeserializationError("AgentFilter.agent_health_codes required")
    return out
