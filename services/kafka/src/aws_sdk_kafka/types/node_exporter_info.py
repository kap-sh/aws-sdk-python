"""Generated from Smithy shape ``com.amazonaws.kafka#NodeExporterInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__boolean


class NodeExporterInfo(TypedDict):
    enabled_in_broker: NotRequired["aws_sdk_kafka.types.__boolean.__boolean"]
    """<p>Indicates whether you want to turn on or turn off the Node Exporter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeExporterInfo) -> dict:
    out: dict = {}
    if "enabled_in_broker" in value:
        out["enabledInBroker"] = value["enabled_in_broker"]
    return out


def deserialize_json(data: dict) -> NodeExporterInfo:
    out: NodeExporterInfo = {}  # type: ignore[typeddict-item]
    if "enabledInBroker" in data:
        out["enabled_in_broker"] = data["enabledInBroker"]
    return out
