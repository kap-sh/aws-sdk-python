"""Generated from Smithy shape ``com.amazonaws.kafka#Prometheus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.jmx_exporter
    import capo_kafka.types.node_exporter


class Prometheus(TypedDict, closed=True):
    jmx_exporter: NotRequired["capo_kafka.types.jmx_exporter.JmxExporter"]
    """<p>Indicates whether you want to turn on or turn off the JMX Exporter.</p>"""
    node_exporter: NotRequired["capo_kafka.types.node_exporter.NodeExporter"]
    """<p>Indicates whether you want to turn on or turn off the Node Exporter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Prometheus) -> dict:
    out: dict = {}
    if "jmx_exporter" in value:
        import capo_kafka.types.jmx_exporter

        out["jmxExporter"] = capo_kafka.types.jmx_exporter.serialize_json(
            value["jmx_exporter"]
        )
    if "node_exporter" in value:
        import capo_kafka.types.node_exporter

        out["nodeExporter"] = capo_kafka.types.node_exporter.serialize_json(
            value["node_exporter"]
        )
    return out


def deserialize_json(data: dict) -> Prometheus:
    out: Prometheus = {}  # type: ignore[typeddict-item]
    if "jmxExporter" in data:
        import capo_kafka.types.jmx_exporter

        out["jmx_exporter"] = capo_kafka.types.jmx_exporter.deserialize_json(
            data["jmxExporter"]
        )
    if "nodeExporter" in data:
        import capo_kafka.types.node_exporter

        out["node_exporter"] = capo_kafka.types.node_exporter.deserialize_json(
            data["nodeExporter"]
        )
    return out
