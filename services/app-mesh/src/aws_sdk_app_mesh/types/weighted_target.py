"""Generated from Smithy shape ``com.amazonaws.appmesh#WeightedTarget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_app_mesh.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_app_mesh.types.listener_port
    import aws_sdk_app_mesh.types.percent_int
    import aws_sdk_app_mesh.types.resource_name


class WeightedTarget(TypedDict, closed=True):
    virtual_node: "aws_sdk_app_mesh.types.resource_name.ResourceName"
    """<p>The virtual node to associate with the weighted target.</p>"""
    weight: "aws_sdk_app_mesh.types.percent_int.PercentInt"
    """<p>The relative weight of the weighted target.</p>"""
    port: NotRequired["aws_sdk_app_mesh.types.listener_port.ListenerPort"]
    """<p>The targeted port of the weighted object.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WeightedTarget) -> dict:
    out: dict = {}
    out["virtualNode"] = value["virtual_node"]
    out["weight"] = value.get("weight", 0)
    if "port" in value:
        out["port"] = value["port"]
    return out


def deserialize_json(data: dict) -> WeightedTarget:
    out: WeightedTarget = {}  # type: ignore[typeddict-item]
    if "virtualNode" in data:
        out["virtual_node"] = data["virtualNode"]
    else:
        raise DeserializationError("WeightedTarget.virtual_node required")
    if "weight" in data:
        out["weight"] = data["weight"]
    else:
        out["weight"] = 0
    if "port" in data:
        out["port"] = data["port"]
    return out
