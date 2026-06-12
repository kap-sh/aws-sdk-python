"""Generated from Smithy shape ``com.amazonaws.kafka#PrometheusInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.jmx_exporter_info
    import aws_sdk_kafka.types.node_exporter_info


class PrometheusInfo(TypedDict):
    jmx_exporter: NotRequired["aws_sdk_kafka.types.jmx_exporter_info.JmxExporterInfo"]
    """<p>Indicates whether you want to turn on or turn off the JMX Exporter.</p>"""
    node_exporter: NotRequired[
        "aws_sdk_kafka.types.node_exporter_info.NodeExporterInfo"
    ]
    """<p>Indicates whether you want to turn on or turn off the Node Exporter.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PrometheusInfo) -> dict:
    out: dict = {}
    if "jmx_exporter" in value:
        import aws_sdk_kafka.types.jmx_exporter_info

        out["jmxExporter"] = aws_sdk_kafka.types.jmx_exporter_info.serialize_json(
            value["jmx_exporter"]
        )
    if "node_exporter" in value:
        import aws_sdk_kafka.types.node_exporter_info

        out["nodeExporter"] = aws_sdk_kafka.types.node_exporter_info.serialize_json(
            value["node_exporter"]
        )
    return out


def deserialize_json(data: dict) -> PrometheusInfo:
    out: PrometheusInfo = {}  # type: ignore[typeddict-item]
    if "jmxExporter" in data:
        import aws_sdk_kafka.types.jmx_exporter_info

        out["jmx_exporter"] = aws_sdk_kafka.types.jmx_exporter_info.deserialize_json(
            data["jmxExporter"]
        )
    if "nodeExporter" in data:
        import aws_sdk_kafka.types.node_exporter_info

        out["node_exporter"] = aws_sdk_kafka.types.node_exporter_info.deserialize_json(
            data["nodeExporter"]
        )
    return out
