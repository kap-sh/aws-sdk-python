"""Generated from Smithy shape ``com.amazonaws.panorama#NodeInputPort``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_panorama.types.description
    import capo_panorama.types.max_connections
    import capo_panorama.types.port_default_value
    import capo_panorama.types.port_name
    import capo_panorama.types.port_type


class NodeInputPort(TypedDict, closed=True):
    name: NotRequired["capo_panorama.types.port_name.PortName"]
    """<p>The input port's name.</p>"""
    description: NotRequired["capo_panorama.types.description.Description"]
    """<p>The input port's description.</p>"""
    type: NotRequired["capo_panorama.types.port_type.PortType"]
    """<p>The input port's type.</p>"""
    default_value: NotRequired[
        "capo_panorama.types.port_default_value.PortDefaultValue"
    ]
    """<p>The input port's default value.</p>"""
    max_connections: "capo_panorama.types.max_connections.MaxConnections"
    """<p>The input port's max connections.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInputPort) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "description" in value:
        out["Description"] = value["description"]
    if "type" in value:
        out["Type"] = value["type"]
    if "default_value" in value:
        out["DefaultValue"] = value["default_value"]
    out["MaxConnections"] = value.get("max_connections", 0)
    return out


def deserialize_json(data: dict) -> NodeInputPort:
    out: NodeInputPort = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Description" in data:
        out["description"] = data["Description"]
    if "Type" in data:
        out["type"] = data["Type"]
    if "DefaultValue" in data:
        out["default_value"] = data["DefaultValue"]
    if "MaxConnections" in data:
        out["max_connections"] = data["MaxConnections"]
    else:
        out["max_connections"] = 0
    return out
