"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#CustomerAgentlessCollectorInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.integer


class CustomerAgentlessCollectorInfo(TypedDict, closed=True):
    active_agentless_collectors: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p>The number of active Agentless Collector collectors. </p>"""
    healthy_agentless_collectors: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p>The number of healthy Agentless Collector collectors. </p>"""
    deny_listed_agentless_collectors: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p>The number of deny-listed Agentless Collector collectors. </p>"""
    shutdown_agentless_collectors: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p>The number of Agentless Collector collectors with <code>SHUTDOWN</code> status. </p>"""
    unhealthy_agentless_collectors: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p> The number of unhealthy Agentless Collector collectors. </p>"""
    total_agentless_collectors: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p> The total number of Agentless Collector collectors. </p>"""
    unknown_agentless_collectors: (
        "capo_application_discovery_service.types.integer.Integer"
    )
    """<p> The number of unknown Agentless Collector collectors. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomerAgentlessCollectorInfo) -> dict:
    out: dict = {}
    out["activeAgentlessCollectors"] = value.get("active_agentless_collectors", 0)
    out["healthyAgentlessCollectors"] = value.get("healthy_agentless_collectors", 0)
    out["denyListedAgentlessCollectors"] = value.get(
        "deny_listed_agentless_collectors", 0
    )
    out["shutdownAgentlessCollectors"] = value.get("shutdown_agentless_collectors", 0)
    out["unhealthyAgentlessCollectors"] = value.get("unhealthy_agentless_collectors", 0)
    out["totalAgentlessCollectors"] = value.get("total_agentless_collectors", 0)
    out["unknownAgentlessCollectors"] = value.get("unknown_agentless_collectors", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> CustomerAgentlessCollectorInfo:
    out: CustomerAgentlessCollectorInfo = {}  # type: ignore[typeddict-item]
    if "activeAgentlessCollectors" in data:
        out["active_agentless_collectors"] = data["activeAgentlessCollectors"]
    else:
        out["active_agentless_collectors"] = 0
    if "healthyAgentlessCollectors" in data:
        out["healthy_agentless_collectors"] = data["healthyAgentlessCollectors"]
    else:
        out["healthy_agentless_collectors"] = 0
    if "denyListedAgentlessCollectors" in data:
        out["deny_listed_agentless_collectors"] = data["denyListedAgentlessCollectors"]
    else:
        out["deny_listed_agentless_collectors"] = 0
    if "shutdownAgentlessCollectors" in data:
        out["shutdown_agentless_collectors"] = data["shutdownAgentlessCollectors"]
    else:
        out["shutdown_agentless_collectors"] = 0
    if "unhealthyAgentlessCollectors" in data:
        out["unhealthy_agentless_collectors"] = data["unhealthyAgentlessCollectors"]
    else:
        out["unhealthy_agentless_collectors"] = 0
    if "totalAgentlessCollectors" in data:
        out["total_agentless_collectors"] = data["totalAgentlessCollectors"]
    else:
        out["total_agentless_collectors"] = 0
    if "unknownAgentlessCollectors" in data:
        out["unknown_agentless_collectors"] = data["unknownAgentlessCollectors"]
    else:
        out["unknown_agentless_collectors"] = 0
    return out
