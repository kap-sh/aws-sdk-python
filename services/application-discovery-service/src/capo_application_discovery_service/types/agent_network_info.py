"""Generated from Smithy shape ``com.amazonaws.applicationdiscoveryservice#AgentNetworkInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_application_discovery_service.types.string


class AgentNetworkInfo(TypedDict, closed=True):
    ip_address: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>The IP address for the host where the agent/collector resides.</p>"""
    mac_address: NotRequired["capo_application_discovery_service.types.string.String"]
    """<p>The MAC address for the host where the agent/collector resides.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AgentNetworkInfo) -> dict:
    out: dict = {}
    if "ip_address" in value:
        out["ipAddress"] = value["ip_address"]
    if "mac_address" in value:
        out["macAddress"] = value["mac_address"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AgentNetworkInfo:
    out: AgentNetworkInfo = {}  # type: ignore[typeddict-item]
    if "ipAddress" in data:
        out["ip_address"] = data["ipAddress"]
    if "macAddress" in data:
        out["mac_address"] = data["macAddress"]
    return out
