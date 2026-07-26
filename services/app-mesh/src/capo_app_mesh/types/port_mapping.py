"""Generated from Smithy shape ``com.amazonaws.appmesh#PortMapping``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import capo_app_mesh.types.port_number
    import capo_app_mesh.types.port_protocol


class PortMapping(TypedDict, closed=True):
    port: "capo_app_mesh.types.port_number.PortNumber"
    """<p>The port used for the port mapping.</p>"""
    protocol: "capo_app_mesh.types.port_protocol.PortProtocol"
    """<p>The protocol used for the port mapping. Specify one protocol.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PortMapping) -> dict:
    out: dict = {}
    out["port"] = value["port"]
    out["protocol"] = value["protocol"]
    return out


def deserialize_json(data: dict) -> PortMapping:
    out: PortMapping = {}  # type: ignore[typeddict-item]
    if "port" in data:
        out["port"] = data["port"]
    else:
        raise DeserializationError("PortMapping.port required")
    if "protocol" in data:
        out["protocol"] = data["protocol"]
    else:
        raise DeserializationError("PortMapping.protocol required")
    return out
