"""Generated from Smithy shape ``com.amazonaws.kafka#OpenMonitoring``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.prometheus


class OpenMonitoring(TypedDict, closed=True):
    prometheus: NotRequired["capo_kafka.types.prometheus.Prometheus"]
    """<p>Prometheus settings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: OpenMonitoring) -> dict:
    out: dict = {}
    if "prometheus" in value:
        import capo_kafka.types.prometheus

        out["prometheus"] = capo_kafka.types.prometheus.serialize_json(
            value["prometheus"]
        )
    return out


def deserialize_json(data: dict) -> OpenMonitoring:
    out: OpenMonitoring = {}  # type: ignore[typeddict-item]
    if "prometheus" in data:
        import capo_kafka.types.prometheus

        out["prometheus"] = capo_kafka.types.prometheus.deserialize_json(
            data["prometheus"]
        )
    return out
