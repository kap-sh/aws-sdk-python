"""Generated from Smithy shape ``com.amazonaws.finspace#CapacityConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_finspace.types.node_count
    import aws_sdk_finspace.types.node_type


class CapacityConfiguration(TypedDict, closed=True):
    node_type: NotRequired["aws_sdk_finspace.types.node_type.NodeType"]
    """<p>The type that determines the hardware of the host computer used for your cluster instance. Each node type offers different memory and storage capabilities. Choose a node type based on the requirements of the application or software that you plan to run on your instance.</p> <p>You can only specify one of the following values:</p> <ul> <li> <p> <code>kx.s.large</code> – The node type with a configuration of 12 GiB memory and 2 vCPUs.</p> </li> <li> <p> <code>kx.s.xlarge</code> – The node type with a configuration of 27 GiB memory and 4 vCPUs.</p> </li> <li> <p> <code>kx.s.2xlarge</code> – The node type with a configuration of 54 GiB memory and 8 vCPUs.</p> </li> <li> <p> <code>kx.s.4xlarge</code> – The node type with a configuration of 108 GiB memory and 16 vCPUs.</p> </li> <li> <p> <code>kx.s.8xlarge</code> – The node type with a configuration of 216 GiB memory and 32 vCPUs.</p> </li> <li> <p> <code>kx.s.16xlarge</code> – The node type with a configuration of 432 GiB memory and 64 vCPUs.</p> </li> <li> <p> <code>kx.s.32xlarge</code> – The node type with a configuration of 864 GiB memory and 128 vCPUs.</p> </li> </ul>"""
    node_count: NotRequired["aws_sdk_finspace.types.node_count.NodeCount"]
    """<p>The number of instances running in a cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CapacityConfiguration) -> dict:
    out: dict = {}
    if "node_type" in value:
        out["nodeType"] = value["node_type"]
    if "node_count" in value:
        out["nodeCount"] = value["node_count"]
    return out


def deserialize_json(data: dict) -> CapacityConfiguration:
    out: CapacityConfiguration = {}  # type: ignore[typeddict-item]
    if "nodeType" in data:
        out["node_type"] = data["nodeType"]
    if "nodeCount" in data:
        out["node_count"] = data["nodeCount"]
    return out
