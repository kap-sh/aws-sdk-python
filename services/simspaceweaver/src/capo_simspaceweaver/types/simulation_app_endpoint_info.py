"""Generated from Smithy shape ``com.amazonaws.simspaceweaver#SimulationAppEndpointInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_simspaceweaver.types.app_port_mappings
    import capo_simspaceweaver.types.non_empty_string


class SimulationAppEndpointInfo(TypedDict, closed=True):
    address: NotRequired["capo_simspaceweaver.types.non_empty_string.NonEmptyString"]
    """<p>The IP address of the app. SimSpace Weaver dynamically assigns this IP address when the app starts.</p>"""
    ingress_port_mappings: NotRequired[
        "capo_simspaceweaver.types.app_port_mappings.AppPortMappings"
    ]
    """<p>The inbound TCP/UDP port numbers of the app. The combination of an IP address and a port number form a network endpoint.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SimulationAppEndpointInfo) -> dict:
    out: dict = {}
    if "address" in value:
        out["Address"] = value["address"]
    if "ingress_port_mappings" in value:
        import capo_simspaceweaver.types.app_port_mappings

        out["IngressPortMappings"] = (
            capo_simspaceweaver.types.app_port_mappings.serialize_json(
                value["ingress_port_mappings"]
            )
        )
    return out


def deserialize_json(data: dict) -> SimulationAppEndpointInfo:
    out: SimulationAppEndpointInfo = {}  # type: ignore[typeddict-item]
    if "Address" in data:
        out["address"] = data["Address"]
    if "IngressPortMappings" in data:
        import capo_simspaceweaver.types.app_port_mappings

        out["ingress_port_mappings"] = (
            capo_simspaceweaver.types.app_port_mappings.deserialize_json(
                data["IngressPortMappings"]
            )
        )
    return out
