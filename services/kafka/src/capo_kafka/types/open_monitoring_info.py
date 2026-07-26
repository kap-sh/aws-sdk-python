"""Generated from Smithy shape ``com.amazonaws.kafka#OpenMonitoringInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.prometheus_info


class OpenMonitoringInfo(TypedDict, closed=True):
    prometheus: NotRequired["capo_kafka.types.prometheus_info.PrometheusInfo"]
    """<p>Prometheus settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenMonitoringInfo) -> dict:
    out: dict = {}
    if "prometheus" in value:
        import capo_kafka.types.prometheus_info

        out["prometheus"] = capo_kafka.types.prometheus_info.serialize_json(
            value["prometheus"]
        )
    return out


def deserialize_json(data: dict) -> OpenMonitoringInfo:
    out: OpenMonitoringInfo = {}  # type: ignore[typeddict-item]
    if "prometheus" in data:
        import capo_kafka.types.prometheus_info

        out["prometheus"] = capo_kafka.types.prometheus_info.deserialize_json(
            data["prometheus"]
        )
    return out
