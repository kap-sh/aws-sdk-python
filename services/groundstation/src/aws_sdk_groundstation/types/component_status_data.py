"""Generated from Smithy shape ``com.amazonaws.groundstation#ComponentStatusData``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_groundstation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.agent_status
    import aws_sdk_groundstation.types.capability_arn
    import aws_sdk_groundstation.types.component_type_string
    import aws_sdk_groundstation.types.uuid


class ComponentStatusData(TypedDict):
    component_type: (
        "aws_sdk_groundstation.types.component_type_string.ComponentTypeString"
    )
    """<p>The Component type.</p>"""
    capability_arn: "aws_sdk_groundstation.types.capability_arn.CapabilityArn"
    """<p>Capability ARN of the component.</p>"""
    status: "aws_sdk_groundstation.types.agent_status.AgentStatus"
    """<p>Component status.</p>"""
    bytes_sent: NotRequired["int"]
    """<p>Bytes sent by the component.</p>"""
    bytes_received: NotRequired["int"]
    """<p>Bytes received by the component.</p>"""
    packets_dropped: NotRequired["int"]
    """<p>Packets dropped by component.</p>"""
    dataflow_id: "aws_sdk_groundstation.types.uuid.Uuid"
    """<p>Dataflow UUID associated with the component.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComponentStatusData) -> dict:
    out: dict = {}
    out["componentType"] = value["component_type"]
    out["capabilityArn"] = value["capability_arn"]
    import aws_sdk_groundstation.types.agent_status

    out["status"] = aws_sdk_groundstation.types.agent_status.serialize_json(
        value["status"]
    )
    if "bytes_sent" in value:
        out["bytesSent"] = value["bytes_sent"]
    if "bytes_received" in value:
        out["bytesReceived"] = value["bytes_received"]
    if "packets_dropped" in value:
        out["packetsDropped"] = value["packets_dropped"]
    out["dataflowId"] = value["dataflow_id"]
    return out


def deserialize_json(data: dict) -> ComponentStatusData:
    out: ComponentStatusData = {}  # type: ignore[typeddict-item]
    if "componentType" in data:
        out["component_type"] = data["componentType"]
    else:
        raise DeserializationError("ComponentStatusData.component_type required")
    if "capabilityArn" in data:
        out["capability_arn"] = data["capabilityArn"]
    else:
        raise DeserializationError("ComponentStatusData.capability_arn required")
    if "status" in data:
        import aws_sdk_groundstation.types.agent_status

        out["status"] = aws_sdk_groundstation.types.agent_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("ComponentStatusData.status required")
    if "bytesSent" in data:
        out["bytes_sent"] = data["bytesSent"]
    if "bytesReceived" in data:
        out["bytes_received"] = data["bytesReceived"]
    if "packetsDropped" in data:
        out["packets_dropped"] = data["packetsDropped"]
    if "dataflowId" in data:
        out["dataflow_id"] = data["dataflowId"]
    else:
        raise DeserializationError("ComponentStatusData.dataflow_id required")
    return out
