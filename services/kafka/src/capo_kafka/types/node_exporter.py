"""Generated from Smithy shape ``com.amazonaws.kafka#NodeExporter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__boolean


class NodeExporter(TypedDict, closed=True):
    enabled_in_broker: NotRequired["capo_kafka.types.__boolean.__boolean"]
    """<p>Indicates whether you want to turn on or turn off the Node Exporter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeExporter) -> dict:
    out: dict = {}
    if "enabled_in_broker" in value:
        out["enabledInBroker"] = value["enabled_in_broker"]
    return out


def deserialize_json(data: dict) -> NodeExporter:
    out: NodeExporter = {}  # type: ignore[typeddict-item]
    if "enabledInBroker" in data:
        out["enabled_in_broker"] = data["enabledInBroker"]
    return out
