"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#CustomerAgentInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.integer


class CustomerAgentInfo(TypedDict, closed=True):
    active_agents: "capo_application_discovery_service.types.integer.Integer"
    """<p>Number of active discovery agents.</p>"""
    healthy_agents: "capo_application_discovery_service.types.integer.Integer"
    """<p>Number of healthy discovery agents</p>"""
    black_listed_agents: "capo_application_discovery_service.types.integer.Integer"
    """<p>Number of blacklisted discovery agents.</p>"""
    shutdown_agents: "capo_application_discovery_service.types.integer.Integer"
    """<p>Number of discovery agents with status SHUTDOWN.</p>"""
    unhealthy_agents: "capo_application_discovery_service.types.integer.Integer"
    """<p>Number of unhealthy discovery agents.</p>"""
    total_agents: "capo_application_discovery_service.types.integer.Integer"
    """<p>Total number of discovery agents.</p>"""
    unknown_agents: "capo_application_discovery_service.types.integer.Integer"
    """<p>Number of unknown discovery agents.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerAgentInfo) -> dict:
    out: dict = {}
    out["activeAgents"] = value.get("active_agents", 0)
    out["healthyAgents"] = value.get("healthy_agents", 0)
    out["blackListedAgents"] = value.get("black_listed_agents", 0)
    out["shutdownAgents"] = value.get("shutdown_agents", 0)
    out["unhealthyAgents"] = value.get("unhealthy_agents", 0)
    out["totalAgents"] = value.get("total_agents", 0)
    out["unknownAgents"] = value.get("unknown_agents", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerAgentInfo:
    out: CustomerAgentInfo = {}  # type: ignore[typeddict-item]
    if "activeAgents" in data:
        out["active_agents"] = data["activeAgents"]
    else:
        out["active_agents"] = 0
    if "healthyAgents" in data:
        out["healthy_agents"] = data["healthyAgents"]
    else:
        out["healthy_agents"] = 0
    if "blackListedAgents" in data:
        out["black_listed_agents"] = data["blackListedAgents"]
    else:
        out["black_listed_agents"] = 0
    if "shutdownAgents" in data:
        out["shutdown_agents"] = data["shutdownAgents"]
    else:
        out["shutdown_agents"] = 0
    if "unhealthyAgents" in data:
        out["unhealthy_agents"] = data["unhealthyAgents"]
    else:
        out["unhealthy_agents"] = 0
    if "totalAgents" in data:
        out["total_agents"] = data["totalAgents"]
    else:
        out["total_agents"] = 0
    if "unknownAgents" in data:
        out["unknown_agents"] = data["unknownAgents"]
    else:
        out["unknown_agents"] = 0
    return out
