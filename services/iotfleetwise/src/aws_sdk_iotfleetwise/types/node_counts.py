"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NodeCounts``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotfleetwise.types.number


class NodeCounts(TypedDict):
    total_nodes: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The total number of nodes in a vehicle network.</p>"""
    total_branches: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The total number of nodes in a vehicle network that represent branches.</p>"""
    total_sensors: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The total number of nodes in a vehicle network that represent sensors.</p>"""
    total_attributes: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The total number of nodes in a vehicle network that represent attributes.</p>"""
    total_actuators: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The total number of nodes in a vehicle network that represent actuators.</p>"""
    total_structs: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The total structure for the node.</p>"""
    total_properties: "aws_sdk_iotfleetwise.types.number.number"
    """<p>The total properties for the node.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NodeCounts) -> dict:
    out: dict = {}
    out["totalNodes"] = value.get("total_nodes", 0)
    out["totalBranches"] = value.get("total_branches", 0)
    out["totalSensors"] = value.get("total_sensors", 0)
    out["totalAttributes"] = value.get("total_attributes", 0)
    out["totalActuators"] = value.get("total_actuators", 0)
    out["totalStructs"] = value.get("total_structs", 0)
    out["totalProperties"] = value.get("total_properties", 0)
    return out


def deserialize_aws_json_1_0(data: dict) -> NodeCounts:
    out: NodeCounts = {}  # type: ignore[typeddict-item]
    if "totalNodes" in data:
        out["total_nodes"] = data["totalNodes"]
    else:
        out["total_nodes"] = 0
    if "totalBranches" in data:
        out["total_branches"] = data["totalBranches"]
    else:
        out["total_branches"] = 0
    if "totalSensors" in data:
        out["total_sensors"] = data["totalSensors"]
    else:
        out["total_sensors"] = 0
    if "totalAttributes" in data:
        out["total_attributes"] = data["totalAttributes"]
    else:
        out["total_attributes"] = 0
    if "totalActuators" in data:
        out["total_actuators"] = data["totalActuators"]
    else:
        out["total_actuators"] = 0
    if "totalStructs" in data:
        out["total_structs"] = data["totalStructs"]
    else:
        out["total_structs"] = 0
    if "totalProperties" in data:
        out["total_properties"] = data["totalProperties"]
    else:
        out["total_properties"] = 0
    return out
